# scitran/dicom-mr-classifier
#
# Use pyDicom to classify raw DICOM data (zip) from Siemens, GE or Philips.
#
# Example usage:
#   docker run --rm -ti \
#        -v /path/to/dicom/data:/data \
#        scitran/dicom-mr-classifier \
#        /data/input.zip \
#        /data/outprefix
#

FROM ubuntu-debootstrap:trusty

MAINTAINER Michael Perry <lmperry@stanford.edu>

# Install dependencies
RUN apt-get update && apt-get -y install python-dev \
   python-virtualenv \
   git \
   libjpeg-dev \
   zlib1g-dev


# Install scitran.data dependencies
RUN pip install \
    pytz \
    pydicom \
    tzlocal

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run
COPY manifest.json ${FLYWHEEL}/manifest.json

# Put the python code in place
ADD https://raw.githubusercontent.com/scitran/utilities/master/measurement_from_label.py ${FLYWHEEL}/measurement_from_label.py
COPY dicom-mr-classifier.py ${FLYWHEEL}/dicom-mr-classifier.py

# Set the entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

