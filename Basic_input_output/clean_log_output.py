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
        if "rhino" in l:  # 'rhino' is the marker for the relevant output
            rhino = True
        if rhino:
            new_file.write(l)
    print str(outfile) + " is  ready"

# Extra output:
# infile = extra_out_full_output.txt
# outfile = extra_out_clean_output.txt
# also (separately) created is: extra_out_errors_list.txt.  this one just has the short stuff

#Rename_me:
     # input: rename_me_full_output.txt                                                                    
     # output: rename_me_clean_output.txt  


def clean_all_output_logs():
    pass
# make a command (here or somewhere else) that just goes through all the output files and cleans them up.  


if __name__ == "__main__": # so it can be done interactively on the command line, but doesn't have to be.  
# the issue is that you have to run it as a separate call then the initial log creating
    file_in = raw_input("what file do you want to clean?  ")
    file_out = raw_input("what do you want to call the cleaned file?  ")
    clean_output_file(file_in, file_out)
