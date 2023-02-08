#!/bin/bash

rm -r dist
python setup.py sdist
yes | pip uninstall lift
pip install dist/lift*.gz
