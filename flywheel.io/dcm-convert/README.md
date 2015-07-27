# scitran/dcm2nii

### Build the Docker image
run the `build.sh` script, which creates the 'scitran/dcm2nii:latest' image.

### Run a container
The container is meant to be run by mounting two host volumes, one to the container `/input` directory, and one to the container `/output` directory. It is easiest to use on a file that is in your current working directory.

For example, you have a file in /some/path/to/dcms.tgz that you want converted to nifti.

    - option 1
    `cd /some/path/to/dcms.tgz`
    `docker run -v $(pwd):/input -v $(pwd):/output --rm scitran/dcm2nii:latest dcms.tgz`

    - option 2
    `docker run -v /some/path/to:/input -v /some/path/to/:/output --rm scitran/dcm2nii:latest dcms.tgz`


The container takes two optional positional arguments.  The first is the name of the input file, and the second is desired base for the output name.  The application container will append the appropriate file extension to the output base name.  If you do not specify a base for the output name, a

If the directory only contains one file to use as input, you do not need to specify the filename.  However, if there are multiple files in the directory, you must specify which file to use as the input.  Currently, there is no batch option to do every file in the input directory.

