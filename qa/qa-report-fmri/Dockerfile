# vistalab/qa_report_fmri
#
# Use modified CNI/NIMS code from @rfdougherty to create a qa_report for a given fmri NIfTI file in Flywheel spec.
# See https://github.com/cni/nims/blob/master/nimsproc/qa_report.py for original source code.
#
# Example usage:
#   docker run --rm -ti \
#        -v /path/nifti_file:/flywheel/v0/input \
#        -v /path/for/output/files:/flywheel/v0/output
#        vistalab/qa_report_fmri /flywheel/v0/input -i nifti_file.nii.gz
#

FROM ubuntu-debootstrap:trusty

MAINTAINER Michael Perry <lmperry@stanford.edu>

# Install dependencies
RUN apt-get update && apt-get -y install python-dev \
   git \
   libjpeg-dev \
   zlib1g-dev \
   pkg-config \
   libpng12-dev \
   libfreetype6-dev

# Link libs: pillow jpegi and zlib support hack
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# Install scitran.data dependencies
RUN apt-get -y install \
    python-numpy \
    python-pip \
    python-scipy \
    python-dipy \
    python-nipy \
    python-nibabel \
    zip \
    unzip

RUN  pip install dipy --upgrade \
    && pip install nipy --upgrade \
    && pip install matplotlib --upgrade

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run
COPY info.toml ${FLYWHEEL}/info.toml

# Put the python code in place
COPY qa_report_sa.py ${FLYWHEEL}/qa_report.py

ENTRYPOINT ["/flywheel/v0/run"]

