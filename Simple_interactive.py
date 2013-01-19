

#import unittest
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./test-output')


class interactive_test(object):
    """
    trying to make a class for the basic interactive tests
    """
    def __init__(self, name, input_output_list, file_name, df="default"):
        self.name = name
        self.input_output_list = input_output_list
        self.file_name = file_name
        self.df = df

    def test_interactive(self):
        for i in self.input_output_list:
            print("-")
            data_in = i[0]
            data_out = i[1]
            print("expected data_out: ", data_out)
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
            if value_found == 0:
                raise NameError(self.name, "Expected output does not match actual output")
            value_found = 0
            print("Test successful")

    def test_file(self):
        # below is  a problem.  need to figure out how to de-specify it
        correct_values = (33.0,38.9,54.5,-90.0)
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

# this needs to be replaced.... for now it doesn't actually run unit tests even with the method                                                                                   
#class Dipole_pinc_bad_input(unittest.TestCase):
 #   def test_bad_input(self):
  #      error_list = [(4,10), (5,9)]
   #     for error in error_list:
    #        self.assertRaises(NameError, test_dipole_pinc_interactive, error)

#if __name__ == "__main__":

#def do_unittest():
 #   unittest.main()
