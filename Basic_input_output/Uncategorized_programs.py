#! /usr/bin/env python

import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Basic_input_output
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory = '/Users/nebula/Python/Basic_input_output'
# also, the fishrot.out is randomly created using fishrot.py, but since I'm using the same fishrot.out every time in the test, it shold be fine                                                                                                                            

"""
def sundec_test():
    in_file = file_prefix + 'sundec_example.dat'
    correct_out = '154.2'
    incorrect_out = '154.3'
    obj = env.run('sundec.py', '-f', in_file)
    output = str(obj.stdout)
    output = output.strip(" ")
    print output
    if correct_out in output and output[0] != "-":
        print "Sundec.py is producing correct output"
    else:
        print "Sundec.py output should have been: " + correct_out + " but instead produced: " + output
        raise(NameError, "Sundec.py produced incorrect output")
    test_help("sundec.py")
    print(env.run("sundec.py", '-i'))
    

sundec_test()

"""

def strip_and_string(string):
    string = str(string)
    string.strip(" ")
#    string.strip("\n")
    string.strip("u")
    return string


class UC(Basic_input_output.in_out):
    

# EITHER use this new __init__ function, or just have the expected output as an argument you put in.  or a dictionary at the bottom of the class, or some such thing
#    def __init__(self, name, input_file, expected_out):
 #       Basic_input_output.__init__(self)
    #    self.name = name
    #    self.input_file = input_file
  #      self.expected_out = expected_out


# this one tests what is essentially a BIO object, but producing stdout instead of an outfile
    def stdout_test(self, expected_out):
        name = self.name
        print "Running: " + str(name)
        if self.WD:
            obj = env.run(self.name, '-WD', file_prefix, '-f', self.input_file)
        else:
            obj = env.run(self.name, '-f', self.input_file)
        output = float(obj.stdout)
        expected_out = float(expected_out)
        print "Output: ", output
        print "Expected out: ", expected_out
        if output == expected_out:
            print "Output as expected"
        else:
            raise NameError(str(self.name) + " generated bad output")
            print "Output should have been " + expected_out + " but was " + output

# this does the same as above, but it uses a list instead of a simple float (longer output)
    def long_stdout_test(self, expected_out, arg1=None, arg2=None):
        # right now this is customized to grab_magic_key.py. Will have to be fixed for any other stuff
        # possibly could have extra args, for the -crd type options
        name = self.name
        print "Running: " + str(name)
        if self.WD:
            obj = env.run(self.name, '-WD', file_prefix, '-f', self.input_file, '-key', 'site_lat')
        else:
            obj = env.run(self.name, '-f', self.input_file)
        output = str(obj.stdout).split()
        print output
        if str(output) == str(expected_out):
            print str(self.name) + " is producing correct output"
        else:
            print "Error raised"
            print "Expected out: " + str(expected_out)
            print "Actual out: " + str(output)
            raise NameError(str(self.name) + " produced incorrect output")




class Bad_test(unittest.TestCase):
    def __init__(self, uc_obj):
        self.uc_obj = uc_obj

    def test_for_stdout_error(self, reference_data):
        #            self.assertRaises(NameError, angle.test_file, angle.incorrect_output_file)
        print "Testing: " + str(self.uc_obj.name) + " with incorrect reference data -- " + str(reference_data) + " -- expecting error"
        self.assertRaises(NameError, self.uc_obj.stdout_test, reference_data)
        print "-"

    def test_for_long_stdout_error(self, reference_data):
        print "Testing: " + str(self.uc_obj.name) + " with incorrect reference data -- " + str(reference_data) + " -- expecting error"
        self.assertRaises(NameError, self.uc_obj.long_stdout_test, reference_data)



nrm_specimens_magic = UC('nrm_specimens_magic.py', 'nrm_specimens_magic_measurements.txt', 'nrm_specimens_results_new.out', 'nrm_specimens_results_correct.out', 'nrm_specimens_results_incorrect.out')

sundec = UC('sundec.py', 'sundec_example.dat')
vgp_di = UC('vgp_di.py', 'vgp_di_example.dat')


grab_magic_key_reference_list = """['42.60264', '42.60264', '42.60352', '42.60104', '42.73656', '42.8418', '42.8657', '42.92031', '42.56857', '42.49964', '42.49962', '42.50001', '42.52872', '42.45559', '42.48923', '42.46186', '42.69156', '42.65289', '43.30504', '43.36817', '43.42133', '43.8859', '43.84273', '43.53289', '43.57494', '44.15663', '44.18629']"""


def complete_combine_magic_test():
    output_file = 'combine_magic_output_new.out'
    reference_file =  'combine_magic_output_correct.out'
    input_1 = 'combine_magic_input_1.dat'
    input_2 = 'combine_magic_input_2.dat'
    obj = env.run('combine_magic.py', '-WD', directory, '-F', output_file, '-f', input_1, input_2)
    print obj.stdout
    clean_output = PmagPy_tests.file_parse(output_file)
    clean_reference = PmagPy_tests.file_parse(reference_file)
    PmagPy_tests.compare_two_lists(clean_output, clean_reference)
    print "Successfully finished combine_magic_test"
    # no unittest


def complete_cont_rot_test():
    obj = env.run('cont_rot.py', '-con', 'af:sam', '-prj', 'ortho', '-eye', '-20', '0', '-sym', 'k-', '1', '-age', '180', '-res', 'l', stdin='a')
    output = str(obj.files_created)
    reference_output = "{'Cont_rot.pdf': <FoundFile ./new-test-output:Cont_rot.pdf>}"
    if output == reference_output:
        print "Cont_rot produced expected plot"

def complete_customize_criteria_test():
    customize_criteria_infile = 'customize_criteria_example.dat'
    customize_criteria_output = 'customize_criteria_outfile.out'
    customize_criteria_reference = "customize_criteria_output_correct.out"
    customize_criteria = UC('customize_criteria.py', customize_criteria_infile, customize_criteria_output, customize_criteria_reference, None, False, '1')
    customize_criteria.test_help()
    customize_criteria.test_file(customize_criteria_reference)
    # unittest, I'm thinking no

def complete_di_eq_test():
    print "Testing di_eq.py"
    di_eq_infile = 'di_eq_example.dat'
    di_eq_reference = ['-0.239410', '-0.893491', '0.436413', '0.712161', '0.063844', '0.760300', '0.321447', '0.686216', '0.322720', '0.670562', '0.407412', '0.540654', '0.580156', '0.340376', '0.105351', '0.657728', '0.247173', '0.599687', '0.182349', '0.615600', '0.174815', '0.601717', '0.282746', '0.545472', '0.264863', '0.538273', '0.235758', '0.534536', '0.290665', '0.505482', '0.260629', '0.511513', '0.232090', '0.516423', '0.244448', '0.505666', '0.277927', '0.464381', '0.250510', '0.477152', '0.291770', '0.440816', '0.108769', '0.516148', '0.196706', '0.482014', '0.349390', '0.381292', '0.168407', '0.475566', '0.206286', '0.446444', '0.175701', '0.450649', '0.301104', '0.378539', '0.204955', '0.423970', '0.199755', '0.422584', '0.346920', '0.308010', '0.119030', '0.441144', '0.239848', '0.376486', '0.269528', '0.342510', '0.085451', '0.423789', '0.192224', '0.387233', '0.172608', '0.395084', '0.272008', '0.320741', '0.393981', '0.117451', '-0.017726', '0.406002', '0.154273', '0.367000', '0.213903', '0.335760', '0.103221', '0.372202', '0.231833', '0.283245', '0.072160', '0.351538', '0.007802', '0.319236', '0.152583', '0.265350', '0.248133', '0.136412']
    di_eq_wrong = "wrong"
    di_eq = UC('di_eq.py', di_eq_infile)
    di_eq.long_stdout_test(di_eq_reference)
    di_eq_unittest = Bad_test(di_eq)
    di_eq_unittest.test_for_long_stdout_error(di_eq_wrong)



def complete_grab_magic_key_test():
    print "Testing grab magic"
    grab_magic_key = UC('grab_magic_key.py', 'grab_magic_key_er_sites.txt', WD = True)
    grab_magic_key.test_help()
    grab_magic_key.long_stdout_test(grab_magic_key_reference_list, '-key','site_lat')
    # no interactive
        # NEEDS UNITTESTS TOO
    print "Sucessfully finished complete_grab_magic_key_test"


def complete_nrm_specimens_magic_test(): # maybe move to complex_programs
    fsa = file_prefix + 'nrm_specimens_magic_er_samples.txt'
    print "Testing nrm_specimens_magic.py"
    obj= env.run('nrm_specimens_magic.py', '-f', nrm_specimens_magic.input_file, '-fsa', fsa, '-crd,', 'g', '-fsa', fsa, '-F', nrm_specimens_magic.output_file)
    nrm_specimens_magic.test_help()
    # no interactive
    output = nrm_specimens_magic.parse_file(nrm_specimens_magic.output_file)
    correct = nrm_specimens_magic.parse_file(nrm_specimens_magic.correct_output_file)
    incorrect = nrm_specimens_magic.parse_file(nrm_specimens_magic.incorrect_output_file)
    the_list = [(nrm_specimens_magic.output_file, nrm_specimens_magic.correct_output_file, nrm_specimens_magic.incorrect_output_file)]
    PmagPy_tests.iterate_through(the_list)
    print "Successfully completed nrm_specimens_magic.py tests"
    # needs unittests
 
def complete_sundec_test():
#    sundec = UC('sundec.py', 'sundec_example.dat')
    sundec.test_help()
    sundec.test_interactive()
 #   sundec.parse_file(sundec.input_file)
    sundec.stdout_test(154.2)
    sundec_unittest = Bad_test(sundec)
    sundec_unittest.test_for_stdout_error(100.)
    sundec_unittest.test_for_stdout_error(0.)
    sundec_unittest.test_for_stdout_error(-230.)
    print "Successfully finished sundec.py tests"


def complete_pca_test():
    pca = UC('pca.py', 'pca_example.dat')
    pca.test_help()
#    pca.stdout_test(pca_correct_out)
    obj = env.run('pca.py', '-dir', 'L', '1', '10', '-f', '/Users/nebula/Python/Basic_input_output/pca_example.dat')
    print obj.stdout
    if str(obj.stdout) in pca_correct_out:
        print "Pca.py output as expected"
    else:
        print "Expected: " + pca_correct_out + " but got: " + str(obj.stdout)
        raise NameError("Pca.py producing incorrect output")
    # there are different possibe configurations, should I test some of them?  The above hits all the command line options, but not all of their configurations
    # need unittests
    print "Successfully completed pca.py tests"

def complete_vgp_di_test():
  #  vgp_di = UC('vgp_di.py', 'vgp_di_example.dat')
    vgp_di.test_help()
    vgp_di.test_interactive()
    file_name = file_prefix + 'vgp_di_example.dat'
    obj = env.run('vgp_di.py', '-f', file_name)
    print obj.stdout
    if str(obj.stdout) in vgp_di_correct_out:
        print "Vgp.py output as expected"
    else:
        print "Expected: " + vgp_di_correct_out + " but got: " + str(obj.stdout)
        raise NameError("vgp_di.py producing incorrect output")
    print "Successfully completed vgp_di.py tests"
#class Bad_pca(unittest.TestCase):
 #   def test_for_error(self):
  #      self.assertRaises(NameError, 





#    complete_sundec_test()
#Basic_input_output.complete_working_test()


pca_correct_out = """
eba24a DE-BFL
0 0.00 339.9 57.9 9.2830e-05
1 2.50 325.7 49.1 7.5820e-05
2 5.00 321.3 45.9 6.2920e-05
3 10.00 314.8 41.7 5.2090e-05
4 15.00 310.3 38.7 4.4550e-05
5 20.00 305.0 37.0 3.9540e-05
6 30.00 303.9 34.7 3.2570e-05
7 40.00 303.0 32.3 2.5670e-05
8 50.00 303.6 32.4 2.2520e-05
9 60.00 299.8 30.8 1.9820e-05
10 70.00 292.5 31.0 1.3890e-05
11 80.00 297.0 25.6 1.2570e-05
12 90.00 299.3 11.3 0.5030e-05
eba24a DE-BFL 10    2.50  70.00    8.8   334.9    51.5
"""


vgp_di_correct_out = """
  335.6    62.9
"""

def complete_working_test():
    complete_combine_magic_test()
    complete_customize_criteria_test()
    complete_di_eq_test()
    complete_grab_magic_key_test()
    complete_nrm_specimens_magic_test()
    complete_sundec_test()
    complete_pca_test()
    complete_vgp_di_test()
#    PmagPy_tests.clean_house()


if __name__ == "__main__":
    pass
#    complete_working_test()

