#!/bin/bash
# Build container within this context

CONTAINER=scitran/fsl-bet

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build --no-cache --tag $CONTAINER $DIR

