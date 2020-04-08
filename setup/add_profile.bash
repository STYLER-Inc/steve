#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0);pwd)
SCRIPT_NAME=`basename "$0"`
BASE_DIR=${SCRIPT_DIR}/..

virtualenv -p `which python3` venv
${BASE_DIR}/venv/bin/pip3 install -r ${BASE_DIR}/requirements.txt
echo "export PATH="${BASE_DIR}/bin:\$PATH"" >> ${HOME}/.profile
