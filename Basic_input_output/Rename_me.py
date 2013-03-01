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
     def run_program(self, output_type="stdout"): # 
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
          elif output_type == "stdout":
               print "stdout out"
               print obj.stdout
               return obj.stdout
          else:
               raise NameError("invalid output type was selected for run_program()")


     # this function will get files ready to be compared.  can return a tuple of whatever data types.  
     # or, it may be best just to use file_parse()

         # this function compares real against expected output.  it can take any form of output, as long as the reference output is formatted the same as the expected output.  it will be most useful for short output, otherwise it is nicer to use the check_
     def check_output(self, actual_out, reference_out):
          print "Checking output (can be any output type)"
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
               raise NameError("Output list empty")
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
          print "testing help for " + str(self.name)
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
          print "testing interactive for " + str(self.name)
          obj = env.run(self.name, '-i', stdin=self.stdin)#, stdin='3')                                                                                           print("stdout: "+ str(obj.stdout))
          if len(obj.stdout) > 10:
               print "Interactive mode works"
               print "-"
          else:
               raise NameError("Interactive mode for " + str(self.name) + " came up empty")

        # this will do all that the typical BIO sequence
         # it assumes output as a file, and it also assumes an interactive mode
     def file_in_file_out_sequence(self, interactive=False):
          self.test_help()
          result = self.run_program(output_type = "file")
          self.check_file_output(result, self.ref_out)
          if interactive:
               self.test_interactive()  
         
# this one tests plotting programs, either that give stdout or that just make a plot
     def plot_program_sequence(self, stdout=True):
          self.test_help()
          if stdout:
               result = self.run_program()
          else:
               result = self.run_program(output_type = "plot")
          self.check_output(result, self.ref_out)

# this one is for programs that produce stdout, usually long 
     def list_sequence(self):
          result = self.run_program(output_type = "stdout")
          print result
          new_list = str(result).split()
          self.check_list_output(new_list, self.ref_out)

# necessary???
     def stdout_sequence(self):
          result = self.run_program(output_type = "stdout")
          result = float(result)
          self.check_output(result, self.ref_out)


     def unittest_file(self):
          unittest = Bad_test(self)
          unittest.test_file_for_error()
          
     def unittest_short_output(self):
          unittest = Bad_test(self)
          unittest.test_short_output_for_error()

     def unittest_list(test_obj):
          unittest = Bad_test(self)
          unittest.test_list_output_for_error()


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
         print "Testing: " + str(self.test_obj.name) + " with incorrect short output, expecting error"
         self.assertRaises(NameError, self.test_obj.check_output, self.test_obj.wrong_out, self.test_obj.ref_out)
         print "Error expected"
         print "-"

    def test_list_output_for_error(self):
         print "Testing: " + str(self.test_obj.name) + " with incorrect list output, expecting error"
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
def complete_angle_test(): # BIO type
    angle = Test_instance('angle.py', 'angle.dat', 'angle_results_new.txt', 'angle_results_correct.txt', 'angle_results_incorrect.txt', None, False)
    angle.file_in_file_out_sequence(interactive=True)
    angle.unittest_file()
#    angle_unittest = Bad_test(angle)
 #   angle_unittest.test_file_for_error()

# plotting.py example, with stdout
def complete_zeq_test(): # Plotting w/stdout
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
    zeq.plot_program_sequence(stdout=True)
    zeq_unittest = Bad_test(zeq)
    zeq_unittest.test_short_output_for_error()

# plotting.py example, no stdout
def complete_chartmaker_test():  # Plotting w/out stdout
     chartmaker_infile = None
     chartmaker_outfile = None
     chartmaker_reference = "{'chart.txt': <FoundFile ./new-test-output:chart.txt>}"
     chartmaker_wrong = "wrong"
     chartmaker = Test_instance('chartmaker.py', chartmaker_infile, chartmaker_outfile, chartmaker_reference, chartmaker_wrong, 'q', False)
     chartmaker.plot_program_sequence(stdout=False)
     chartmaker_unittest = Bad_test(chartmaker)
     chartmaker_unittest.test_short_output_for_error()

# UC example.  creates a list, tests that list
def complete_di_eq_test(): # basic list type
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
     di_eq.list_sequence()
     di_eq_unittest = Bad_test(di_eq)
     di_eq_unittest.test_list_output_for_error()



# the rest of the UCs
#     def __init__(self, name, infile, outfile, ref_out, wrong_out, stdin, WD, *args):
# this one is a weird amalgam, because of two -f inputs.  but it works.  
def complete_combine_magic_test(): # irregular type
    output_file = 'combine_magic_output_new.out'
    reference_file =  'combine_magic_output_correct.out'
    incorrect_output = 'combine_magic_output_incorrect.out'
    input_1 = 'combine_magic_input_1.dat'
    input_2 = 'combine_magic_input_2.dat'
    # have to run it specially, because -f takes two arguments.  it doesn't fit with its class in this regard. 
    obj = env.run('combine_magic.py', '-WD', directory, '-F', output_file, '-f', input_1, input_2)
    combine_magic = Test_instance('combine_magic.py', None, output_file, reference_file, incorrect_output, None, True, '-f', input_1, input_2)
    combine_magic.check_file_output(combine_magic.outfile, combine_magic.ref_out)
    combine_magic.test_help()
    combine_magic_unittest = Bad_test(combine_magic)
    combine_magic_unittest.test_file_for_error()
    print "Successfully finished combine_magic_test"


def complete_cont_rot_test(): # Irregular type -- running specially because it has so many command line options
    obj = env.run('cont_rot.py', '-con', 'af:sam', '-prj', 'ortho', '-eye', '-20', '0', '-sym', 'k-', '1', '-age', '180', '-res', 'l\
', stdin='a')
    output = str(obj.files_created) # output is the name of the plot that has been saved
    reference_output = "{'Cont_rot.pdf': <FoundFile ./new-test-output:Cont_rot.pdf>}"
    incorrect_output = "wrong"
    cont_rot = Test_instance('cont_rot.py', None, output, reference_output, incorrect_output, 'a', False)
    cont_rot.check_output(cont_rot.outfile, cont_rot.ref_out)
    cont_rot.test_help()
    cont_rot_unittest = Bad_test(cont_rot)
    cont_rot_unittest.test_short_output_for_error()

def complete_customize_criteria_test():  # BIO type
    customize_criteria_infile = 'customize_criteria_example.dat'
    customize_criteria_output = 'customize_criteria_outfile.out'
    customize_criteria_reference = "customize_criteria_output_correct.out"
    customize_criteria_wrong = "customize_criteria_output_incorrect.out"
    customize_criteria = Test_instance('customize_criteria.py', customize_criteria_infile, customize_criteria_output, customize_criteria_reference, customize_criteria_wrong, '1', False)
    customize_criteria.file_in_file_out_sequence(interactive=True)
    customize_criteria_unittest = Bad_test(customize_criteria)
    customize_criteria_unittest.test_file_for_error()




grab_magic_key_reference_list = ['42.60264', '42.60264', '42.60352', '42.60104', '42.73656', '42.8418', '42.8657', '42.92031', '42.56857', '42.49964', '42.49962', '42.50001', '42.52872', '42.45559', '42.48923', '42.46186', '42.69156', '42.65289', '43.30504', '43.36817', '43.42133', '43.8859', '43.84273', '43.53289', '43.57494', '44.15663', '44.18629']

def complete_grab_magic_key_test(): # Basic list type
    print "Testing grab magic"
    grab_magic_key_infile = 'grab_magic_key_er_sites.txt'
    grab_magic_key_outfile = None
    grab_magic_key_wrong = "wrong"
    grab_magic_key_reference = grab_magic_key_reference_list
    grab_magic_key = Test_instance('grab_magic_key.py', grab_magic_key_infile, grab_magic_key_outfile, grab_magic_key_reference, grab_magic_key_wrong, None, True, '-key', 'site_lat')
    grab_magic_key.list_sequence()
    grab_magic_unittest = Bad_test(grab_magic_key)
    grab_magic_unittest.test_list_output_for_error()
    print "Sucessfully finished complete_grab_magic_key_test"


def complete_incfish_test(): # BIO type
    incfish_infile = 'incfish_example_inc.dat'
    incfish_outfile = 'incfish_results_new.out'
    incfish_reference = 'incfish_results_correct.out'
    incfish_wrong = 'incfish_results_incorrect.out'
    incfish = Test_instance('incfish.py', incfish_infile, incfish_outfile, incfish_reference, incfish_wrong, None, False)
    incfish.file_in_file_out_sequence()
    incfish_unittest = Bad_test(incfish)
    incfish_unittest.test_file_for_error()
    # no interactive                                                                                                                 




def complete_magic_select_test(): # BIO type.. but it doesn't work yet!  Lisa must add in a WD option.  
    magic_select_infile = 'magic_select_example.txt'
    magic_select_outfile = 'magic_select_results_new.out'
    magic_select_reference = 'magic_select_results_correct.out'
    magic_select_wrong = 'magic_select_results_incorrect.out'
    magic_select = Test_instance('magic_select.py', magic_select_infile, magic_select_outfile, magic_select_reference, magic_select_wrong, None, True, '-key', 'magic_method_codes', 'LP-DIR-AF', 'has')
    magic_select.file_in_file_out_sequence()
    # add unittest when you get it together

def complete_nrm_specimens_magic_test(): # BIO type
     print "Testing nrm_specimens_magic.py"
     fsa = file_prefix + 'nrm_specimens_magic_er_samples.txt'
     nrm_specimens_magic_infile = 'nrm_specimens_magic_measurements.txt'
     nrm_specimens_magic_outfile = 'nrm_specimens_results_new.out'
     nrm_specimens_magic_reference = 'nrm_specimens_results_correct.out'
     nrm_specimens_magic_wrong = 'nrm_specimens_results_incorrect.out'
     nrm_specimens_magic = Test_instance('nrm_specimens_magic.py', nrm_specimens_magic_infile, nrm_specimens_magic_outfile, nrm_specimens_magic_reference, nrm_specimens_magic_wrong, None, False, '-fsa', fsa, '-crd', 'g')
     nrm_specimens_magic.file_in_file_out_sequence()
     nrm_specimens_unittest = Bad_test(nrm_specimens_magic)
     nrm_specimens_unittest.test_file_for_error()
     print "Successfully completed nrm_specimens_magic.py tests"

def complete_sundec_test(): # list type
     sundec_infile = 'sundec_example.dat'
     sundec_outfile = None
     sundec_reference = ['154.2']
     sundec_wrong = ['154.3']
     sundec = Test_instance('sundec.py', sundec_infile, sundec_outfile, sundec_reference, sundec_wrong, None, False)
     sundec.run_program()
     sundec.list_sequence()
     sundec_unittest = Bad_test(sundec)
     sundec_unittest.test_list_output_for_error()
     print "Successfully finished sundec.py tests"

def complete_pca_test(): # list type
     pca_infile = 'pca_example.dat'
     pca_outfile = None
     pca_reference = pca_correct_out
     pca_wrong = ['eba24a', 'wrong']
     pca = Test_instance('pca.py', pca_infile, pca_outfile, pca_reference, pca_wrong, None, False, '-dir', 'L', '1', '10')
#     pca.run_program(output_type="list")
     pca.list_sequence()
     pca_unittest = Bad_test(pca)
     pca_unittest.test_list_output_for_error()
     


pca_correct_out = ['eba24a', 'DE-BFL', '0', '0.00', '339.9', '57.9', '9.2830e-05', '1', '2.50', '325.7', '49.1', '7.5820e-05', '2', '5.00', '321.3', '45.9', '6.2920e-05', '3', '10.00', '314.8', '41.7', '5.2090e-05', '4', '15.00', '310.3', '38.7', '4.4550e-05', '5', '20.00', '305.0', '37.0', '3.9540e-05', '6', '30.00', '303.9', '34.7', '3.2570e-05', '7', '40.00', '303.0', '32.3', '2.5670e-05', '8', '50.00', '303.6', '32.4', '2.2520e-05', '9', '60.00', '299.8', '30.8', '1.9820e-05', '10', '70.00', '292.5', '31.0', '1.3890e-05', '11', '80.00', '297.0', '25.6', '1.2570e-05', '12', '90.00', '299.3', '11.3', '0.5030e-05', 'eba24a', 'DE-BFL', '10', '2.50', '70.00', '8.8', '334.9', '51.5']

def complete_vgp_di_test():
     vgp_di_infile = 'vgp_di_example.dat'
     vgp_di_oufile = None
     vgp_di_
  #  vgp_di = UC('vgp_di.py', 'vgp_di_example.dat')
     vgp_di.test_help()
     vgp_di.test_interactive()
     file_name = file_prefix + 'vgp_di_example.dat'

def complete_working_test():
     complete_angle_test()
 #    complete_zeq_test()
  #   complete_chartmaker_test()
#     complete_di_eq_test()
#     complete_combine_magic_test()
#     complete_cont_rot_test()
 #    complete_customize_criteria_test()
  #   complete_grab_magic_key_test()
#     complete_incfish_test()
#     complete_magic_select_test() NEEDS -WD!!!!!
     #     complete_nrm_specimens_magic_test()
#     complete_sundec_test()
#     complete_pca_test()

if __name__ == '__main__':
#    pass
     complete_working_test()



