# Create a base docker container that will run fsl's fast
#
# Example usage:
#    docker run --rm -ti \
#       -v </path/to/input/data>:/flyweel/v0/input/nifti \
#       -v </path/to/output>:/flywheel/v0/output \
#       scitran/ants-quicksyn /flywheel/v0/input/<t1_file.nii.gz>

# Install ANTs
FROM neurodebian:trusty

MAINTAINER Yaroslav Halchenko <debian@onerussian.com>

# Run apt-get calls
COPY sources /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-get update \
    && apt-get install -y \
        ants

# Configure environment (Must also be done in the run script)
ENV PATH=$PATH:/usr/lib/ants
RUN echo 'export PATH=$PATH:/usr/lib/ants' >> /root/.bashrc

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run ${FLYWHEEL}/run

COPY manifest.json ${FLYWHEEL}/manifest.json
COPY metadata_create.py ${FLYWHEEL}/metadata_create.py
RUN chmod +x ${FLYWHEEL}/metadata_create.py

# Add types from scitran
WORKDIR ${FLYWHEEL}
ADD https://raw.githubusercontent.com/scitran/utilities/master/file_types.json ./types.json

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

