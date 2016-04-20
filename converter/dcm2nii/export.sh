#!/bin/bash
# Exports the container in the cwd.
# The container can be exported once it's started with

version=0.0.1
outname=dcm2nii-$version.tar
container=dcm2nii
image=scitran/dcm2nii

# Check if input was passed in.
if [[ -n $1 ]]; then
    outname=$1
fi

docker run --name=$container --entrypoint=/bin/true $image
docker export -o $outname $container
docker rm $container

