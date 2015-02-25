#/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# TODO, tag with git revision
docker build --tag scitran/nipa_base:latest $DIR
