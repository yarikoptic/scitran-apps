# scitran/dcm2nii

### Build the Docker image
Build the image, from within the dcm2nii directory

    `docker build --tag scitran/dcm2nii:latest .`

### Run a container
This container is meant to be run by mounting two host volumes, one to the container `/input` directory, and one to the container `/output` directory. It is easiest to use on a file that is in your current working directory.

For example, you have a file in /some/path/to/dcms.tgz that you want converted to nifti.

    - option 1
    `cd /some/path/to/dcms.tgz`
    `docker run -v $(pwd):/input -v $(pwd):/output --rm scitran/dcm2nii:latest dcms.tgz`

    - option 2
    `docker run -v /some/path/to/input.tgz:/input -v /some/path/to/output_dir:/output --rm scitran/dcm2nii:latest dcms.tgz`
