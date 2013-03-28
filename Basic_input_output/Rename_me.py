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
     
     def parse_args(self): # turns up to 6 args into command line options
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
         # it takes the arguments "stdout", "plot", or  "file", and respectively returns the standard output for the program, the plots created, or the file created/updated
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
               print "output is plot"
               if obj.files_created == {}:
                    print "files updated: ", obj.files_updated
                    return obj.files_updated
               else:
                    print "new files created: ", obj.files_created
                    return obj.files_created
          elif output_type == "file":
               print "output is file"
               print self.outfile
               return self.outfile
          elif output_type == "stdout":
               print "output is stdout"
               print obj.stdout
               return obj.stdout
          else:
               raise NameError("invalid output type was selected for run_program()")


         # this function compares real against expected output.  it can take any form of output, as long as the reference output is formatted the same as the expected output.  
     def check_output(self, actual_out, reference_out):
          print "Checking stdout output"
          actual_out, reference_out = str(actual_out), str(reference_out)
          if reference_out in actual_out:#the in syntax is because of weird extra spaces and characters at the end/start of stdout
               print str(self.name) + " output as expected"
               print "-"
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
          print "output_list:         " + str(output_list)
          print "correct_output_list: " + str(correct_output_list)
          print "Comparing two lists"
          list_empty = True
          for num, i in enumerate(output_list):
               list_empty = False
               if i == correct_output_list[num]:
                    print i, "   ",  correct_output_list[num]
                   # print "correct"
               else:
                    print "Output contained:    " + str(i)  
                    print "but should have had: " + str(correct_output_list[num])
                    print "Error raised"
                    raise NameError("Wrong output")
          if list_empty:
               print "ONE OR BOTH LISTS DID NOT HAVE CONTENT"
               raise NameError("Output list empty")
          print "Lists were the same"
          print str(self.name) + " produced correct output"
               
     def check_file_output(self, output_file, correct_file): # takes in two file names as arguments, parses their contents into list format, and then compares the first against the second
          print "checking file output, using: " + str(output_file) + " AND " + str(correct_file)
#          parsed_output = PmagPy_tests.file_parse(output_file)
          parsed_output = PmagPy_tests.file_parse_by_word_and_pmagpy_strip(output_file)
          print parsed_output
#          parsed_correct = PmagPy_tests.file_parse(correct_file)
          parsed_correct = PmagPy_tests.file_parse_by_word_and_pmagpy_strip(correct_file)
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

        # This sequence fully tests a standard program that takes in a file and outputs another file
         # it assumes output as a file. it assumes no interactive mode, but can be given the argument interactive=True, in which case it will test it.  
     def file_in_file_out_sequence(self, interactive=False):
          self.test_help()
          result = self.run_program(output_type = "file")
          self.check_file_output(result, self.ref_out)
          if interactive:
               self.test_interactive()  
          self.unittest_file()         
# this sequence fully tests plotting programs, either that give stdout or that just make a plot
     def plot_program_sequence(self, stdout=True):
          self.test_help()
          if stdout:
               result = self.run_program()
          else:
               result = self.run_program(output_type = "plot")
          self.check_output(result, self.ref_out)
          self.unittest_short_output() # possibly this is not the best way to do this.  possibly some should get listified.  but, fuck it. 

# this sequence fully tests programs that produce stdout
     def list_sequence(self):
          result = self.run_program(output_type = "stdout")
          print result
          new_list = str(result).split()
          self.check_list_output(new_list, self.ref_out)
          self.unittest_list()

     def unittest_file(self): # creates a unittest for a simple file in file out program
          unittest = Bad_test(self)
          unittest.test_file_for_error()
          
     def unittest_short_output(self): # creates a unittest for a plot program 
          unittest = Bad_test(self)
          unittest.test_short_output_for_error()

     def unittest_list(self): # creates a unittest for a stdout-producing program
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
#    angle.unittest_file()


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
 #   zeq.unittest_short_output()


# plotting.py example, no stdout
def complete_chartmaker_test():  # Plotting w/out stdout
     chartmaker_infile = None
     chartmaker_outfile = None
     chartmaker_reference = "{'chart.txt': <FoundFile ./new-test-output:chart.txt>}"
     chartmaker_wrong = "wrong"
     chartmaker = Test_instance('chartmaker.py', chartmaker_infile, chartmaker_outfile, chartmaker_reference, chartmaker_wrong, 'q', False)
     chartmaker.plot_program_sequence(stdout=False)
#     chartmaker.unittest_short_output()


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
#     di_eq_unittest = Bad_test(di_eq)
 #    di_eq_unittest.test_list_output_for_error()



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
    combine_magic.unittest_file()
#    combine_magic_unittest = Bad_test(combine_magic)
 #   combine_magic_unittest.test_file_for_error()
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

def complete_pt_rot_test(): # Irregular type.  has both an -ff and an -f option.  testing both here. 
     pt_rot = Test_instance('pt_rot.py', 'pt_rot_example.dat', 'pt_rot_results_new.out', 'pt_rot_results_correct.out', 'pt_rot_results_incorrect.out', None, True)
     pt_rot.file_in_file_out_sequence()
     # then, testing the -ff option
     input_1 = 'pt_rot_extra_in_nam_180-200.txt'
     input_2 = 'pt_rot_extra_in_nam_panA.frp'
     pt_rot_extra_outfile = 'pt_rot_extra_out.out'
     pt_rot_extra_reference = 'pt_rot_extra_correct.out'
     pt_rot_extra_wrong ='pt_rot_results_incorrect.out'
     pt_rot_extra = Test_instance('pt_rot.py', None, pt_rot_extra_outfile, pt_rot_extra_reference, pt_rot_extra_wrong, None, True, '-ff', input_1, input_2)
     print "Testing pt_rot.py with -ff option"
     obj = env.run('pt_rot.py', '-WD', '/Users/nebula/Python/Basic_input_output/', '-ff', input_1, input_2 , '-F', pt_rot_extra_outfile)
     pt_rot_extra.check_file_output(pt_rot_extra.outfile, pt_rot_extra.ref_out)
     pt_rot_extra_unittest = Bad_test(pt_rot_extra)
     pt_rot_extra_unittest.test_file_for_error()


     


def complete_customize_criteria_test():  # BIO type
    customize_criteria_infile = 'customize_criteria_example.dat'
    customize_criteria_output = 'customize_criteria_outfile.out'
    customize_criteria_reference = "customize_criteria_output_correct.out"
    customize_criteria_wrong = "customize_criteria_output_incorrect.out"
    customize_criteria = Test_instance('customize_criteria.py', customize_criteria_infile, customize_criteria_output, customize_criteria_reference, customize_criteria_wrong, '1', False)
    customize_criteria.file_in_file_out_sequence(interactive=True)
#    customize_criteria_unittest = Bad_test(customize_criteria)
 #   customize_criteria_unittest.test_file_for_error()




grab_magic_key_reference_list = ['42.60264', '42.60264', '42.60352', '42.60104', '42.73656', '42.8418', '42.8657', '42.92031', '42.56857', '42.49964', '42.49962', '42.50001', '42.52872', '42.45559', '42.48923', '42.46186', '42.69156', '42.65289', '43.30504', '43.36817', '43.42133', '43.8859', '43.84273', '43.53289', '43.57494', '44.15663', '44.18629']

def complete_grab_magic_key_test(): # List type
    print "Testing grab magic"
    grab_magic_key_infile = 'grab_magic_key_er_sites.txt'
    grab_magic_key_outfile = None
    grab_magic_key_wrong = "wrong"
    grab_magic_key_reference = grab_magic_key_reference_list
    grab_magic_key = Test_instance('grab_magic_key.py', grab_magic_key_infile, grab_magic_key_outfile, grab_magic_key_reference, grab_magic_key_wrong, None, True, '-key', 'site_lat')
    grab_magic_key.list_sequence()
    print "Sucessfully finished complete_grab_magic_key_test"


def complete_incfish_test(): # BIO type
    incfish_infile = 'incfish_example_inc.dat'
    incfish_outfile = 'incfish_results_new.out'
    incfish_reference = 'incfish_results_correct.out'
    incfish_wrong = 'incfish_results_incorrect.out'
    incfish = Test_instance('incfish.py', incfish_infile, incfish_outfile, incfish_reference, incfish_wrong, None, False)
    incfish.file_in_file_out_sequence()
#    incfish_unittest = Bad_test(incfish)
 #   incfish_unittest.test_file_for_error()
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
     print "Successfully completed nrm_specimens_magic.py tests"

def complete_sundec_test(): # list type
     sundec_infile = 'sundec_example.dat'
     sundec_outfile = None
     sundec_reference = ['154.2']
     sundec_wrong = ['154.3']
     sundec = Test_instance('sundec.py', sundec_infile, sundec_outfile, sundec_reference, sundec_wrong, None, False)
     sundec.run_program()
     sundec.list_sequence()
     print "Successfully finished sundec.py tests"

def complete_pca_test(): # list type
     pca_infile = 'pca_example.dat'
     pca_outfile = None
     pca_reference = pca_correct_out
     pca_wrong = ['eba24a', 'wrong']
     pca = Test_instance('pca.py', pca_infile, pca_outfile, pca_reference, pca_wrong, None, False, '-dir', 'L', '1', '10')
#     pca.run_program(output_type="list")
     pca.list_sequence()

pca_correct_out = ['eba24a', 'DE-BFL', '0', '0.00', '339.9', '57.9', '9.2830e-05', '1', '2.50', '325.7', '49.1', '7.5820e-05', '2', '5.00', '321.3', '45.9', '6.2920e-05', '3', '10.00', '314.8', '41.7', '5.2090e-05', '4', '15.00', '310.3', '38.7', '4.4550e-05', '5', '20.00', '305.0', '37.0', '3.9540e-05', '6', '30.00', '303.9', '34.7', '3.2570e-05', '7', '40.00', '303.0', '32.3', '2.5670e-05', '8', '50.00', '303.6', '32.4', '2.2520e-05', '9', '60.00', '299.8', '30.8', '1.9820e-05', '10', '70.00', '292.5', '31.0', '1.3890e-05', '11', '80.00', '297.0', '25.6', '1.2570e-05', '12', '90.00', '299.3', '11.3', '0.5030e-05', 'eba24a', 'DE-BFL', '10', '2.50', '70.00', '8.8', '334.9', '51.5']


def complete_scalc_test(): # irregular, & list type
     scalc_infile = 'scalc_example.txt'
     scalc_outfile = None
     scalc_reference = ['99', '19.5', '90.0']
     scalc_wrong = ['99', '19.5', '90.1']
     scalc = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference, scalc_wrong, None, False)
     scalc.list_sequence()
     # testing addition command line options
     scalc_reference2 = ["89", "15.2", "32.3"]
     scalc2 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference2, scalc_wrong, None, False, '-v')
     scalc2.list_sequence()
     #
     scalc_reference3 = ["100" ,"21.1", "90.0"]
     scalc3 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference3, scalc_wrong, None, False, '-a')
     scalc3.list_sequence()
     #
     scalc_reference4 = ["99", "19.8", "90.0"]
     scalc4 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference4, scalc_wrong, None, False, '-p')
     scalc4.list_sequence()
     # 
     scalc_reference5 = ["100", "21.1", "180.0"] 
     scalc5 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference5, scalc_wrong, None, False, '-C')
     scalc5.list_sequence()
     #
     scalc_reference6 = ["71", "10.9", "20.0"]
     scalc6 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference6, scalc_wrong, None, False, '-c', '20')
     scalc6.list_sequence()
     #
     scalc_reference7 = ["90", "15.9", "33.6"]
     scalc7 = Test_instance('scalc.py', scalc_infile, scalc_outfile, scalc_reference7, scalc_wrong, None, False, '-p', '-C', '-v', '-a', '-c', '20')
     scalc7.list_sequence()

def complete_scalc_magic_test():
     scalc_magic_infile = 'scalc_magic_example.txt'
     scalc_magic_outfile = None
     scalc_magic_reference = ['13', '17.8', '90.0']
     scalc_magic_wrong = [1, 2, 3, 4]
     scalc_magic = Test_instance('scalc_magic.py', scalc_magic_infile, scalc_magic_outfile, scalc_magic_reference, scalc_magic_wrong, None, False)
     scalc_magic.list_sequence()
     # not testing every single option because they are essentially the same as scalc.py above
     scalc_magic_reference2 = ['21','16.8','35.3']
     scalc_magic2 = Test_instance('scalc_magic.py', scalc_magic_infile, scalc_magic_outfile, scalc_magic_reference2, scalc_magic_wrong, None, False, '-p', '-C', '-v', '-a', '-c', '20')
     scalc_magic2.list_sequence()



def complete_s_hext_test(): # list type
     s_hext_infile = "s_hext_example.dat"
     s_hext_outfile = None
     s_hext_reference = s_hext_correct
     s_hext_wrong = ["wrong", "wronger"]
     s_hext = Test_instance('s_hext.py', s_hext_infile, s_hext_outfile, s_hext_reference, s_hext_wrong, None, False)
     s_hext.list_sequence()


s_hext_correct = ['F', '=', '2.56', 'F12', '=', '1.12', 'F23', '=', '2.16', 'N', '=', '8', 'sigma', '=', '0.000815076759', '0.33471', '265.8', '17.6', '40.3', '93.0', '72.2', '19.6', '356.5', '2.1', '0.33349', '93.0', '72.2', '31.4', '356.5', '2.1', '40.3', '265.8', '17.6', '0.33180', '356.5', '2.1', '19.6', '265.8', '17.6', '31.4', '93.0', '72.2']


def complete_vgp_di_test(): # list type
     vgp_di_infile = 'vgp_di_example.dat'
     vgp_di_outfile = None
     vgp_di_reference = ['335.6', '62.9']
     vgp_di_wrong = ['335.6', '20']
     vgp_di = Test_instance('vgp_di.py', vgp_di_infile, vgp_di_outfile, vgp_di_reference, vgp_di_wrong, None, False)
     vgp_di.list_sequence()


def complete_watsonsF_test(): # list/stdout type
     watsonsF_infile = "watsonsF_example_file1.dat"
     watsonsF_infile2 = file_prefix + "watsonsF_example_file2.dat"
     watsonsF_outfile = None
     watsonsF_reference = ["5.23074427567", "3.2594"]
     watsonsF_wrong = ["5.23074427567", "3.2394"]
     watsonsF = Test_instance('watsonsF.py', watsonsF_infile, watsonsF_outfile, watsonsF_reference, watsonsF_wrong, None, False, '-f2', watsonsF_infile2)
     watsonsF.list_sequence()





# BIO ones

def complete_apwp_test():
    apwp = Test_instance('apwp.py', 'apwp_example.dat', 'apwp_results_new.out', 'apwp_results_correct.out', 'apwp_results_incorrect.out', None, False)
    apwp.file_in_file_out_sequence(interactive=True)

def complete_b_vdm_test():
    b_vdm = Test_instance('b_vdm.py', 'b_vdm_example.dat', 'b_vdm_results_new.out', 'b_vdm_results_correct.out', 'b_vdm_results_incorrect.out', None, False)
    b_vdm.file_in_file_out_sequence(interactive=True)

def complete_cart_dir_test():
    cart_dir = Test_instance('cart_dir.py', 'cart_dir_example.dat', 'cart_dir_results_new.out', 'cart_dir_results_correct.out', 'cart_dir_results_incorrect.out', None, False)
    cart_dir.file_in_file_out_sequence(interactive=True)
    
def complete_convert_samples_test():
    convert_samples = Test_instance('convert_samples.py', 'convert_samples_example.dat', 'convert_samples_Northern_Iceland.txt', 'convert_samples_results_correct.out', 'convert_samples_results_incorrect.out', None, False)
    convert_samples.file_in_file_out_sequence(interactive=True)

def complete_di_geo_test():
    di_geo = Test_instance('di_geo.py', 'di_geo_example.dat', 'di_geo_results_new.out', 'di_geo_results_correct.out', 'di_geo_results_incorrect.out', None, False)
    di_geo.file_in_file_out_sequence(interactive=True)

def complete_di_tilt_test():
    di_tilt = Test_instance('di_tilt.py', 'di_tilt_example.dat', 'di_tilt_results_new.out', 'di_tilt_results_correct.out', 'di_tilt_results_incorrect.out', None, False)
    di_tilt.file_in_file_out_sequence(interactive=True)

def complete_dir_cart_test():
    dir_cart = Test_instance('dir_cart.py', 'dir_cart_example.dat', 'dir_cart_results_new.out', 'dir_cart_results_correct.out', 'dir_cart_results_incorrect.out', None, False)
    dir_cart.file_in_file_out_sequence(interactive=True)

def complete_di_rot_test():
    di_rot = Test_instance('di_rot.py', 'di_rot_example.dat', 'di_rot_results_new.out', 'di_rot_results_correct.out', 'di_rot_results_incorrect.out', None, False)
    di_rot.file_in_file_out_sequence()

def complete_di_vgp_test():
    di_vgp = Test_instance('di_vgp.py', 'di_vgp_example.dat', 'di_vgp_results_new.out', 'di_vgp_results_correct.out', 'di_vgp_results_incorrect.out', None, False)
    di_vgp.file_in_file_out_sequence(interactive=True)

def complete_eigs_s_test():
    eigs_s = Test_instance('eigs_s.py', 'eigs_s_example.dat', 'eigs_s_results_new.out', 'eigs_s_results_correct.out', 'eigs_s_results_incorrect.out', None, False)
    eigs_s.file_in_file_out_sequence()

def complete_eq_di_test():
    eq_di = Test_instance('eq_di.py', 'eq_di_example.dat', 'eq_di_results_new.out', 'eq_di_results_correct.out', 'eq_di_results_incorrect.out', None, False)
    # no interactive                                                                                                                 
    eq_di.file_in_file_out_sequence()

def complete_gobing_test():
    gobing = Test_instance('gobing.py', 'gobing_example.out', 'gobing_results_new.out', 'gobing_results_correct.out', 'gobing_results_incorrect.out', None, False)
    gobing.file_in_file_out_sequence()

def complete_gofish_test():
    gofish = Test_instance('gofish.py', 'gofish_example.out', 'gofish_results_new.out', 'gofish_results_correct.out', 'gofish_results_incorrect.out', None, False)
    gofish.file_in_file_out_sequence()

def complete_gokent_test():
    gokent = Test_instance('gokent.py', 'gokent_example.out', 'gokent_results_new.out', 'gokent_results_correct.out', 'gokent_results_incorrect.out', None, False)
    gokent.file_in_file_out_sequence()
    # no interactive  

def complete_goprinc_test():
    goprinc = Test_instance('goprinc.py', 'goprinc_example.dat', 'goprinc_results_new.out', 'goprinc_results_correct.out', 'goprinc_results_incorrect.out', None, False)
    goprinc.file_in_file_out_sequence()

def complete_igrf_test():
# this guy also has command line options, including a plotting one.  possibly it should get some more/different stuff.               
    igrf = Test_instance('igrf.py', 'igrf_example.dat', 'igrf_results_new.out', 'igrf_results_correct.out', 'igrf_results_incorrect.out', None, False)
    igrf.file_in_file_out_sequence(interactive=True)


def complete_k15_s_test():
    # this guy has one additional command line option.  i wonder if it needs to be tested??                                          
    k15_s = Test_instance('k15_s.py', 'k15_s_example.dat', 'k15_s_results_new.out', 'k15_s_results_correct.out', 'k15_s_results_incorrect.out', None, False)
    k15_s.file_in_file_out_sequence()

def complete_mk_redo_test():
    mk_redo = Test_instance('mk_redo.py', 'pmag_specimens.txt', 'mk_redo_results_new.out', 'mk_redo_results_correct.out', 'mk_redo_results_incorrect.out', None, True)
    mk_redo.file_in_file_out_sequence()

def complete_s_eigs_test():
    s_eigs = Test_instance('s_eigs.py', 's_eigs_example.dat', 's_eigs_results_new.out', 's_eigs_results_correct.out', 's_eigs_results_incorrect.out', None, False)
    s_eigs.file_in_file_out_sequence()

def complete_s_geo_test():
    s_geo = Test_instance('s_geo.py', 's_geo_example.dat', 's_geo_results_new.out', 's_geo_results_correct.out', 's_geo_results_incorrect.out', None, False)
    s_geo.file_in_file_out_sequence()

def complete_s_tilt_test():
    s_tilt = Test_instance('s_tilt.py', 's_tilt_example.dat', 's_tilt_results_new.out', 's_tilt_results_correct.out', 's_tilt_results_incorrect.out', None, False)
    s_tilt.file_in_file_out_sequence()

def complete_stats_test():
    stats = Test_instance('stats.py', 'stats_example.dat', 'stats_results_new.out', 'stats_results_correct.out', 'stats_results_incorrect.out', None, False)
    stats.file_in_file_out_sequence()

def complete_vdm_b_test():
    vdm_b = Test_instance('vdm_b.py', 'vdm_b_example.dat', 'vdm_b_results_new.out', 'vdm_b_results_correct.out', 'vdm_b_results_incorrect.out', None, False)
    vdm_b.file_in_file_out_sequence(interactive=True)


def complete_vector_mean_test():
     infile = "vector_mean_example.dat"
     outfile = "vector_mean_results_new.out"
     reference = "vector_mean_results_correct.out"
     wrong = "vector_mean_results_incorrect.out"
     vector_mean = Test_instance('vector_mean.py', infile, outfile, reference, wrong, None, False)
     vector_mean.file_in_file_out_sequence()
     obj = env.run('vector_mean.py', '-f', file_prefix + infile)
     print obj.stdout



# end of BIO section : ) 

# beginning of Plotting section

def complete_ani_depthplot_test():
     print "Testing ani_depthplot.py"
     ani_depthplot_infile = 'ani_depthplot_rmag_anisotropy.txt'
     ani_depthplot_outfile = None
     ani_depthplot_reference = "{'U1359A_ani-depthplot.svg': <FoundFile ./new-test-output:U1359A_ani-depthplot.svg>}"
     ani_depthplot_wrong = "No way"
     ani_depthplot_fsa = 'ani_depthplot_er_samples.txt'
     ani_depthplot = Test_instance('ani_depthplot.py', ani_depthplot_infile, ani_depthplot_outfile, ani_depthplot_reference, ani_depthplot_wrong, 'a', True, '-fsa', ani_depthplot_fsa)
     ani_depthplot.plot_program_sequence(stdout=False)

def complete_basemap_magic_test():
     basemap_magic_infile = 'basemap_example.txt'
     basemap_magic_outfile = None
     basemap_magic_reference = "{'Site_map.pdf': <FoundFile ./new-test-output:Site_map.pdf>}"
     basemap_magic_wrong = "wrong"
     basemap_magic = Test_instance('basemap_magic.py', basemap_magic_infile, basemap_magic_outfile, basemap_magic_reference, basemap_magic_wrong, 'a', True)
     basemap_magic.plot_program_sequence(stdout=False)


def complete_biplot_magic_test():
     biplot_magic_infile = 'biplot_magic_example.dat'
     biplot_magic_outfile = None
     biplot_magic_reference = """LP-X  selected for X axis
LT-AF-I  selected for Y axis
All
measurement_magn_mass  being used for plotting Y
measurement_chi_mass  being used for plotting X.
S[a]ve plots, [q]uit,  Return for next plot """
     biplot_magic_wrong = 1235.
     biplot_magic = Test_instance('biplot_magic.py', biplot_magic_infile, biplot_magic_outfile, biplot_magic_reference, biplot_magic_wrong, 'q', False, '-x', 'LP-X', '-y', 'LT-AF-I')
     biplot_magic.plot_program_sequence(stdout=True)


def complete_chi_magic_test():
     chi_magic_infile = 'chi_magic_example.dat'
     chi_magic_outfile = None
     chi_magic_reference = "{'IRM-OldBlue-1892_2.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_2.svg>, 'IRM-OldBlue-1892_3.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_3.svg>, 'IRM-OldBlue-1892_1.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_1.svg>}"
     chi_magic_wrong = "wrong"
     chi_magic = Test_instance('chi_magic.py', chi_magic_infile, chi_magic_outfile, chi_magic_reference, chi_magic_wrong, 'a', False)
     chi_magic.plot_program_sequence(stdout=False)



def complete_common_mean_test(): # Irregular type: a little fanciness after the standard stuff
     common_mean_infile = 'common_mean_ex_file1.dat'
     common_mean_outfile = None
     common_mean_reference = "{'CD_X.svg': <FoundFile ./new-test-output:CD_X.svg>, 'CD_Y.svg': <FoundFile ./new-test-output:CD_Y.svg>, 'CD_Z.svg': <FoundFile ./new-test-output:CD_Z.svg>}"
     common_mean_wrong = "wrong"
     common_mean_f2 = file_prefix + 'common_mean_ex_file2.dat'
     common_mean = Test_instance('common_mean.py', common_mean_infile, common_mean_outfile, common_mean_reference, common_mean_wrong, 'a', False, '-f2', common_mean_f2)
     common_mean.plot_program_sequence(stdout=False)
     # testing with -dir option
     common_mean_2 = Test_instance('common_mean.py', common_mean_infile, common_mean_outfile, common_mean_reference, common_mean_wrong, 'a', False, '-dir', '0', '9.9')
     obj = env.run('common_mean.py', '-f', file_prefix + common_mean_infile, '-f2', common_mean_f2)
     if obj.files_updated:
          print "Successfully updated file"
     else:
          raise NameError("common_mean.py with -dir option did not update plots")

def complete_core_depthplot_test():
     core_depthplot_infile = 'core_depthplot_example.dat'
     core_depthplot_outfile = None
     core_depthplot_reference = "{'DSDP Site 522_m:_LT-AF-Z_core-depthplot.svg': <FoundFile ./new-test-output:DSDP Site 522_m:_LT-AF-Z_core-depthplot.svg>}"
     core_depthplot_wrong = "wrong"
     core_depthplot_fsa = 'core_depthplot_er_samples.txt'
     core_depthplot = Test_instance('core_depthplot.py', core_depthplot_infile, core_depthplot_outfile, core_depthplot_reference, core_depthplot_wrong, 'a', True, '-fsa', core_depthplot_fsa, '-LP', 'AF', '15')
     core_depthplot.plot_program_sequence(stdout=False)


def complete_dayplot_magic_test():
     dayplot_magic_infile = 'dayplot_magic_example.dat'
     dayplot_magic_outfile = None
     dayplot_magic_reference = "{'LO:_unknown_SI:__SA:__SP:__TY:_day_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_day_.svg>, 'LO:_unknown_SI:__SA:__SP:__TY:_S-Bc_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_S-Bc_.svg>, 'LO:_unknown_SI:__SA:__SP:__TY:_S-Bcr_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_S-Bcr_.svg>}"
     dayplot_magic_wrong = "wrong"
     dayplot_magic = Test_instance('dayplot_magic.py', dayplot_magic_infile, dayplot_magic_outfile, dayplot_magic_reference, dayplot_magic_wrong, 'a', True)
     dayplot_magic.plot_program_sequence(stdout=False)

def complete_dmag_magic_test():
     dmag_magic_infile = 'dmag_magic_example.dat'
     dmag_magic_outfile = None
     dmag_magic_reference = "{'McMurdo_LT-AF-Z.svg': <FoundFile ./new-test-output:McMurdo_LT-AF-Z.svg>}"
     dmag_magic_wrong = "wrong"
     dmag_magic = Test_instance('dmag_magic.py', dmag_magic_infile, dmag_magic_outfile, dmag_magic_reference, dmag_magic_wrong, 'a', False)
     dmag_magic.plot_program_sequence(stdout=False)

def complete_eqarea_test():
     eqarea_infile = 'eqarea_example.dat'
     eqarea_outfile = None
     eqarea_reference = "{'eq.svg': <FoundFile ./new-test-output:eq.svg>}"
     eqarea_wrong = "wrong"
     eqarea = Test_instance('eqarea.py', eqarea_infile, eqarea_outfile, eqarea_reference, eqarea_wrong, 'a', False)
     eqarea.plot_program_sequence(stdout=False)

def complete_eqarea_ell_test():
     eqarea_ell_infile = 'eqarea_ell_example.dat'
     eqarea_ell_outfile = None
     eqarea_ell_reference = """Zdec   137.8
     Edec   235.4
     Eta     2.9
     n        100
     Einc    17.7
     Zinc    22.6
     Zeta     2.1
     dec     0.0
     inc    60.7
 S[a]ve to save plot, [q]uit, Return to continue:"""
     eqarea_ell_wrong = "wrong"
     eqarea_ell = Test_instance('eqarea_ell.py', eqarea_ell_infile, eqarea_ell_outfile, eqarea_ell_reference, eqarea_ell_wrong, 'q', False, '-ell', 'B')
     eqarea_ell.plot_program_sequence(stdout=True)



def complete_fishqq_test(): # irregular type, because it produces a useful outfile as well as a plot
     fishqq_infile = 'fishqq_example.dat'
     fishqq_outfile = 'fishqq_results_new.out'
     fishqq_reference = "{'exp1.svg': <FoundFile ./new-test-output:exp1.svg>, 'unf1.svg': <FoundFile ./new-test-output:unf1.svg>}"
     fishqq_file_reference = 'fishqq_results_correct.out'
     fishqq_wrong = "wrong"
     fishqq = Test_instance('fishqq.py', fishqq_infile, fishqq_outfile, fishqq_reference, fishqq_wrong, 'a', False)
     fishqq.plot_program_sequence(stdout=False)
     fishqq.check_file_output(fishqq.outfile, fishqq_file_reference)


def complete_foldtest_magic_test(): # Irregular: has potential for bootstrapping.  I'm just not sure if I should simply test the file out instead
     foldtest_magic_infile = 'foldtest_magic_example.txt'
     foldtest_magic_outfile = 'foldtest_magic_results_new.out'
     foldtest_magic_reference = "{'foldtest_ge.svg': <FoundFile ./new-test-output:foldtest_ge.svg>, 'foldtest_st.svg': <FoundFile ./new-test-output:foldtest_st.svg>, 'foldtest_ta.svg': <FoundFile ./new-test-output:foldtest_ta.svg>}"
     foldtest_magic_wrong = [1, 2, 3]
     foldtest_magic_fsa = 'foldtest_magic_er_samples.txt'
     foldtest_magic = Test_instance('foldtest_magic.py', foldtest_magic_infile, foldtest_magic_outfile, foldtest_magic_reference, foldtest_magic_wrong, 'a', True,  '-fsa', foldtest_magic_fsa, '-n', '100')
     foldtest_magic.plot_program_sequence(stdout=False)


def complete_foldtest_test(): # irregular?  may be boostrap-y
    # doesn't produce stdout :(                                                                                 
     print"Testing foldtest.py"
     foldtest_infile = 'foldtest_example.dat'
     foldtest_outfile = 'foldtest_results_new.out'
     foldtest_reference = """{'foldtest_ge.svg': <FoundFile ./new-test-output:foldtest_ge.svg>, 'foldtest_st.svg': <FoundFile ./new-test-output:foldtest_st.svg>, 'foldtest_ta.svg': <FoundFile ./new-test-output:foldtest_ta.svg>}"""
     foldtest_wrong = "wrong"
     foldtest = Test_instance('foldtest.py', foldtest_infile, foldtest_outfile, foldtest_reference, foldtest_wrong, 'a', False, '-n', 50)
     foldtest.plot_program_sequence(stdout=False)

def complete_histplot_test():
     print"Testing histplot.py"
     histplot_infile = 'extra_histplot_sample.out'
     histplot_outfile = None
     histplot_reference = "{'hist.svg': <FoundFile ./new-test-output:hist.svg>}"
     histplot_wrong = "wrong"
     histplot = Test_instance('histplot.py', histplot_infile, histplot_outfile, histplot_reference, histplot_wrong, 'a', False)
     histplot.plot_program_sequence(stdout=False)


def complete_irmaq_magic_test():
     print"Testing irmaq_magic.py"
     irmaq_magic_infile = 'irmaq_magic_measurements.txt'
     irmaq_magic_outfile = None
     irmaq_magic_reference = "{'U1359A_LP-IRM.svg': <FoundFile ./new-test-output:U1359A_LP-IRM.svg>}"
     irmaq_magic_wrong = 8
     irmaq_magic = Test_instance('irmaq_magic.py', irmaq_magic_infile, irmaq_magic_outfile, irmaq_magic_reference, irmaq_magic_wrong, 'a', True)
     irmaq_magic.plot_program_sequence(stdout=False)


def complete_lnp_magic_test(): # irregular type.  it had to be written the long way, because it won't run with -F.  
     print"Testing lnp_magic.py"
     lnp_magic_infile = 'lnp_magic_pmag_specimens.txt'
     lnp_magic_outfile = None
     lnp_magic_reference = PmagPy_tests.file_parse_by_word(file_prefix + 'lnp_magic_output_correct.txt')
     lnp_magic_wrong = ['sv01', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'I am not right']
     lnp_magic = Test_instance('lnp_magic.py', lnp_magic_infile, lnp_magic_outfile, lnp_magic_reference, lnp_magic_wrong, None, True, '-crd', 'g', '-P')
     obj = env.run('lnp_magic.py', '-WD', '/Users/nebula/Python/Basic_input_output', '-f', 'lnp_magic_pmag_specimens.txt', '-crd', 'g', '-P')
     result = str(obj.stdout).split()
     lnp_magic.test_help()
     lnp_magic.check_list_output(result, lnp_magic.ref_out)
     lnp_magic.unittest_list()



def complete_lowrie_test():
    # doesn't produce stdout : (
     print "Testing lowrie.py"
     lowrie_infile = 'lowrie_example.dat'
     lowrie_outfile = None
     lowrie_reference = """318-U1359A-002H-1-W-109
S[a]ve figure? [q]uit, <return> to continue"""
     lowrie_wrong = "wrong"
     lowrie = Test_instance('lowrie.py', lowrie_infile, lowrie_outfile, lowrie_reference, lowrie_wrong, 'q', False)
     lowrie.plot_program_sequence(stdout=True)

def complete_lowrie_magic_test():
     print "testing lowrie_magic.py"
     infile = 'lowrie_magic_example.dat'
     outfile = None
     reference = """318-U1359A-002H-1-W-109
S[a]ve figure? [q]uit, <return> to continue"""
     wrong = "1, 2, 3, 4"
     lowrie_magic = Test_instance('lowrie_magic.py', infile, outfile, reference, wrong, 'q', True)
     lowrie_magic.plot_program_sequence(stdout=True)


def complete_plot_cdf_test():
     print"Testing plot_cdf.py"
     infile =  "plot_cdf_example.dat"
     outfile = None
     reference = "{'CDF_.svg': <FoundFile ./new-test-output:CDF_.svg>}"
     wrong = "Not right"
     plot_cdf = Test_instance('plot_cdf.py', infile, outfile, reference, wrong, 'a', False)
     plot_cdf.plot_program_sequence(stdout=False)



def complete_plotdi_a_test():
    print "Testing plotdi_a.py"
    plotdi_a_infile = "plotdi_a_example.dat"
    plotdi_a_outfile = None
    plotdi_a_reference = "{'eq.svg': <FoundFile ./new-test-output:eq.svg>}"
    plotdi_a_wrong = ['1', 'one']
    plotdi_a = Test_instance('plotdi_a.py', plotdi_a_infile, plotdi_a_outfile, plotdi_a_reference, plotdi_a_wrong, 'a', False)
    plotdi_a.plot_program_sequence(stdout=False)


def complete_plotxy_test():
     plotxy_infile = 'plotxy_example.dat'
     plotxy_outfile = None
     plotxy_reference = "{'plotXY.svg': <FoundFile ./new-test-output:plotXY.svg>}"
     plotxy_wrong = ["something", 2]
     plotxy = Test_instance('plotxy.py', plotxy_infile, plotxy_outfile, plotxy_reference, plotxy_wrong, 'a', False, '-l')
     plotxy.plot_program_sequence(stdout=False)


def complete_qqplot_test():# irregular type.  produces a lot of output, which is then parsed out.  
    qqplot_infile = "qqplot_example.dat"
    qqplot_outfile = None
    qqplot_reference_output = [10.12243251, 2.79670530387, 0.0558584072909, 0.0886]
    qqplot_wrong_output = [10.12243251, 2., 0., 0.]
    qqplot = Test_instance('qqplot.py', qqplot_infile, qqplot_outfile, qqplot_reference_output, qqplot_wrong_output, 'a', False)
    qqplot_output = qqplot.run_program(output_type='stdout')
    qqplot_list_out = str(qqplot_output).split()
    qqplot_clean_out = []
    for num, i in enumerate(qqplot_list_out): # isolates the relevant numbers for testing
        print num
        print i
        if str(i) == '1':  # this prevents the 1 from "1 plot saved" being put into the array of answers
             pass
        else:
            try:
                qqplot_clean_out.append(float(i))
                print qqplot_clean_out
            except ValueError:
                pass
    qqplot.check_output(qqplot_clean_out, qqplot.ref_out)
    qqplot.test_help()
    qqplot.unittest_list()


def complete_quick_hyst_test():
    quick_hyst_infile = 'quick_hyst_example.dat'
    quick_hyst_outfile = None
    quick_hyst_reference = """IS06a-1 1 out of  8
working on t:  273
S[a]ve plots, [s]pecimen name, [q]uit, <return> to continue
 Good bye"""
    quick_hyst_wrong = "wrong"
    quick_hyst = Test_instance('quick_hyst.py', quick_hyst_infile, quick_hyst_outfile, quick_hyst_reference, quick_hyst_wrong, 'q', True)
    quick_hyst.plot_program_sequence(stdout=True)


def complete_revtest_test():
     revtest_infile = 'revtest_example.dat'
     revtest_outfile = None
     revtest_reference = "{'REV_Z.svg': <FoundFile ./new-test-output:REV_Z.svg>, 'REV_Y.svg': <FoundFile ./new-test-output:REV_Y.svg>, 'REV_X.svg': <FoundFile ./new-test-output:REV_X.svg>}"
     revtest_wrong = "not right"
     revtest = Test_instance('revtest.py', revtest_infile, revtest_outfile, revtest_reference, revtest_wrong, 'a', False)
     revtest.plot_program_sequence(stdout=False)



def complete_site_edit_magic_test():
    site_edit_magic_reference = """sr01
specimen, dec, inc, n_meas/MAD,| method codes 
sr01a1:   331.0    64.5 9 / 1.8 | LP-DIR-T:DE-BFL
sr01a2:   325.9    62.1 10 / 0.9 | LP-DIR-T:DE-BFL
sr01c2:   345.0    64.3 9 / 3.0 | LP-DIR-T:DE-BFL
sr01d1:   327.0    65.2 10 / 1.9 | LP-DIR-T:DE-BFL
sr01e2:   332.9    67.0 10 / 1.9 | LP-DIR-AF:DE-BFL
sr01f2:   325.9    66.1 15 / 1.6 | LP-DIR-T:DE-BFL
sr01g2:   324.3    66.7 10 / 2.6 | LP-DIR-AF:DE-BFL
sr01i1:   328.5    62.5 9 / 2.8 | LP-DIR-T:DE-BFL

 Site lines planes  kappa   a95   dec   inc
sr01 8  0     574      2.3    330.1     64.9  7.9878 
s[a]ve plot, [q]uit, [e]dit specimens, <return> to continue:"""
    site_edit_magic_wrong = "wrong"
    site_edit_magic_infile = 'site_edit_example.dat'
    site_edit_fsa = 'site_edit_er_samples.txt'
    site_edit_magic_outfile = None
    site_edit = Test_instance('site_edit_magic.py', site_edit_magic_infile, site_edit_magic_outfile, site_edit_magic_reference, site_edit_magic_wrong, 'q', True, '-fsa', site_edit_fsa)
    site_edit.plot_program_sequence(stdout=True)

def complete_strip_magic_test():
     strip_magic_infile = 'strip_magic_example.txt'
     strip_magic_outfile = None
     strip_magic_reference = "{'strat.svg': <FoundFile ./new-test-output:strat.svg>}"
     strip_magic_wrong = "hello there"
     strip_magic = Test_instance('strip_magic.py', strip_magic_infile, strip_magic_outfile, strip_magic_reference, strip_magic_wrong, 'a', True, '-x', 'age', '-y', 'lat')
     strip_magic.plot_program_sequence(stdout=False)
     

thellier_ref = """starting new specimen interpretation file:  thellier_specimens.txt
s1p1-01 1 of  269
index step Dec   Inc  Int       Gamma
0     0   320.7     2.2 6.280e-07 
1     100   323.0     2.3 6.380e-07    22.2
2     200   322.9     1.4 5.850e-07     6.2
3     300   322.7     2.0 4.690e-07     3.7
4     325   321.4     1.0 3.950e-07     8.5
5     350   322.8     1.6 3.690e-07     5.2
6     375   322.9     0.7 3.420e-07     5.5
7     400   323.1     1.2 3.250e-07     8.3
8     425   323.6    -0.1 2.890e-07     4.3
9     450   323.6     1.2 2.580e-07     4.6
10     475   323.7    -0.8 2.200e-07     6.8
11     500   322.7     1.0 1.720e-07     6.9
12     510   322.2    -1.1 1.480e-07     4.4
13     520   322.3    -0.1 1.230e-07     3.2
14     530   322.2    -4.8 8.580e-08     5.8
15     540   323.8    -0.9 6.250e-08     5.9
16     550   323.6    -4.9 4.370e-08     4.2
17     560   322.1    -2.5 3.240e-08     4.9
Looking up saved interpretation....
    None found :(  

               s[a]ve plot, set [b]ounds for calculation, [d]elete current interpretation, [p]revious, [s]ample, [q]uit:
               
Return for next specimen """


def complete_thellier_magic_test(): # Irregular, and imperfect.  fix??
    thellier_magic_infile = 'thellier_magic_measurements.txt'
    thellier_magic_reference = PmagPy_tests.file_parse_by_word('thellier_magic_output_correct.out')# this is in a file because it is irritatingly long to keep in the document.  I've left it above, for now.  
    print thellier_magic_reference
    thellier_magic_outfile = None
    thellier_magic_wrong = "wrong"
    thellier_magic = Test_instance('thellier_magic.py', thellier_magic_infile, thellier_magic_outfile, thellier_magic_reference, thellier_magic_wrong,  'q', False)
    thellier_magic.list_sequence()


def complete_vgpmap_magic_test():
    vgpmap_magic_infile = 'vgpmap_magic_pmag_results.txt'
    vgpmap_magic_outfile = None
    vgpmap_magic_reference = "{'VGP_map.pdf': <FoundFile ./new-test-output:VGP_map.pdf>}"
    vgpmap_magic_wrong = "wrong"
    vgpmap_magic = Test_instance('vgpmap_magic.py', vgpmap_magic_infile, vgpmap_magic_outfile, vgpmap_magic_reference, vgpmap_magic_wrong, 'a', True, '-prj', 'ortho', '-eye', '60', '0')
    vgpmap_magic.plot_program_sequence(stdout=False)
#    obj = env.run('vgpmap_magic.py', '-WD', directory, '-f', vgpmap_magic_infile, '-crd', 'g', '-prj', 'ortho', '-eye', '60', '0', '-sym', 'ko', '10', '-fmt', 'png', stdin='a') 

zeq_magic_reference = """sr01a1 0 out of  177
    looking up previous interpretations...
g: 0      0.0  C  4.065e-05   324.1    66.0 
g: 1    100.0  C  3.943e-05   330.5    64.6 
g: 2    150.0  C  3.908e-05   324.9    65.5 
g: 3    200.0  C  3.867e-05   329.4    64.6 
g: 4    250.0  C  3.797e-05   330.3    64.5 
g: 5    300.0  C  3.627e-05   330.1    64.0 
g: 6    350.0  C  3.398e-05   327.0    64.4 
g: 7    400.0  C  2.876e-05   328.2    64.0 
g: 8    450.0  C  2.148e-05   323.8    65.2 
g: 9    500.0  C  1.704e-05   326.0    63.9 
g: 10    525.0  C  1.200e-05   326.5    63.7 
g: 11    550.0  C  5.619e-06   325.5    64.4 

                g/b: indicates  good/bad measurement.  "bad" measurements excluded from calculation

                 set s[a]ve plot, [b]ounds for pca and calculate, [p]revious, [s]pecimen, 
                 change [h]orizontal projection angle,   change [c]oordinate systems, 
                 [d]elete current interpretation(s), [e]dit data,   [q]uit: 
                
<Return>  for  next specimen 
Good bye"""

def complete_zeq_magic_test(): # NOT SURE THIS IS ACTUALLY USEFUL.  Consider
    zeq_magic_infile = 'zeq_magic_measurements.txt'
    zeq_magic_outfile = None
#    zeq_magic_reference = See above                                       
    zeq_magic_wrong = "wrong"
    fsa = 'zeq_magic_er_samples.txt'
    fsp = 'zeq_magic_specimens.txt'
    zeq_magic = Test_instance('zeq_magic.py', zeq_magic_infile, zeq_magic_outfile, zeq_magic_reference, zeq_magic_wrong, 'q', True, '-fsa', fsa, '-fsp', fsp, '-crd', 'g')
    zeq_magic.plot_program_sequence(stdout=True)
# could do the below, but it takes forever and creates a TON of files                                                          
#    extra_zeq_magic = Plot('zeq_magic.py', zeq_magic_infile, zeq_magic_reference, zeq_magic_wrong, None, True, '-fsa', fsa, '-fsp', fsp, '-sav')                                                          


def complete_zeq_magic_redo_test(): # BIO type
     zeq_redo_infile = 'zeq_magic_redo_measurements.txt'
     zeq_redo_outfile = 'zeq_magic_redo_results_new.out'
     zeq_redo_reference = 'zeq_magic_redo_results_correct.out'
     zeq_redo_wrong = 'zeq_magic_redo_results_incorrect.out'
     fre =  'zeq_magic_redo'
     fsa =  'zeq_magic_redo_er_samples.txt'
     zeq_magic_redo = Test_instance('zeq_magic_redo.py', zeq_redo_infile, zeq_redo_outfile, zeq_redo_reference, zeq_redo_wrong, None, True, '-fre', fre, '-fsa', fsa)
     zeq_magic_redo.file_in_file_out_sequence()




#"zeq_magic_redo.py -f zeq_magic_redo_measurements.txt -fre zeq_magic_redo -fsa zeq_magic_er_samples.txt -F zeq_magic_redo_results_new.out"


# Measurement import stuff
 
def complete_agm_magic_test():
     agm_magic_infile = 'agm_magic_example.agm'
     agm_magic_outfile = 'agm_magic_output.out'
     agm_magic_reference = 'agm_magic_output_correct.out'
     agm_magic_wrong = 'agm_magic_output_incorrect.out'
     agm = Test_instance('agm_magic.py', agm_magic_infile, agm_magic_outfile, agm_magic_reference, agm_magic_wrong, None, True, '-spn', 'myspec', '--usr', "Lima Tango", '-u', 'cgs')
     agm.file_in_file_out_sequence()
     extra_infile = 'agm_magic_example.irm'
     extra_outfile = 'agm_magic_irm_output.out'
     extra_reference = 'agm_magic_extra_output_correct.out'
     extra_wrong = 'agm_magic_extra_output_incorrect.out'
     extra_agm = Test_instance('agm_magic.py', extra_infile, extra_outfile, extra_reference, extra_wrong, None, True, '-spn', 'myspec', '--usr', "Lima Tango", '-bak')
     extra_agm.file_in_file_out_sequence()



def complete_upload_magic_test(): # irregular.  must be tested in a different directory. 
     obj = env.run("upload_magic.py", cwd=directory + "/upload_magic") # cwd allows specifying a directory other than the one you are in
     reference = "upload_magic/correct_upload.txt"
     wrong = "upload_magic/incorrect_upload.txt"
     upload_magic = Test_instance("upload_magic.py", None, None, reference, wrong, None, False) #, "cwd=" +str(directory))
     print obj.stdout
     upload_magic.test_help()
     upload_magic.check_file_output(file_prefix + "upload_magic/upload.txt", upload_magic.ref_out)
     subprocess.call(['rm', 'upload_magic/upload.txt'])



     

# UNFINISHED


def complete_revtest_magic_test():
     pass

def complete_working_test():
     # the examples
     complete_angle_test()
     complete_zeq_test()
     complete_chartmaker_test()
     complete_di_eq_test()
     # the UCs
     complete_combine_magic_test()
     complete_cont_rot_test()
     complete_customize_criteria_test()
     complete_grab_magic_key_test()
     complete_incfish_test()
#     complete_magic_select_test() NEEDS -WD!!!!!
     complete_nrm_specimens_magic_test()
     complete_sundec_test()
     complete_pca_test()
     complete_scalc_test()  # will probably also go in bootstrap-plotting
     complete_scalc_magic_test() # also in bootstrap_plotting
     complete_vgp_di_test()
     complete_watsonsF_test()
     # the BIOs
#     complete_apwp_test()
 #    complete_b_vdm_test()
#     complete_cart_dir_test()
#     complete_convert_samples_test()
 #    complete_di_geo_test()
#     complete_di_tilt_test()
#     complete_dir_cart_test()
#     complete_di_rot_test()
#     complete_di_vgp_test()
 #    complete_eigs_s_test()
#     complete_eq_di_test()
 #    complete_gobing_test()
#     complete_gofish_test()
 #    complete_gokent_test()
#     complete_goprinc_test()
 #    complete_igrf_test()
#     complete_k15_s_test()
 #    complete_mk_redo_test()
#     complete_pt_rot_test()
#     complete_s_eigs_test()
 #    complete_s_geo_test()
#     complete_s_tilt_test()
 #    complete_stats_test()
  #   complete_vdm_b_test()
#complete_vector_mean_test()
     complete_zeq_magic_redo_test()
     #PLOTTING
#     complete_ani_depthplot_test()
 #    complete_basemap_magic_test()
#     complete_biplot_magic_test()
#     complete_chi_magic_test()
#     complete_common_mean_test()
#     complete_core_depthplot_test()
#     complete_dayplot_magic_test()
#     complete_dmag_magic_test()
 #    complete_eqarea_test()
  #   complete_eqarea_ell_test()
     #complete_fishqq_test()
#     complete_foldtest_magic_test()
#     complete_foldtest_test()
#     complete_histplot_test()
 #    complete_irmaq_magic_test()
#     complete_lnp_magic_test()
 #    complete_lowrie_test()
#     complete_lowrie_magic_test()
#     complete_plot_cdf_test()
 #    complete_plotdi_a_test()
#     complete_plotxy_test()
  #   complete_qqplot_test()
   #  complete_quick_hyst_test()
#     complete_revtest_test() # NOT DONE
 #    complete_revtest_magic_test() # NOT DONE
#     complete_site_edit_magic_test()
 #    complete_strip_magic_test()
#     complete_s_hext_test()
#     complete_thellier_magic_test()
#     complete_vgpmap_magic_test()
#     complete_zeq_magic_test()
#     complete_agm_magic_test()
#complete_upload_magic_test()
  #   pass

if __name__ == '__main__':
     pass
#     complete_working_test()



