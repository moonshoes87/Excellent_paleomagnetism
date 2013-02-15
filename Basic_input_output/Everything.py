#! /usr/bin/env python                                                                                                                
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Basic_input_output
import PmagPy_tests
import Uncategorized_programs
import Plotting
import Extra_output

if __name__ == '__main__':
    Basic_input_output.complete_working_test()
    print "Finished BIO"
    Uncategorized_programs.complete_working_test()
    print "Finished uncategorized programs"
    Plotting.complete_working_test()
    print "Finished plotting"
    Extra_output.complete_working_test()
    print "Done with everything"
