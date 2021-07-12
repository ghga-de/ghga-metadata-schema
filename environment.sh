#!/bin/sh
python3 -m venv env
source env/bin/activate
export PYTHONPATH=.:$PYTHONPATH
