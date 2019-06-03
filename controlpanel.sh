#!/bin/bash

installdir="/home/$USER/bin/hackerspace-scripts-2"
FILE="/home/$USER/.profile"
localdir="$(pwd)"

cd $installdir/PycharmProjects/hackerspace-scripts-2


echo -e "export PATH=\$PATH:$localdir/" >> $FILE
echo "log out then back in, successfuly made 'controlpanel.sh' a linked command!"

if [ ! -f $installdir/venv/bin/activate ]; then
    virtualenv -p python3 $installdir
fi

source $installdir/venv/bin/activate
python $installdir/controlpanel.py