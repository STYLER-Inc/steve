#!/bin/bash
rm -rf ${HOME}/.profs
mkdir ${HOME}/.profs

cp -r src ${HOME}/.profs
cp -r bin ${HOME}/.profs
cp -r setup ${HOME}/.profs
cp requirements.txt ${HOME}/.profs

cd ${HOME}/.profs
mv setup/add_profile.bash .
./add_profile.bash

rm -rf ${HOME}/.profs/setup
