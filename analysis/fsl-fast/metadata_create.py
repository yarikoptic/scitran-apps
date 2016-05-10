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

    # Write metadata file
    output_files = os.listdir(outbase)
    files = []
    if len(output_files) > 0:
        for f in output_files:

            fdict = {}
            fdict['name'] = f

            if f.endswith('.nii.gz'):
                ftype = 'nifti'

            elif f.endswith('bvec'):
                ftype = 'bvec'

            elif f.endswith('bval'):
                ftype = 'bval'

            elif f.endswith('montage.zip'):
                ftype = 'montage'

            elif f.endswith('.png'):
                ftype = 'screenshot'

            else:
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

    metafile = meta_create(args.outbase)

    if os.path.isfile(metafile):
        print '[scitran/fsl-fast]  generated %s' % metafile
    else:
        print '[scitran/fsl-fast]  Failed to create metadata.json'
