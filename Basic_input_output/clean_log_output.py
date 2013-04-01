#! /usr/bin/env python

import sys
import traceback
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Rename_me
import PmagPy_tests as PT
import subprocess


def clean_output_file():
    the_file = open('all_output.txt', 'rU')
    info = the_file.readlines()
    rhino = False
    new_file = open('clean_output_log.txt', 'w')
    for l in info:
        if "rhino" in l:
            rhino = True
        if rhino:
            new_file.write(l)
    print " 'clean_output_log.txt' ready"

if __name__ == "__main__":
    clean_output_file()
