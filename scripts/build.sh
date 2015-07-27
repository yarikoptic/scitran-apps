#!/bin/bash -e

# Build app graph
( cd index.docker.io/ubuntu/   && hroot build )
( cd scitran.io/ubuntu/        && hroot build )
( cd scitran.io/dcm-convert/   && hroot build )
