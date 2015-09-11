#!/bin/bash

#
# Setting up the virtual environment.
#
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
