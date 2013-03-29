#! /usr/bin/env python                                                                                                         

# MOVED ALL TESTS OVER
               
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import Basic_input_output
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'


class complex_test_object(object):

     def __init__(self, name, infile, ref_out, wrong_out, WD, stdin, *args): # removed stdin
         self.name = name
         self.infile = file_prefix + infile
         self.ref_out = ref_out
         self.wrong_out = wrong_out
#         self.stdin = stdin
         self.WD = WD
         self.stdin = stdin
#         self.how_many_args = how_many_args
         self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5 = None, None, None, None, None, None
         self.args = args
         self.parse_args() # SEE IF THIS WORKS
         if self.WD:
              print "WD"
              self.infile = infile
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
         
     def run_program(self, plot=False): # if plot is true, this function will return files_created.  by default, the function returns stdout
         if self.WD:
             print "WD program about to run:"
             print(self.name, '-WD', directory, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5)# 'stdin='+str(self.stdin))
             obj = env.run(self.name, '-WD', directory, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin) 
# stdin=self.stdin)
         else:
             print "Non-WD program about to run:"
             print self.name, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5#  'stdin=' + str(self.stdin)
             obj = env.run(self.name, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin)# stdin=self.stdin)
         if plot:
             print obj.files_created
             return obj.files_created
         else:
             print obj.stdout
             return obj.stdout
     
     def check_output(self, actual_out, reference_out):
         actual_out, reference_out = str(actual_out), str(reference_out)
         if reference_out in actual_out:
             print str(self.name) + " output as expected"
         else:
             print "Output was: "
             print str(actual_out)
             print "Output should have been: " 
             print str(reference_out)
             print "Error raised"
             raise NameError(str(self.name) + " produced incorrect output")



     def compare_two_files(self, output, reference_output):
          clean_output = PmagPy_tests.file_parse(output)
          clean_reference = PmagPy_tests.file_parse(reference_output)
          for z, line in enumerate(clean_output):
               output_file_empty = False
               print(line, " should equal ", clean_reference[z])
               if line == clean_reference[z]:
                    print "success"
               else:
                    print "Error raised"
                    raise NameError(str(self.name) + " expected output does not match actual output")
          if output_file_empty:
               print "OUTPUT FILE WAS EMPTY, error raised"
               raise NameError("Running " + self.name +  "  produced no output")
          print "Test file found no errors, using as reference: "+ str(reference_output)
          print "-"



class Bad_test(unittest.TestCase):
    def __init__(self, plotting_obj):
        self.plotting_obj = plotting_obj

    def test_for_error(self):
        print "Running unittest(s) for:  " + str(self.plotting_obj.name)
        self.assertRaises(NameError, self.plotting_obj.check_output, self.plotting_obj.wrong_out, self.plotting_obj.ref_out)
        print "Error expected"



#    ani_depthplot = Plot('ani_depthplot.py', ani_depthplot_infile, ani_depthplot_reference, ani_depthplot_wrong, 'a', True, '-fsa', ani_depthplot_fsa)

def complete_azdip_magic_test():
     # non-WD
     azdip_magic_infile = 'azdip_magic_example.dat'
     azdip_magic_reference = file_prefix + 'azdip_magic_output_correct.out'
     azdip_magic_wrong = "wrong"
     azdip_magic_outfile = file_prefix + 'azdip_magic_output.out' # file_prefix + 
     azdip_magic = complex_test_object('azdip_magic.py', azdip_magic_infile, azdip_magic_reference, azdip_magic_wrong, False, None, '-Fsa', azdip_magic_outfile, '-mcd', 'FS-FD:SO-POM', '-loc', "Northern Iceland")
     azdip_magic.run_program()
     azdip_magic.compare_two_files(azdip_magic_outfile, azdip_magic.ref_out)
     azdip_magic_unittest = Bad_test(azdip_magic)
     azdip_magic_unittest.test_for_error()

#complete_azdip_magic_test()
     
def complete_download_magic_test():
     download_magic_infile = 'download_magic_example.dat'
     download_magic_reference = PmagPy_tests.file_parse(file_prefix + 'download_magic_correct_output.out')
     download_magic_wrong = "wrong"
     download_magic = complex_test_object('download_magic.py', download_magic_infile, download_magic_reference, download_magic_wrong, True, 'y')
     output = download_magic.run_program()
     subprocess.call(['rm', '-rf', 'Location_1/'])
     subprocess.call(['rm', 'er_locations.txt', 'magic_measurements.txt', 'pmag_samples.txt', 'er_samples.txt', 'magic_methods.txt', 'pmag_sites.txt', 'er_ages.txt', 'er_sites.txt', 'pmag_criteria.txt', 'pmag_specimens.txt', 'er_citations.txt', 'er_specimens.txt', 'pmag_results.txt'])
     # this test just runs the program and verifies that it makes no errors.  that's really all it reasonably can do.  

def complete_working_test():
     complete_azdip_magic_test()
     complete_download_magic_test()

if __name__ == "__main__":
     complete_working_test()
