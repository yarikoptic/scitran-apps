## scitran/dcm2nii

This dockerfile will create a MRICRON docker image that can execute ```dcm2nii```.

## Options
Options are set in `dcm2nii.ini`. Current defaults are set and copied into the container on build.

Optional flags can be passed to the container and will override config in `dcm2nii.ini`.

### Build the Image
To build the image, either download the files from this repo or clone the repo:
```
./build.sh
```

### Example Usage ###
To run dcm2nii from this image you can do the following:
```
docker run --rm -ti \
    -v </path/to/input/data>:/flywheel/v0/input \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/dcm2nii <optional_flags>
```




