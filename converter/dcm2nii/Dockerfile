# Creates docker container that runs dcm2nii
#
# Example usage:
#   docker run --rm -ti \
#       -v <someDirWithDicoms>:/flywheel/v0/input \
#       -v <emptyOutputFolder>:/flywheel/v0/output \
#       scitran/dcm2nii <optional_flags>
#
#

# Start with neurodebian image
FROM neurodebian:trusty
MAINTAINER Michael Perry <lmperry@stanford.edu>

# Run apt-get calls
RUN apt-get update \
    && apt-get install -y \
    python \
    mricron \
    unzip \
    gzip

ENV DCM2NIIDIR /root/.dcm2nii
RUN mkdir -p $DCM2NIIDIR
COPY dcm2nii.ini $DCM2NIIDIR/dcm2nii.ini

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run
COPY metadata_create.py ${FLYWHEEL}/metadata_create.py
RUN chmod +x ${FLYWHEEL}/metadata_create.py
COPY info.toml ${FLYWHEEL}/info.toml

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

