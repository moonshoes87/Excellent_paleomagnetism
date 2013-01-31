#! /usr/bin/env python
# to do:  simplify and comment this up.  Also, consider having a way to intentionally give bad input and expect exceptions to be raised.  
import sys
import unittest
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./test-output')
# second tuple should start with 3
input_output_list = [(70, 79.7),(3., 6.),(118, -75.1),(32, 51.3)] # pairs of known correct input and output

def test_dipole_pinc_interactive(in_out_list):
    for i in in_out_list:
        data_in = i[0]
        data_out = i[1]
        print("data_out: ", data_out)
        obj = env.run('dipole_pinc.py', '-i', stdin='%s' %(data_in))
        string = str(obj.stdout)
        array = string.split()
        print("ARRAY: ", array)
        value_found = 0
        print(array)
        for z in array:
            if str(z) == str(data_out):
                print "SUCCESS"
                value_found = 1
            else:
                pass
        if value_found == 0:
            raise NameError("Dipole_pinc.py: Expected output does not match actual output")
        value_found = 0
    print("Test successful")

def test_dipole_pinc_file(f):
    # file should have: 18, 22, 35, -90  & correct values should be 33.0, 38.9, 54.5, -90.0
    correct_values = (33.0,38.9,54.5,-90.0)
    the_file = open(f).readlines()
    clean_file = []
    for l in the_file:
        new_line = l.strip('\n')
        clean_file.append(new_line)
    print("clean file: ",clean_file)
    x = 0
    for line in clean_file:
        print("-")
        obj = env.run('dipole_pinc.py', '-i', stdin=line)
        print("stdout was: ", obj.stdout)
        print("cleaned input was: ", line)
        print("output should have been", correct_values[x])
        string = str(obj.stdout)
        array = string.split()
        value_found = 0
        for q in array:
            if str(q) == str(correct_values[x]):
                value_found = 1
                print("for loop has found the correct value: ", q)
            else:
                pass
        if value_found == 1:
            print("test works!!!!!!!!!")
        else:
            raise NameError("Dipole_pinc.py: Expected output does not match actual output.")
        x += 1

# this basically tests the test_dipole_pinc_interactive.  it makes sure that it actually does raise an exception if I give it bad input.  
class Dipole_pinc_bad_input(unittest.TestCase):       
    def test_bad_input(self):
        self.assertRaises(NameError, test_dipole_pinc_interactive, [(4,10), (5,9)])


test_dipole_pinc_interactive(input_output_list)
test_dipole_pinc_file('test_dipole_pinc.txt')
#test_dipole_pinc_interactive([(4,10),(5,9)])
if __name__ == "__main__":
    unittest.main()


#            print "nope"

# make this a loop so it iterates over all the words....
#    if '%s' %(paleo_out) in string:
 #       print "success"
  #  else:
   #     print("Input: ", paleo_in, "output: ", string) 

