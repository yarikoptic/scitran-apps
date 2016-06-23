#!/bin/bash
# Builds the brain-extraction container.
# The container can be exported using the export.sh script
GEAR=cortex-demo
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build --no-cache --tag scitran/$GEAR $DIR
