# Create a base docker container that will run fsl's fast
#
# Example usage:
#    docker run --rm -ti \
#       -v </path/to/input/data>:/flyweel/v0/input/nifti \
#       -v </path/to/output>:/flywheel/v0/output \
#       scitran/fsl-fast /flywheel/v0/input/<t1_file.nii.gz>

# Install FSL
FROM neurodebian:trusty

MAINTAINER Michael Perry <lmperry@stanford.edu>

# Run apt-get calls
COPY sources /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-get update \
    && apt-get install -y \
        fsl-5.0-core \
        zip

# Configure environment (Must also be done in the run script)
ENV FSLDIR=/usr/lib/fsl/5.0
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV PATH=$PATH:$FSLDIR
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FSLDIR
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run

COPY manifest.json ${FLYWHEEL}/manifest.json

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

