#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0);pwd)
SCRIPT_NAME=`basename "$0"`

virtualenv -p `which python3` venv
${SCRIPT_DIR}/venv/bin/pip3 install -r ${SCRIPT_DIR}/requirements.txt

# Add to `$PATH` if not there already.
if grep -q $HOME/.profs/bin $HOME/.profile ; then 
	exit(0)
fi
echo "export PATH="${SCRIPT_DIR}/bin:\$PATH"" >> ${HOME}/.profile
