#!/bin/bash
TOOL_NAME=steve
rm -rf ${HOME}/.${TOOL_NAME}
mkdir ${HOME}/.${TOOL_NAME}

cp -r src ${HOME}/.${TOOL_NAME}
cp -r bin ${HOME}/.${TOOL_NAME}
cp -r setup ${HOME}/.${TOOL_NAME}
cp requirements.txt ${HOME}/.${TOOL_NAME}

cd ${HOME}/.${TOOL_NAME}
mv setup/add_profile.bash .
./add_profile.bash

rm -rf ${HOME}/.${TOOL_NAME}/setup
