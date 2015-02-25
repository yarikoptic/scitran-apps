# scitran/neuroimage_analysis Dockerfile

run the build.sh script to create the scitran/nipa_base:latest image.


Ubuntu image configured with neurodebian "non-free" apt repositories.

The dockerfile adds the neurodebian key, and adds neurodebian contrib non-free repository to apt sources, and finally installs several
image processing and analysis tools.

This image itself cannot be shipped.

Please ensure you have the approriate licenses to use the following tools.

    - octave \
    - afni \
    - fsl-core \
    - ants \
    - itksnap \
    - python-numpy \
    - python-scipy \
    - python-nipype \
    - python-nibabel \
    - python-dipy \
    - python-nitime \
    - python-nipy \
    - mrtrix \
    - mrtrix-doc \
    - mricron \
    - mriconvert \
    - gifti-bin \
    - dicomnifti \
    - nifti2dicom \
    - qnifti2dicom
