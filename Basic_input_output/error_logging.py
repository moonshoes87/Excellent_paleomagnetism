#! /usr/bin/env python                                                                                                                
import sys
import traceback
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
#import Rename_me
import PmagPy_tests as PT
#import clean_log_output


file_prefix = PT.file_prefix
directory =  PT.directory


print "STARTING HERE"

# relocate the functions below, maybe to PmagPy_tests.py.  Otherwise, to a program that is devoted to just checking output

def go_through(a_list, errors_log): # args are: the list of programs to check, and the file to write errors to
    PT.clean_house()
    redo_me = [] # will be a list of the functions to be redone
    errors_count = 0
    messed_up_programs = [] # will be a list doc strings of the programs that have pr
    for i in a_list:
        try:
            print "TRYING"
            print " - "
            i()
#        except IOError:
# will catch just the file missing type errors
 #           print "IOERROR UNICORN"
        except Exception as ex:
            redo_me.append(i)
            errors_count += 1
            messed_up_programs.append(i.__doc__)
            print str(i) + " failed donut"
            print "i, ex: ", i, ex
            print "type(ex)", type(ex)
            print "ex.args", ex.args
            x = str(ex)
#            problems_dictionary[i.__doc__] = x
            errors_log.write(i.__doc__)
            errors_log.write(": " + x + ".  ")
#            print "stack stuff"
 #           traceback.print_stack()
  #          exc_type, exc_value, exc_traceback = sys.exc_info()
   #         print "*** print_tb:"
    #        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
     #       print "end stack stuff"
    print "messed up programs", messed_up_programs
    print "total errors found: " + str(errors_count)
    message = []
    for i in messed_up_programs:
        message.append(i)
    print "THESE ONES ARE BROKEN ", message
#    print "problems dictionary", problems_dictionary
    print "redo me list", redo_me
    return redo_me

def redo_broken_ones(a_list):
    print "rhino"
    for i in a_list:
        print i.__doc__
        try:
            i()
        except Exception as ex:
            print str(i.__doc__) + " raised error: " + str(ex)
            print "-----------"
            print "-----------"
            #raise ex



    
if __name__ == "__main__":
    pass
#    new_list = go_through(Extra_output_tests, ex_out_errors_log)
 #   redo_broken_ones(new_list)


