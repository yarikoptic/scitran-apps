## scitran/dcm2niix

This dockerfile will create a docker image that can execute ```dcm2niix```.

## Options
Options are set in `dcm2nii.ini`. Current defaults are set and copied into the container on build.

### Build the Image
To build the image, either download the files from this repo or clone the repo:
```
./build.sh
```

### Example Usage ###
To run dcm2niix from this image you can do the following:
```
docker run --rm -ti \
    -v </path/to/input/data>:/flywheel/v0/input/dicom \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/dcm2niix <optional_flags>
```




