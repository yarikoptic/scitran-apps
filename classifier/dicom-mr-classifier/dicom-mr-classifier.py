#!/usr/bin/env python

import os
import json
import pytz
import tzlocal
import logging
import datetime
import scitran.data as scidata

logging.basicConfig()
log = logging.getLogger('dicom-mr-classifier')

def timestamp(date, time, timezone):
    if date and time:
        return datetime.datetime.strptime(date + time[:6], '%Y%m%d%H%M%S')
#        return localize_timestamp(datetime.datetime.strptime(date + time[:6], '%Y%m%d%H%M%S'), timezone)
    return None

def localize_timestamp(timestamp, timezone):
    return timezone.localize(timestamp)

def get_time(ds, timezone):
    session_timestamp = timestamp(ds.study_date, ds.study_time, timezone)
    acquisition_timestamp = timestamp(ds.acq_date, ds.acq_time, timezone)
    if session_timestamp:
        session_timestamp = session_timestamp.isoformat()
    else:
        session_timestamp = ''
    if acquisition_timestamp:
        acquisition_timestamp = acquisition_timestamp.isoformat()
    else:
        acquisition_timestamp = ''
    return session_timestamp, acquisition_timestamp

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
        outbase = '/flywheel/v0/output'   # take everything before dicom...
        log.info('setting outbase to %s' % outbase)

    log.info('reading metadata %s' % fp)

    # TODO: Replace this with calls to pydicom
    ds = scidata.parse(fp, filetype='dicom', ignore_json=True, load_data=False)

    session_timestamp, acquisition_timestamp = get_time(ds, timezone);

    log.info('done')

    final_results = []

    # Write metadata file
    metadata = {}

    metadata['session'] = {}
    metadata['session']['operator'] = ds.operator

    metadata['session']['subject'] = {}
    metadata['session']['subject']['sex'] = ds.subj_sex
    metadata['session']['subject']['age'] = ds.subj_age
    metadata['session']['subject']['firstname'] = ds.subj_firstname
    metadata['session']['subject']['lastname'] = ds.subj_lastname
    metadata['session']['subject']['firstname_hash'] = ds.firstname_hash  # unrecoverable, if anonymizing
    metadata['session']['subject']['lastname_hash'] = ds.lastname_hash  # unrecoverable, if anonymizing

    if session_timestamp:
        metadata['session']['timestamp'] = session_timestamp

    metadata['acquisition'] = {}
    metadata['acquisition']['instrument'] = ds.domain
    metadata['acquisition']['label'] = ds.series_desc
    metadata['acquisition']['measurement'] = ds.scan_type
    metadata['acquisition']['metadata'] = {}
    metadata['acquisition']['metadata'] = ds._hdr

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

    # Don't set the timezone for now
    set_timezone = False
    timezone = args.timezone
    if set_timezone and not timezone:
        timezone = tzlocal.get_localzone()

    results = dicom_classify(args.dcmzip, args.outbase, timezone)

    log.info('job stop: %s' % datetime.datetime.utcnow())

    log.info('generated %s' % ', '.join(results))

