import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest

# need to put in a test for the -h option
class dipole(object):
    """
    trying to make a class for the basic interactive tests
    """
    # name should be the program name, i.e. dipole_pinc.py.  input_output_list is correctly verified pairs of data in/data out.  File_name should be a file that contains input for the program, one number per line. Correct_file_values are the proper output for the submitted file values.  
    def __init__(self, name, input_output_list, file_name, correct_file_values=(1,2,3,4,5), df="default"):
        self.name = name
        self.input_output_list = input_output_list
        self.file_name = file_name
        self.correct_file_values = correct_file_values
        self.df = df

    
    def interactive_test(self):
        print("Testing: ", self.name)
        for i in self.input_output_list:
            print("-")
            data_in = i[0]
            data_out = i[1]
            print("data in: ", data_in)
            print("expected data_out: ", data_out)
            # runs a command line sequence, which translates to the program name and its arguments, i.e. dipole_pinc.py -i 13
            obj = env.run(self.name, '-i', stdin='%s' %(data_in))
            string = str(obj.stdout)
            array = string.split()
            print("ARRAY: ", array)
            value_found = 0
            print(array)
            for z in array:
                if str(z) == str(data_out):
                    print(z)
                    print "SUCCESS"
                    value_found = 1
                else:
                    pass
            # if the correct value was not found in the ouput array, it raises an error:
            if value_found == 0:
                raise NameError(self.name, "Expected output does not match actual output")
            value_found = 0
            print("Test successful")


    def real_file_test(self):
        # equivalent of running the_program.py -f the_file.txt
        obj = env.run(self.name, '-f', self.file_name)
        print("stdout: ",obj.stdout)
        print("correct_file_values: ",self.correct_file_values)
        # a tuple that has all of the proper corresponding values to the file examples
        correct_values = self.correct_file_values
        # creates a nice list of the output
        output = obj.stdout.split()
        clean_output = []
        for item in output:
            item = float(item)
            clean_output.append(item)
        print("clean_output: ",clean_output)
        z = 0
        # iterates through each result and checks it against the correct values
        for x in clean_output:
            print("iterating through clean output")
            if x == correct_values[z]:
                print "Well done"
            else:
                print("x == ", x, " it should have been: ", correct_values[z])
                print "You fucked it up!"
                raise NameError(self.name, "Expected output does not match actual output")
            z += 1
                

# the next tests basically tests the test_dipole_pinc_interactive.  it makes sure that it actually does raise an exception it gets bad input.  Below are dipole instances for the two bad examples

badtest_pinc = dipole("dipole_pinc.py", [(3.5, 6.0),(93.0, 15.7),(30.,6.)], "/Users/nebula/Python/Testing_dipole/test_dipole_pinc.txt", (33.0,38.9,54.5,12.0))
badtest_plat = dipole("dipole_plat.py", [(3.0, 6.0),(8.0, 15.7),(3.,6.)], "/Users/nebula/Python/Testing_dipole/test_dipole_pinc.txt", (1,2,3,4,5))

class Bad_input(unittest.TestCase):
    def test_dipole_pinc_interactive(self):
        self.assertRaises(NameError, badtest_pinc.interactive_test)

    def test_dipole_pinc_file(self):
        self.assertRaises(NameError, badtest_pinc.real_file_test)

    def test_dipole_plat_interactive(self):
        self.assertRaises(NameError, badtest_plat.interactive_test)

    def test_dipole_plat_file(self):
        self.assertRaises(NameError, badtest_plat.real_file_test)

def find_name():
    if __name__ == 'Simple_interactive':
        print __name__
        print unittest.main
    else:
        print __name__
        print '__Simple_interactive__'
        print("lame")

def do_unittest():
    unittest.main(module='Testing_dipole')



# this was basically not useful, but it may have some recyclable bits of code
"""
def file_test(self):
        print("Testing: ", self.name)
        # below is  a problem.  need to figure out how to de-specify it
        correct_values = self.correct_file_values
        the_file = open(self.file_name).readlines()
        clean_file = []
        # removes the extra characters from the input file
        for l in the_file:
            new_line = l.strip('\n')
            clean_file.append(new_line)
            print("clean file: ",clean_file)
        # moved x out of the previous for loop.  it really didn't belong there
        x = 0
        for line in clean_file:
            print("-")
            obj = env.run(self.name, '-i', stdin=line)
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
                raise NameError(self.name, "Expected output does not match actual output.")
            x += 1
"""
