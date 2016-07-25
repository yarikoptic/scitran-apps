#!/bin/bash
# Builds the brain-extraction container.
# The container can be exported using the export.sh script
GEAR=scitran/afq-demo
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build --no-cache --tag $GEAR $DIR
