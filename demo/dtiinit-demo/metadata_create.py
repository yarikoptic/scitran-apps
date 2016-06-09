#!/usr/bin/env python

import os
import json
import datetime

def meta_create(outbase):
    """
    Create metadata file based on output files
    """

    if not os.path.isdir(outbase):
            outbase = '/flywheel/v0/output'

    with open('/flywheel/v0/types.json') as data_file:
            data_types = json.load(data_file)

    # Write metadata file
    output_files = os.listdir(outbase)
    files = []
    if len(output_files) > 0:
        for f in output_files:
            fdict = {}
            fdict['name'] = f

            # Check file extension against every data_type to determine
            # The correct type
            ftype = ''
            for d in data_types:
                extensions = list(data_types[d])
                if any([f.endswith(ext) for ext in extensions]):
                    ftype = d
            if not ftype:
                ftype = 'None'

            fdict['type'] = ftype
            files.append(fdict)

        metadata = {}
        metadata['acquisition'] = {}
        metadata['acquisition']['files'] = files

        with open(os.path.join(outbase, '.metadata.json'), 'w') as metafile:
            json.dump(metadata, metafile)

    return os.path.join(outbase,'.metadata.json')

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('outbase', help='outfile name prefix')
    args = ap.parse_args()

    gearname = 'dtiinit-demo'

    metafile = meta_create(args.outbase)

    if os.path.isfile(metafile):
        print '[scitran/' + gearname + ']  generated %s' % metafile
    else:
        print '[scitran/' + gearname + ']  Failed to create metadata.json'

