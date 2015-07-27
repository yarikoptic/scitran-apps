#!/bin/bash -e

# Build app graph
( cd index.docker.io/ubuntu/   && hroot build )
( cd flywheel.io/ubuntu/       && hroot build )
( cd flywheel.io/dcm-convert/  && hroot build )
