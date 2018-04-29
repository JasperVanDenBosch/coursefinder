#!/usr/bin/env bash
python3 --version
pip3 install virtualenv # system-wide virtualenv for python3
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
python3 setup.py develop
