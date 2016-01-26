#!/bin/bash
# Build container within this context
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build --no-cache --tag scitran/qa-report-fmri $DIR

