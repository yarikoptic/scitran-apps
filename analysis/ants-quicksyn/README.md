## scitran/ants-quicksyn

This dockerfile will create an ANTS (currently 2.1.0-2) docker image that
executes ANTs 'quick Syn' alignment


### Build the Image
To build the image, either download the files from this repo or clone the repo:
```
./build.sh
```

### Example Usage ###
To run ```ANTS quick syn``` from this image you can do the following:
```
docker run --rm -ti \
    -v </path/to/input/data>:/flyweel/v0/input/nifti \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/ants-quicksyn -o /flywheel/v0/output/fast /flywheel/v0/input/nifti/<t1_file.nii.gz>
```
* Note that the directory mounted at "/flywheel/v0/output" must be EMPTY for the algorithm to run.
* Note that if you put your input file in properly mounted directories, no inputs are required for the algorithm to run - as below


```
# If <t1_file.nii.gz> exists in </path/to/input/data>, then the following will work and produce a compressed output file </path/to/output>:
docker run --rm -ti \
    -v </path/to/input/data>:/flyweel/v0/input/nifti \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/ants-quicksyn
```

