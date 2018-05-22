#!/bin/sh

cp _sender.py sender.pyx
cp _receiver.py receiver.pyx
python setup.py build_ext --inplace
