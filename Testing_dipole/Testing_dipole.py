import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest

file_prefix = "/Users/nebula/Python/Testing_dipole/"

class dipole(object):
    """
    trying to make a class for the basic interactive tests
    """
    # name should be the program name, i.e. dipole_pinc.py.  input_output_list is correctly verified pairs of data in/data out.  File_name should be a file that contains input for the program, one number per line. Correct_file_values are the proper output for the submitted file values.  
    def __init__(self, name, input_output_list, file_name, correct_file_values=(1,2,3,4,5)):
        self.name = name
        self.input_output_list = input_output_list
        self.file_name = file_prefix + file_name
        self.correct_file_values = correct_file_values

    def interactive_test(self):
        print "-"
        print "Running interactive test: " + str(self.name)
        # this iterates through a set of verified input/output pairs, testing them with the interactive 
        for i in self.input_output_list:
            print "-"
            data_in = i[0]
            data_out = i[1]
            print "data in: "+ str(data_in)
            print "expected data_out: " + str(data_out)
            # runs a command line sequence, which translates to the program name and its arguments, i.e. dipole_pinc.py -i 13
            obj = env.run(self.name, '-i', stdin='%s' %(data_in))
            string = str(obj.stdout)
            array = string.split()
            print "array of output: " + str(array)
           # print array[8]
            value_found = 0
            # this loops through the output and makes sure the expected numerical output is in there
            for z in array:
                if str(z) == str(data_out):
                    print "output contained: "+ str(z)
                    value_found = 1
                else:
                    pass
            # if the correct value was not found in the ouput array, it raises an error:
            if value_found == 0:
                raise NameError(self.name, "Expected output does not match actual output")
            value_found = 0
        print str(self.name) + " test successful"


    def file_test(self):
        print "-"
        print "Running file test: " + str(self.name)
        obj = env.run(self.name, '-f', self.file_name)
        print "stdout: " + str(obj.stdout)
        print "correct_file_values: " + str(self.correct_file_values)
        # a tuple that has all of the proper corresponding values to the file examples
        correct_values = self.correct_file_values
        # creates a nice list of the output
        output = obj.stdout.split()
        clean_output = []
        for item in output:
            item = float(item)
            clean_output.append(item)
        print "clean_output: " + str(clean_output)
        z = 0
        # iterates through the results and checks them against the correct values
        for x in clean_output:
            if x == correct_values[z]:
                pass
            else:
                print "x == " +str(x) + " it should have been: "+ str(correct_values[z])
                raise NameError(self.name, "Expected output does not match actual output")
            z += 1
        print str(self.name) + " file test successful"
                


def complete_dipole_pinc_test():
    dipole_pinc = dipole("dipole_pinc.py",[(70.,79.7),(3.,6.),(118,-75.1),(32,51.3)],"test_dipole_pinc.txt",(33.0,38.9,54.5,9.9)) 
    dipole_pinc.interactive_test()
 #   dipole_pinc.file_test()

def complete_dipole_plat_test():
    dipole_plat = dipole("dipole_plat.py", [(15.0,7.6),(81.0, 72.4),(-2.0,-1.0)], "test_dipole_pinc.txt", (9.2,11.4,19.3,2.5))
    dipole_plat.interactive_test()
    dipole_plat.file_test()


# these are instances for the unittests
badtest_pinc = dipole("dipole_pinc.py", [(3.5, 6.0),(93.0, 15.7),(30.,6.)], "test_dipole_pinc.txt", (33.0,38.9,54.5,12.0))
badtest_plat = dipole("dipole_plat.py", [(3.0, 6.0),(8.0, 15.7),(3.,6.)], "test_dipole_pinc.txt", (1,2,3,4,5))

class Bad_input(unittest.TestCase):
    def test_dipole_pinc_interactive(self):
        self.assertRaises(NameError, badtest_pinc.interactive_test)

    def test_dipole_pinc_file(self):
        self.assertRaises(NameError, badtest_pinc.file_test)

    def test_dipole_plat_interactive(self):
        self.assertRaises(NameError, badtest_plat.interactive_test)

    def test_dipole_plat_file(self):
        self.assertRaises(NameError, badtest_plat.file_test)


def do_unittest():
    unittest.main(module='Testing_dipole')

def complete_dipole_test():
    complete_dipole_pinc_test()
    complete_dipole_plat_test()
    do_unittest()


