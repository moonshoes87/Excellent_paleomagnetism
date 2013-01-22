import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest

class dipole(object):
    """
    trying to make a class for the basic interactive tests
    """
    # name should be the program name, i.e. dipole_pinc.py.  input_output_list is correctly verified pairs of data in/data out.  File_name should be a file that contains input for the program, one number per line. Correct_file_values are the proper output for the submitted file values.  
    def __init__(self, name, input_output_list, file_name, correct_file_values, df="default"):
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

    def file_test(self):
        print("Testing: ", self.name)
        # below is  a problem.  need to figure out how to de-specify it
        correct_values = self.correct_file_values
        the_file = open(self.file_name).readlines()
        clean_file = []
        for l in the_file:
            new_line = l.strip('\n')
            clean_file.append(new_line)
            print("clean file: ",clean_file)
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

# this basically tests the test_dipole_pinc_interactive.  it makes sure that it actually does raise an exception it gets bad input    

badtest_pinc = dipole("dipole_pinc.py", [(3.5, 6.0),(93.0, 15.7),(30.,6.)], "test_dipole_pinc.txt", (1,2,3,4,5))
badtest_plat = dipole("dipole_plat.py", [(3.0, 6.0),(8.0, 15.7),(3.,6.)], "test_dipole_pinc.txt", (1,2,3,4,5))

class Bad_input(unittest.TestCase):
    def test_dipole_pinc(self):
        self.assertRaises(NameError, badtest_pinc.interactive_test)

    def test_dipole_plat(self):
        self.assertRaises(NameError, badtest_plat.interactive_test)


def do_thing():
    if __name__ == 'Simple_interactive':
        print __name__
        print unittest.main
    else:
        print __name__
        print '__Simple_interactive__'
        print("lame")

def do_unittest():
    # make newtest here, but make it specific to which file you want to unittest....?
    # changing the names of the non unittest to things that don't start with test doesn't prevent it from testing them.  so, I need to figure out/understand the syntax to specifically say, just do "test_bad_input"
    # newtest= dipole("dipole_plat.py", [(70, 79.7),(3., 6.),(118, -75.1),(32, 51.3)], "test_dipole_pinc.txt")
    unittest.main(module='Testing_dipole')
