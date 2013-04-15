#! /usr/bin/env python                                                                                                                
import sys
import traceback
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import PmagPy_tests as PT


file_prefix = PT.file_prefix
directory =  PT.directory

print "STARTING HERE"

def old_go_through(programs_list, errors_log): # args are: the list of programs to check, and the file to write errors to
    errors_log.write(str(errors_log)[12:-28] + ':  ' + '\n')  
    PT.clean_house()
    redo_me = [] # will be a list of the functions to be redone
    errors_count = 0
    messed_up_programs = [] # will be a list doc strings of the programs that have problems
    for i in programs_list:
        try:
            print "TRYING"
            print " - "
            i()
        except Exception as ex:
            redo_me.append(i)
            errors_count += 1
            messed_up_programs.append(i.__doc__)
            print str(i.__doc__) + " failed"
            print "i, ex: ", i, ex
            print "type(ex)", type(ex)
            print "ex.args", ex.args
            x = str(ex)
            errors_log.write(str(i.__doc__))
            errors_log.write(": " + x + ".  ")
            errors_log.write('\n')
            stuff = sys.exc_info()
            print 0, stuff[0]
            print 1, stuff[1]
            print 2, stuff[2] # this is the traceback object, which I will print below
            errors_log.write("Traceback below: " + "\n")
            traceback.print_tb(stuff[2], None, errors_log)
            errors_log.write('\n')
#            print "tb", tb
 #           errors_log.write(str(tb))
#            traceback.print_stack(ex)
#            print "stack stuff"  # traceback.print_stack() # exc_type, exc_value, exc_traceback = sys.exc_info()   # print "*** print_tb:"   #  traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)  #       print "end stack stuff"
    print "messed up programs", messed_up_programs
    print "total errors found: " + str(errors_count)
    message = []
    for i in messed_up_programs:
        message.append(i)
    print "THESE ONES ARE BROKEN ", message
    print "redo me list", redo_me
    errors_log.write("programs with errors: " + str(messed_up_programs) + "\n") # added this in, see if it works well
    errors_log.write('\n')
    return redo_me


def go_through(programs_list, errors_log): # args are: a dictionary of program names and the functions that test them, and the file to write errors to
    errors_log.write(str(errors_log)[12:-28] + ':  ' + '\n')  
    PT.clean_house()
    redo_me = [] # will be a list of the functions to be redone
    errors_count = 0
    messed_up_programs = [] # will be a list doc strings of the programs that have problems
    for k, v in programs_list.items():
        try:
            print "TRYING"
            print " - "
            v()
        except Exception as ex:
            redo_me.append(v)
            errors_count += 1
            messed_up_programs.append(v.__doc__)
            print str(v.__doc__) + " failed"
            print "program, ex: ", k, ex
            print "type(ex)", type(ex)
            print "ex.args", ex.args
            x = str(ex)
            errors_log.write(str(v.__doc__))
            errors_log.write(": " + x + ".  ")
            errors_log.write('\n')
            stuff = sys.exc_info()
            print 0, stuff[0]
            print 1, stuff[1]
            print 2, stuff[2] # this is the traceback object, which I will print below
            errors_log.write("Traceback below: " + "\n")
            traceback.print_tb(stuff[2], None, errors_log)
            errors_log.write('\n')
#            print "tb", tb
 #           errors_log.write(str(tb))
#            traceback.print_stack(ex)
#            print "stack stuff"  # traceback.print_stack() # exc_type, exc_value, exc_traceback = sys.exc_info()   # print "*** print_tb:"   #  traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)  #       print "end stack stuff"
    print "messed up programs", messed_up_programs
    print "total errors found: " + str(errors_count)
    message = []
    for i in messed_up_programs:
        message.append(i)
    print "THESE ONES ARE BROKEN ", message
    print "redo me list", redo_me
    errors_log.write("programs with errors: " + str(messed_up_programs) + "\n") # added this in, see if it works well
    errors_log.write('\n')
    return redo_me

def redo_broken_ones(redo_list):
    print "rhino"
    for i in redo_list:
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


