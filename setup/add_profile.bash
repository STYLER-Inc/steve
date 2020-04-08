#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0);pwd)
SCRIPT_NAME=`basename "$0"`

path_is_installed() {
    [[ -n "$(echo ${PATH} | grep 'profs/bin')" ]]
}

virtualenv -p `which python3` venv
${SCRIPT_DIR}/venv/bin/pip3 install -r ${SCRIPT_DIR}/requirements.txt

# Add to `$PATH` if not there already.
path_is_installed && exit 0
echo "export PATH="${SCRIPT_DIR}/bin:\$PATH"" >> ${HOME}/.profile
