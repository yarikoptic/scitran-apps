# scitran/cmrr-rtmask
#
# This docker file will configure an environment into which the Matlab compiler
# runtime will be installed and in which stand-alone matlab routines (such as
# those created with Matlab's deploytool) can be executed. Here we execute rtmask.
#
# See http://www.mathworks.com/products/compiler/mcr/ for more info.
#
# EXAMPLE USAGE:
#     wget https://storage.googleapis.com/flywheel/containers/assets/cmrr-rtmask-example-data-v0.0.0.zip && \
#           unzip cmrr-rtmask-example-data-v0.0.0.zip && \
#           cd cmrr-rtmask-example-data-v0.0.0
#     docker run -ti --rm -v `pwd`/input:/flywheel/v0/input -v `pwd`/output:/flywheel/v0/output scitran/cmrr-rtmask
#

# All the heavy lifiting is done from vistalab/mcr-v82
# The ENV from that image is duplicated in mcr-env, which is sourced from 'run'.
FROM vistalab/mcr-v82
MAINTAINER Michael Perry <lmperry@stanford.edu>

# Install deps
RUN apt-get update \
    && apt-get install -y \
    zip \
    gzip \
    python

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}

# Run script and metadata code
COPY run ${FLYWHEEL}/run
RUN chmod +x ${FLYWHEEL}/run
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY metadata_create.py ${FLYWHEEL}/metadata_create.py
RUN chmod +x ${FLYWHEEL}/metadata_create.py

# Add templates from google storage (this could be places here, if need be).
WORKDIR /opt/
ADD https://storage.googleapis.com/flywheel/containers/assets/cmrr-rtmask-templates-v0.0.0.zip ./templates.zip
RUN unzip -q templates.zip && rm templates.zip

# Add MCR executable
WORKDIR ${FLYWHEEL}
COPY mcr_env ./mcr_env
COPY rtMask_v0.0.0 ${FLYWHEEL}/rtMask
RUN chmod +x ${FLYWHEEL}/rtMask

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]

