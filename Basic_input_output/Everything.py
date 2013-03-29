#! /usr/bin/env python                                                                                                                
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Rename_me.py
import PmagPy_tests as PT
import Bootstrap_plotting
import Extra_output
import random_stuff

if __name__ == '__main__':
    Rename_me.complete_working_test()
    print "Finished Rename_me"
    Bootstrap_plotting.complete_working_test()
    print "Finished Bootstrap plotting"
    Extra_output.complete_working_test()
    print "Finished extra output"
    random_stuff.complete_working_test()
    print "Done with everything"
    PT.clean_house()
    PT.remove_new_outfiles()
