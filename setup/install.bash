#!/bin/bash
rm -rf ${HOME}/.sprofs
mkdir ${HOME}/.sprofs

cp -r src ${HOME}/.sprofs
cp -r bin ${HOME}/.sprofs
cp -r setup ${HOME}/.sprofs
cp requirements.txt ${HOME}/.sprofs

cd ${HOME}/.sprofs
mv setup/add_profile.bash .
./add_profile.bash

rm -rf ${HOME}/.sprofs/setup
