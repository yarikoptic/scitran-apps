# Create a base docker container that will run bet2
#
# Example usage:
#   docker run --rm -ti \
#       scitran/fsl-bet <input_fileroot> <output_fileroot> [options]
#


# Install FSL
FROM neurodebian:trusty

# Run apt-get calls
COPY sources /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-get update \
    && apt-get install -y fsl-5.0-core

# Configure environment (Must also be done it the RUN script)
ENV FSLDIR=/usr/lib/fsl/5.0
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV PATH=$PATH:$FSLDIR
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FSLDIR
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc

MAINTAINER Michael Perry <lmperry@stanford.edu>

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run

COPY manifest.json ${FLYWHEEL}/manifest.json
COPY metadata_create.py ${FLYWHEEL}/metadata_create.py
RUN chmod +x ${FLYWHEEL}/metadata_create.py

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

