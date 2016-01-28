#!/usr/bin/env python

import os
import json
import logging
import datetime
logging.basicConfig()
log = logging.getLogger('dicom-mr-classifier')
import scitran.data as scidata


def dicom_convert(fp, outbase=None):
    """
    Attempts multiple types of conversion on dicom files.

    Attempts to create a nifti for all files, except screen shots.
    Also attesmpt to create tiff montages of all files.

    tiff creation requires imagemagick.

    """
    if not os.path.exists(fp):
        print 'could not find %s' % fp
        print 'checking input directory ...'
        if os.path.exists(os.path.join('/input', fp)):
            fp = os.path.join('/input', fp)
            print 'found %s' % fp

    if not outbase:
        fn = os.path.basename(fp)
        outbase = os.path.join('/output', fn[:fn.index('_dicom')])   # take everything before dicom...
        log.info('setting outbase to %s' % outbase)

    log.info('reading metadata %s' % fp)
    ds = scidata.parse(fp, filetype='dicom', ignore_json=True, load_data=False)
    log.info('done')

    final_results = []

    # Write metadata file
    metadata = {}

    metadata['session'] = {}
    metadata['session']['operator'] = ds.operator

    metadata['session']['subject'] = {}
    metadata['session']['subject']['sex'] = ds.subj_sex
    metadata['session']['subject']['age'] = ds.subj_age
    metadata['session']['subject']['code'] = ds.subj_code
    metadata['session']['subject']['firstname'] = ds.subj_firstname
    metadata['session']['subject']['lastname'] = ds.subj_lastname
    metadata['session']['subject']['firstname_hash'] = ds.firstname_hash  # unrecoverable, if anonymizing
    metadata['session']['subject']['lastname_hash'] = ds.lastname_hash  # unrecoverable, if anonymizing

    metadata['acquisition'] = {}
    metadata['acquisition']['instrument'] = ds.domain
    metadata['acquisition']['label'] = ds.series_desc
    metadata['acquisition']['measurement'] = ds.scan_type
    metadata['acquisition']['metadata'] = {}
    metadata['acquisition']['metadata'] = ds._hdr

    metafile_outname = os.path.join(os.path.dirname(outbase),'.metadata.json')
    with open(metafile_outname, 'w') as metafile:
        json.dump(metadata, metafile)

    final_results.append(metafile_outname)

    return final_results

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('dcmtgz', help='path to dicom zip')
    ap.add_argument('outbase', nargs='?', help='outfile name prefix')
    ap.add_argument('--log_level', help='logging level', default='info')
    args = ap.parse_args()

    log.setLevel(getattr(logging, args.log_level.upper()))
    logging.getLogger('sctran.data').setLevel(logging.INFO)

    log.info('job start: %s' % datetime.datetime.utcnow())
    results = dicom_convert(args.dcmtgz, args.outbase)
    log.info('job stop: %s' % datetime.datetime.utcnow())

    log.info('generated %s' % ', '.join(results))

