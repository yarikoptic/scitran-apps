#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# TODO: tag with git revision
docker build --no-cache --tag scitran-apps-dcmconvert:0 $DIR
