#! /usr/bin/env python

import sys
import unittest
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')

# all this one can actually do is test that it is possible to enter interactive mode.  unless I rewrite the interactive mode
def test_angle_interactive():
    obj = env.run('angle.py', '-i', stdin='3')
    print("stdout: ",obj.stdout)
    expected_out = u'Declination 1: [ctrl-D  to quit] Inclination 1: \nGood bye\n\n'
    print("expected out: ", expected_out)
    if obj.stdout == expected_out:
        print "Interactive mode successfully instantiated"
    else:
        raise(NameError, "There was a problem entering interactive mode")

def test_angle_file(file_in = 0, file_out = 0, file_correct = 0):
    obj = env.run('angle.py', '-f', '/Users/nebula/Python/angle.dat', '-F', '/Users/nebula/Python/new_angle_results.txt')
    print obj.stdout
    output = obj.stdout
    print output
    print ("files created:", obj.files_created)
    print ("files updated: ", obj.files_updated)
    print ("error", obj.stderr)
    print ("file out", file_out)
    new_file_out = parse_file(file_out)
    new_file_correct = parse_file(file_correct)
    print ("(parsed) new_file_out", new_file_out)
    for z, thing in enumerate(new_file_out):
        print (thing, " should equal ", new_file_correct[z])
        if thing == new_file_correct[z]:
            print "You rock"
        else:
            raise(NameError, "Expected output does not match actual output")
    print "Test_angle_file successful"
      
def clean_file(the_file):
    for l in the_file:
        clean_file = []
        new_line = l.strip('\n')
        clean_file.append(new_line)
        return clean_file
    
def read_file(the_file):
    read_file = open(the_file).readlines()
    return read_file

def parse_file(the_file):
    thing = open(the_file).readlines()
    clean_file = []
    for l in thing:
        new_line = l.strip('\n')
        clean_file.append(new_line)
    return clean_file

def test_angle_help():
    obj = env.run('angle.py', '-h')
    message = str(obj.stdout)
    print ("standard output is: ", type(message))
    print("output help message: ", message)
    print("proper help message: ", angle_help_message)
    if len(message) > 50:
        print "Help message successfully called"
    else:
        raise(NameError, "Help message failed...")
    if message == angle_help_message:
        print "AWESOME help message"
    else:
        raise(NameError, "Help message failed...")

angle_help_message = """
    NAME
        angle.py
    
    DESCRIPTION
      calculates angle between two input directions D1,D2
    
    INPUT (COMMAND LINE ENTRY) 
           D1_dec D1_inc D1_dec D2_inc
    OUTPUT
           angle
    
    SYNTAX
        angle.py [-h][-i] [command line options] [< filename]
    
    OPTIONS
        -h prints help and quits 
        -i for interactive data entry
        -f FILE input filename
        -F FILE output filename (required if -F set)
        Standard I/O 
    
"""

class Bad_angle(unittest.TestCase):
    def test_something(self):
        self.assertRaises(NameError, test_angle_file, angle_file_in, angle_file_out, angle_file_incorrect)

#    def test_dipole_pinc_file(self):
 #       self.assertRaises(NameError, badtest_pinc.real_file_test)


def do_unittest():
    unittest.main(module='test_angle')


# the various test files for testing
# this one is the input
angle_file_in = '/Users/nebula/Python/angle.dat'
# this one is where the output is written
angle_file_out = '/Users/nebula/Python/new_angle_results.txt'
# this is a reference file with the correct output
angle_file_correct = '/Users/nebula/Python/correct_angle_results.txt'
# this one is a reference file with incorrect output
angle_file_incorrect = '/Users/nebula/Python/incorrect_angle_results.txt'

test_angle_interactive()
test_angle_file(angle_file_in, angle_file_out, angle_file_correct)
test_angle_help()
do_unittest()

if __name__ == "__main__":
    unittest.main()


