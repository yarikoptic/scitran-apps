## scitran/brain-extraction

This dockerfile will create a FSL (v5.0) docker image that executes bet2


### Build the Image
To build the image, either download the files from this repo or clone the repo:
```
./build.sh
```

### Example Usage ###
To run ```bet2``` from this image you can do the following:
```
docker run --rm -ti \
    -v </path/to/input/data>:/flyweel/v0/input \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/brain-extraction /flywheel/v0/input/<t1_file.nii.gz> /flywheel/v0/output/bet2_
```
* Note that the directory mounted at "/flywheel/v0/output" must be EMPTY for the algorithm to run.
* Note that if you put your input file in properly mounted directories, no inputs are required for the algorithm to run - as below


```
# If <t1_file.nii.gz> exists in </path/to/input/data>, then the following will work and produce a brain extracted file in </path/to/output>:
docker run --rm -ti \
    -v </path/to/input/data>:/flyweel/v0/input \
    -v </path/to/output>:/flywheel/v0/output \
    scitran/brain-extraction
```

