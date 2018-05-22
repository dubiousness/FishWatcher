#!/bin/sh

cp sender.py sender.pyx
python setup.py build_ext --inplace
