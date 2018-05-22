#!/bin/sh

cp sender.py sender.pyx
cp receiver.py receiver.pyx
python setup.py build_ext --inplace
