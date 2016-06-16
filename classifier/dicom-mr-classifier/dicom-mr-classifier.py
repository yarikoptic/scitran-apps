#!/usr/bin/env python

import os
import json
import pytz
import dicom
import tzlocal
import logging
import zipfile
import datetime
import measurement_from_label

logging.basicConfig()
log = logging.getLogger('dicom-mr-classifier')

def parse_patient_age(age):
    """
    Parse patient age from string.
    convert from 70d, 10w, 2m, 1y to datetime.timedelta object.
    Returns age as duration in seconds.
    """
    if age == 'None':
        return None

    conversion = {  # conversion to days
        'Y': 365,
        'M': 30,
        'W': 7,
        'D': 1,
    }
    scale = age[-1:]
    value = age[:-1]
    return datetime.timedelta(int(value) * conversion.get(scale)).total_seconds()

def timestamp(date, time, timezone):
    if date and time:
        return datetime.datetime.strptime(date + time[:6], '%Y%m%d%H%M%S')
    return None

def get_time(dcm, timezone):
    if hasattr(dcm, 'StudyDate') and hasattr(dcm, 'StudyTime'):
        study_date = dcm.StudyDate
        study_time = dcm.StudyTime
    elif hasattr(dcm, 'StudyDateTime'):
        study_date = dcm.StudyDateTime[0:8]
        study_time = dcm.StudyDateTime[8:]
    else:
        study_date = None
        study_time = None

    if hasattr(dcm, 'AcquisitionDate') and hasattr(dcm, 'AcquisitionTime'):
        acquitision_date = dcm.AcquisitionDate
        acquisition_time = dcm.AcquisitionTime
    elif hasattr(dcm, 'AcquisitionDateTime'):
        acquitision_date = dcm.AcquisitionDateTime[0:8]
        acquisition_time = dcm.AcquisitionDateTime[8:]
    else:
        acquitision_date = None
        acquisition_time = None

    session_timestamp = timestamp(dcm.StudyDate, dcm.StudyTime, timezone)
    acquisition_timestamp = timestamp(acquitision_date, acquisition_time, timezone)

    if session_timestamp:
        if session_timestamp.tzinfo is None:
            session_timestamp = pytz.timezone('UTC').localize(session_timestamp)
        session_timestamp = session_timestamp.isoformat()
    else:
        session_timestamp = ''
    if acquisition_timestamp:
        if acquisition_timestamp.tzinfo is None:
            acquisition_timestamp = pytz.timezone('UTC').localize(acquisition_timestamp)
        acquisition_timestamp = acquisition_timestamp.isoformat()
    else:
        acquisition_timestamp = ''
    return session_timestamp, acquisition_timestamp

def get_sex(sex_str):
    if sex_str == 'M':
        sex = 'male'
    elif sex_str == 'F':
        sex = 'female'
    else:
        sex = ''
    return sex

def dicom_classify(fp, outbase, timezone):
    """
    Extracts metadata from dicom zip and writes to .metadata.json.
    """
    if not os.path.exists(fp):
        print 'could not find %s' % fp
        print 'checking input directory ...'
        if os.path.exists(os.path.join('/input', fp)):
            fp = os.path.join('/input', fp)
            print 'found %s' % fp

    if not outbase:
        outbase = '/flywheel/v0/output'
        log.info('setting outbase to %s' % outbase)

    # List of the output files that will be written
    final_results = []

    # Extract the first file in the zip to /tmp/ and read it
    zip = zipfile.ZipFile(fp)
    for n in range(0, len(zip.namelist())):
        dcm_path = zip.extract(zip.namelist()[n], '/tmp')
        if os.path.isfile(dcm_path):
            try:
                dcm = dicom.read_file(dcm_path)
                break
            except:
                pass

    # Extract the header values
    header = {}
    exclude = ['[Unknown]', 'PixelData', 'Pixel Data',  '[User defined data]', '[Protocol Data Block (compressed)]', '[Histogram tables]', '[Unique image iden]']
    types = [int, float, str, list]
    for t in dcm.dir():
        if t not in exclude:
            value = dcm.get(t)
            if value:
                if type(value) not in types:
                    try:
                        value = float(value)
                    except:
                        value = str(value)
                if (type(value) == str and len(value) < 10240):
                    header[t] = value
                elif type(value) != str and type(value) in types:
                    header[t] = value
                else:
                    print 'Excluding ' + t

    # header = {}
    # exclude = ['[Unknown]', 'Pixel Data', '[User defined data]', '[Protocol Data Block (compressed)]', '[Histogram tables]', '[Unique image iden]']
    # types = [int, float, str, list, tuple]
    # for k in dcm.keys():
    #     if hasattr(dcm[k], 'name') and hasattr(dcm[k], 'value') and (dcm[k].name not in exclude):
    #         value = dcm[k].value
    #         if type(value) not in types:
    #             try:
    #                 value = float(value)
    #             except:
    #                 value = str(value)
    #         header[dcm[k].name.replace('[','').replace(']','')] = value
    #     else:
    #         pass
    log.info('done')

    # Write metadata file
    metadata = {}
    metadata['session'] = {}
    metadata['session']['operator'] = dcm.get('OperatorsName')
    metadata['session']['subject'] = {}
    metadata['session']['subject']['sex'] = get_sex(dcm.get('PatientSex'))
    metadata['session']['subject']['age'] = parse_patient_age(dcm.get('PatientAge'))
    metadata['session']['subject']['firstname'] = dcm.get('PatientName').given_name
    metadata['session']['subject']['lastname'] = dcm.get('PatientName').family_name
    session_timestamp, acquisition_timestamp = get_time(dcm, timezone);
    if session_timestamp:
        metadata['session']['timestamp'] = session_timestamp
    metadata['acquisition'] = {}
    metadata['acquisition']['instrument'] = dcm.get('Modality')
    metadata['acquisition']['label'] = dcm.get('SeriesDescription')
    metadata['acquisition']['measurement'] = measurement_from_label.infer_measurement(dcm.get('SeriesDescription'))
    metadata['acquisition']['metadata'] = {}
    metadata['acquisition']['metadata'] = header
    if acquisition_timestamp:
        metadata['acquisition']['timestamp'] = acquisition_timestamp

    # Write out the metadata to file (.metadata.json)
    metafile_outname = os.path.join(os.path.dirname(outbase),'.metadata.json')
    with open(metafile_outname, 'w') as metafile:
        json.dump(metadata, metafile)

    final_results.append(metafile_outname)

    return final_results

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('dcmzip', help='path to dicom zip')
    ap.add_argument('outbase', nargs='?', help='outfile name prefix')
    ap.add_argument('--log_level', help='logging level', default='info')
    ap.add_argument('-z', '--timezone', help='instrument timezone [system timezone]', default=None)
    args = ap.parse_args()

    log.setLevel(getattr(logging, args.log_level.upper()))
    logging.getLogger('sctran.data').setLevel(logging.INFO)
    log.info('job start: %s' % datetime.datetime.utcnow())

    results = dicom_classify(args.dcmzip, args.outbase, args.timezone)

    log.info('job stop: %s' % datetime.datetime.utcnow())
    log.info('generated %s' % ', '.join(results))
