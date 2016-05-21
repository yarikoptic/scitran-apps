#!/bin/bash
#
# To recreate this executable you mush have matlab installed and on your path.
# Before running fully comment out your startup.m file to avoid path collision.
#
# Example usage:
#   compile_rtMask.sh /usr/local/bin/matlab /tmp/compile_rtMask
#

# Path to system matlab binary
MATLABBIN=$1

# Build directory
BUILDDIR=$2

if [[ ! -d $BUILDDIR ]]; then
    mkdir $BUILDDIR
fi

# Download the templates
wget -O $BUILDDIR/templates.zip https://storage.googleapis.com/flywheel/containers/assets/cmrr-rtmask-templates-v0.0.0.zip
cd $BUILDDIR && unzip -q templates.zip 

# Compile
$MATLABBIN -r "mcc -I $BUILDDIR/spm8/ -I $BUILDDIR/rtMask/matlab -I $BUILDDIR/rtMask/mask -m $BUILDDIR/rtMask/matlab/rtMask.m; exit"

