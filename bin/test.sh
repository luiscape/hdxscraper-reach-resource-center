#!/bin/bash

#
# Running tests.
#
source venv/bin/activate
nosetests --no-byte-compile --with-coverage -d -v
