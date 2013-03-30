#! /usr/bin/env python                                                                                                                
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Rename_me
import PmagPy_tests as PT
import Bootstrap_plotting
#import Extra_output
import random_stuff

#if __name__ == '__main__':
if 1 == 0:
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


def multiply(n=0, n2=3.):
    if n == 0:
        raise ValueError("0 can't be used")
    else:
        print n * n2
        return n * n2

def divide(n=3., n2=2.):
    if n2 == 0:
        raise ValueError("0 can't be used")
    else:
        print n / n2
        return n / n2

def lower_case(string="e"):
    if len(string) == 1:
        raise NameError("give me more!!")
    else:
        print string.lower()
        return string.lower()


functions = [multiply, divide, lower_case]
for i in functions:
    try:
        i()
    except Exception as ex:
        print i, ex
#        print "AWESOMENESS!!!!"


#print functions[1]
#functions[1]()
#multiply(8, 3)
#divide(1, 5)
#lower_case("HELLO")
