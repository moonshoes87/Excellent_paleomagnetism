#! /usr/bin/env python

import sys
import traceback
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Rename_me
import PmagPy_tests as PT
import subprocess

def clean_output_file(infile, outfile):
    a_file = open(infile, 'rU')
    info = a_file.readlines()
    rhino = False
    new_file = open(outfile, 'w')
    for l in info:
        if "rhino" in l:
            rhino = True
        if rhino:
            new_file.write(l)
    print str(outfile) + " is  ready"


if __name__ == "__main__": # so it can be done interactively on the command line, but doesn't have to be.  
# the issue is that you have to run it as a separate call then the initial log creating
    file_in = raw_input("what file do you want to clean?  ")
    file_out = raw_input("what do you want to call the cleaned file?  ")
    clean_output_file(file_in, file_out)
