#!/bin/bash
# Builds the fsl-bet container.
# The container can be exported using the export.sh script

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build --no-cache --tag scitran/fsl-bet $DIR
