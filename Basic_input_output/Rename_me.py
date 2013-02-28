#! /usr/bin/env python                                                                                                                        
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import Basic_input_output
import PmagPy_tests
import Complex_test

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'


#class Plot(Complex_test.complex_test_object):
class Test_instance(object):
     def __init__(self, name, infile, outfile, ref_out, wrong_out, stdin, WD, *args):
         self.name = name
         if infile != None:
              self.infile = file_prefix + infile
         else:
              self.infile = None
         if outfile != None:
              self.outfile = file_prefix + outfile
         else:
              self.outfile = None
         self.ref_out = ref_out
         self.wrong_out = wrong_out
         self.stdin = stdin
         self.WD = WD
#         self.how_many_args = how_many_args
         self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5 = None, None, None, None, None, None
         self.args = args
         self.parse_args() # SEE IF THIS WORKS
         if self.WD:
              self.infile = infile
              self.outfile = outfile
     
     def parse_args(self):
         if len(self.args) == 1:
             self.arg_0 = self.args[0]
         if len(self.args) == 2:
             self.arg_0 = self.args[0]
             self.arg_1 = self.args[1]
         if len(self.args) == 3:
             self.arg_0 = self.args[0]
             self.arg_1 = self.args[1]
             self.arg_2 = self.args[2]
         if len(self.args) == 4:
             self.arg_0 = self.args[0]
             self.arg_1 = self.args[1]
             self.arg_2 = self.args[2]
             self.arg_3 = self.args[3]
         if len(self.args) == 5:
             self.arg_0 = self.args[0]
             self.arg_1 = self.args[1]
             self.arg_2 = self.args[2]
             self.arg_3 = self.args[3]
             self.arg_4 = self.args[4]
         if len(self.args) == 6:
             self.arg_0 = self.args[0]
             self.arg_1 = self.args[1]
             self.arg_2 = self.args[2]
             self.arg_3 = self.args[3]
             self.arg_4 = self.args[4]
             self.arg_5 = self.args[5]
         for num, arg in enumerate(self.args):
              pass
         
         # this function simply runs the command line program with whatever its options
     def run_program(self, output_type=False): # if plot is true, this function will return files_created.  by default, the function returns stdout
          if self.WD:
               print "WD program about to run:"
               print(self.name, '-WD', directory, '-f', self.infile, '-F', self.outfile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, 'stdin='+str(self.stdin))
               obj = env.run(self.name, '-WD', directory, '-f', self.infile, '-F', self.outfile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin)
          else:
               print "Non-WD program about to run:"
               print self.name, '-f', self.infile, '-F', self.outfile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5,  'stdin=' + str(self.stdin)
               obj = env.run(self.name, '-f', self.infile, '-F', self.outfile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin)
          if output_type == "plot":
               print "plot true"
               print obj.files_created
               return obj.files_created
          elif output_type == "file":
               print "file out"
               print self.outfile
               return self.outfile
          else:
               print obj.stdout
               return obj.stdout


     # this function will get files ready to be compared.  can return a tuple of whatever data types.  
     # or, it may be best just to use file_parse()

         # this function compares real against expected output.  it can take any form of output, as long as the reference output is formatted the same as the expected output.  it will be most useful for short output, otherwise it is nicer to use the check_
     def check_output(self, actual_out, reference_out):
         actual_out, reference_out = str(actual_out), str(reference_out)
         if reference_out in actual_out:#the in syntax is because of weird extra spaces and characters at the end/start of stdout
             print str(self.name) + " output as expected"
         else:
             print "Output was: "
             print str(actual_out)
             print "Output should have been: " 
             print str(reference_out)
             print "Error raised"
             raise NameError(str(self.name) + " produced incorrect output")

     # this function will iterate through a reference list and see if each item of output is correct 
     def check_list_output(self, output_list, correct_output_list):
          print "checking list output"
          print "output_list: " + str(output_list)
          print "correct_output_list: " + str(correct_output_list)
          print "Comparing two lists"
          list_empty = True
          for num, i in enumerate(output_list):
               print "i"
               list_empty = False
               print i, correct_output_list[num]
               if i == correct_output_list[num]:
                    print i, correct_output_list[num]
                    print "correct"
               else:
                    print "Output contained: " + str(i) + " where it should have had " + str(correct_output_list[num])
                    print "Error raised"
                    raise NameError("Wrong output")
          if list_empty:
               print "ONE OR BOTH LISTS DID NOT HAVE CONTENT"
          print "Lists were the same"
          print str(self.name) + " produced correct output"
               
     def check_file_output(self, output_file, correct_file):
          print "checking file output, using: " + str(output_file), str(correct_file)
          parsed_output = PmagPy_tests.file_parse(output_file)
          print parsed_output
          parsed_correct = PmagPy_tests.file_parse(correct_file)
          print parsed_correct
          self.check_list_output(parsed_output, parsed_correct)


               # this function just runs the help option, and makes sure the help message is of a reasonable length
     def test_help(self):
          print "testing help"
          obj = env.run(self.name, '-h')
          message = str(obj.stdout)
          print(len(message))
          if len(message) > 150:
               print "Help message successfully called"
               print "-"
          else:
               raise NameError("Help message for " + str(self.name)+ " failed...")

     # this function will call the interactive option
     def test_interactive(self):
          obj = env.run(self.name, '-i')#, stdin='3')                                                                                  
          print("stdout: "+ str(obj.stdout))
          if len(obj.stdout) > 10:
               print "Interactive mode works"
               print "-"
          else:
               raise NameError("Interactive mode for " + str(self.name) + " came up empty")

        # this will do all that the typical BIO sequence used to do.
         # it assumes output as a file, and it also assumes an interactive mode
     def file_in_file_out_sequence(self):
          self.test_help()
          result = self.run_program(output_type = "file")
          self.check_file_output(result, self.ref_out)
          self.test_interactive()
         

     def plot_program_test(self, stdout=True):
          self.test_help()
          if stdout:
               result = self.run_program()
          else:
               result = self.run_program(output_type = "plot")
          self.check_output(result, self.ref_out)


     def list_sequence(self):
          result = self.run_program()
          new_list = str(result).split()
          self.check_list_output(new_list, self.ref_out)
 #    self.unittest = Bad_test(self)
#     self.unittest.test_list_output_for_error()


class Bad_test(unittest.TestCase):
    def __init__(self, test_obj):
        self.test_obj = test_obj
    def test_file_for_error(self):
        print "Testing: " + str(self.test_obj.name) + " with incorrect file, expecting error"
        # means: run the check_file_output(self.wrong_out, self.ref_out)
        self.assertRaises(NameError, self.test_obj.check_file_output, self.test_obj.wrong_out, self.test_obj.ref_out)
        print "Error expected"
        print "-"


    def test_short_output_for_error(self):
         self.assertRaises(NameError, self.test_obj.check_output, self.test_obj.wrong_out, self.test_obj.ref_out)
         print "Error expected"
         print "-"

    def test_list_output_for_error(self):
         self.assertRaises(NameError, self.test_obj.check_list_output, self.test_obj.wrong_out, self.test_obj.ref_out)
         print "Error expected"
         print "-"


class Other_Bad_test(unittest.TestCase):
    def __init__(self, test_obj):
        self.test_obj = test_obj

    def test_for_error(self):
        print "Running unittest(s) for:  " + str(self.test_obj.name)
        self.assertRaises(NameError, self.test_obj.check_output, self.test_obj.wrong_out, self.test_obj.ref_out)
        print "Error expected"

# BIO example
#     def __init__(self, name, infile, ref_out, wrong_out, stdin, WD, *args):
def complete_angle_test():
    angle = Test_instance('angle.py', 'angle.dat', 'angle_results_new.txt', 'angle_results_correct.txt', 'angle_results_incorrect.txt', None, False)
    angle.file_in_file_out_sequence()
    angle_unittest = Bad_test(angle)
    angle_unittest.test_file_for_error()

# plotting.py example, with stdout
def complete_zeq_test():
    # DONE                                                                                                                                                 
    zeq_infile = 'zeq_example.dat'
    zeq_reference_output = """0      0.0 9.283e-08   339.9    57.9 
1      2.5 7.582e-08   325.7    49.1 
2      5.0 6.292e-08   321.3    45.9 
3     10.0 5.209e-08   314.8    41.7 
4     15.0 4.455e-08   310.3    38.7 
5     20.0 3.954e-08   305.0    37.0 
6     30.0 3.257e-08   303.9    34.7 
7     40.0 2.567e-08   303.0    32.3 
8     50.0 2.252e-08   303.6    32.4 
9     60.0 1.982e-08   299.8    30.8 
10     70.0 1.389e-08   292.5    31.0 
11     80.0 1.257e-08   297.0    25.6 
12     90.0 5.030e-09   299.3    11.3 
 s[a]ve plot, [b]ounds for pca and calculate, change [h]orizontal projection angle, [q]uit:   """
    zeq_wrong_output = "Hi there"
    zeq_outfile = None
    zeq = Test_instance('zeq.py', zeq_infile, zeq_outfile, zeq_reference_output, zeq_wrong_output, 'q', False, '-u', 'C')
    zeq.plot_program_test(stdout=True)
    zeq_unittest = Bad_test(zeq)
    zeq_unittest.test_short_output_for_error()

# plotting.py example, no stdout
def complete_chartmaker_test():
     chartmaker_infile = None
     chartmaker_outfile = None
     chartmaker_reference = "{'chart.txt': <FoundFile ./new-test-output:chart.txt>}"
     chartmaker_wrong = "wrong"
     chartmaker = Test_instance('chartmaker.py', chartmaker_infile, chartmaker_outfile, chartmaker_reference, chartmaker_wrong, 'q', False)
     chartmaker.plot_program_test(stdout=False)
     chartmaker_unittest = Bad_test(chartmaker)
     chartmaker_unittest.test_short_output_for_error()

# UC example
def complete_di_eq_test():
     print "Testing di_eq.py"
     di_eq_infile = 'di_eq_example.dat'
     di_eq_outfile = None
     di_eq_reference = ['-0.239410', '-0.893491', '0.436413', '0.712161', '0.063844', '0.760300', '0.321447', '0.686216', '0.322720',\
 '0.670562', '0.407412', '0.540654', '0.580156', '0.340376', '0.105351', '0.657728', '0.247173', '0.599687', '0.182349', '0.615600',\
 '0.174815', '0.601717', '0.282746', '0.545472', '0.264863', '0.538273', '0.235758', '0.534536', '0.290665', '0.505482', '0.260629',\
 '0.511513', '0.232090', '0.516423', '0.244448', '0.505666', '0.277927', '0.464381', '0.250510', '0.477152', '0.291770', '0.440816',\
 '0.108769', '0.516148', '0.196706', '0.482014', '0.349390', '0.381292', '0.168407', '0.475566', '0.206286', '0.446444', '0.175701',\
 '0.450649', '0.301104', '0.378539', '0.204955', '0.423970', '0.199755', '0.422584', '0.346920', '0.308010', '0.119030', '0.441144',\
 '0.239848', '0.376486', '0.269528', '0.342510', '0.085451', '0.423789', '0.192224', '0.387233', '0.172608', '0.395084', '0.272008',\
 '0.320741', '0.393981', '0.117451', '-0.017726', '0.406002', '0.154273', '0.367000', '0.213903', '0.335760', '0.103221', '0.372202'\
, '0.231833', '0.283245', '0.072160', '0.351538', '0.007802', '0.319236', '0.152583', '0.265350', '0.248133', '0.136412']
     di_eq_wrong = "wrong"
     di_eq = Test_instance('di_eq.py', di_eq_infile, di_eq_outfile, di_eq_reference, di_eq_wrong, None, False)
     #result = di_eq.run_program()
     #new_list = str(result).split()
     #di_eq.check_list_output(new_list, di_eq.ref_out)
     di_eq_unittest = Bad_test(di_eq)
     di_eq_unittest.test_list_output_for_error()


     

    # maybe work on better unittests

def complete_working_test():
#     complete_angle_test()
 #    complete_zeq_test()
  #   complete_chartmaker_test()
     complete_di_eq_test()

if __name__ == '__main__':
#    pass
     complete_working_test()



