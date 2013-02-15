#! /usr/bin/env python                                                                                                                
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Basic_input_output
import PmagPy_tests
import subprocess

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'

print PmagPy_tests.universal_variable

# iterates through a list of tuples with files, and compares them.  Order is: (output, correct_reference, incorrect_reference)
def iterate_through(some_list):
    print "Iterating through: " + str(some_list)
    z = 0
    for i in some_list:
        print i
        thing = PmagPy_tests.file_parse(some_list[z][0])
        correct_thing = PmagPy_tests.file_parse(some_list[z][1])
        incorrect_thing = PmagPy_tests.file_parse(some_list[z][2])
        print "Output was: " + str(thing)
        print "-"
        print "Output should have been: " + str(correct_thing)
        print "-"
        z +=1
        if thing == correct_thing:
            print "Output is as expected"
        else:
            print "Error raised"
            raise NameError("No good")
        if thing != incorrect_thing:
            print "Output does not equal incorrect reference"
        else:
            print "Error raised"
            raise NameError("You suck")
        print str(z) + " iterations"


class Ex_out(Basic_input_output.in_out):

    def add_attr(self, input_file, Fa, Fr, Fa_reference = None, Fr_reference = None, Fa_wrong = None, Fr_wrong = None):
        self.input_file = input_file
        self.Fa = Fa
        self.Fr = Fr
        self.Fa_reference = Fa_reference
        self.Fr_reference = Fr_reference
        self.Fa_wrong = Fa_wrong
        self.Fr_wrong = Fr_wrong


    def run_with_two_options(self):
        env.run(self.name, '-WD', directory, '-f', self.input_file , '-Fa', self.Fa, '-Fr', self.Fr)

    def check_attr(self):
        Fa = self.parse_file(self.Fa)
        Fr = self.parse_file(self.Fr)
        Fa_reference = self.parse_file(self.Fa_reference)
        Fr_reference = self.parse_file(self.Fr_reference)
        Fa_wrong = self.parse_file(self.Fa_wrong)
        Fr_wrong = self.parse_file(self.Fr_wrong)
        if Fa == Fa_reference and Fa != Fa_wrong:
            print self.Fa + " is correct"
        else:
            print self.name + " raised error"
            raise NameError(self.Fa + " was incorrect")
        if Fr == Fr_reference and Fr != Fr_wrong:
            print str(self.Fr) + " is correct"
        else:
            print str(self.name) + " raised error"
            raise NameError(self.Fr + " was incorrect")

        
# aarm_magic test
aarm_magic_in_file = "aarm_measurements.txt"
#fsa = 'er_samples.txt' appears not to matter.....
aarm_Fa, aarm_Fr = 'aarm_magic_anisotropy.out', 'aarm_magic_results.out'
aarm_Fa_reference, aarm_Fr_reference = 'aarm_magic_anisotropy_correct.out', 'aarm_magic_results_correct.out'
aarm_Fa_wrong, aarm_Fr_wrong = 'aarm_magic_anisotropy_incorrect.out', 'aarm_magic_results_incorrect.out'
aarm_magic = Ex_out('aarm_magic.py', aarm_magic_in_file)

def complete_aarm_magic_test():   
    print "-"
    print "Testing aarm_magic.py:"
    aarm_magic.add_attr(aarm_magic_in_file, aarm_Fa, aarm_Fr, aarm_Fa_reference, aarm_Fr_reference, aarm_Fa_wrong, aarm_Fr_wrong)
    aarm_magic.run_with_two_options()
    aarm_magic.check_attr()

class Bad_aarm_magic(unittest.TestCase):
    def test_for_error(self):
        aarm_magic.add_attr(aarm_magic_in_file, aarm_Fa, aarm_Fr, aarm_Fa_wrong, aarm_Fr_wrong, aarm_Fa_reference, aarm_Fr_reference)
        aarm_magic.run_with_two_options()
        self.assertRaises(NameError, aarm_magic.check_attr)         

# atrm_magic.py test
atrm_in_file = 'atrm_magic_example.dat'
atrm_Fa, atrm_Fr = "atrm_anisotropy.txt", "atrm_results.txt"
atrm_Fa_reference, atrm_Fr_reference = "atrm_anisotropy_correct.txt", "atrm_results_correct.txt"
atrm_Fa_wrong, atrm_Fr_wrong = "atrm_anisotropy_incorrect.txt", "atrm_results_incorrect.txt"
atrm_magic = Ex_out('atrm_magic.py', atrm_in_file)

def complete_atrm_magic_test():
    print "-"
    print "Testing atrm_magic.py:"
    atrm_magic.add_attr(atrm_in_file, atrm_Fa, atrm_Fr, atrm_Fa_reference, atrm_Fr_reference, atrm_Fa_wrong, atrm_Fr_wrong)
    atrm_magic.run_with_two_options()
    atrm_magic.check_attr()

class Bad_atrm(unittest.TestCase):
    def test_for_error(self):
        atrm_magic.add_attr(atrm_in_file, atrm_Fa, atrm_Fr, atrm_Fa_wrong, atrm_Fr_wrong, atrm_Fa_reference, atrm_Fr_reference)
        atrm_magic.run_with_two_options()
        self.assertRaises(NameError, atrm_magic.check_attr)


#k15_magic.py test
k15_in_file = 'k15_magic_example.dat'
k15_Fsa, k15_Fsa_reference, k15_Fsa_wrong = 'k15_magic_er_samples.txt', 'k15_magic_er_samples_correct.txt', 'k15_magic_er_samples_incorrect.txt'
k15_Fa, k15_Fa_reference, k15_Fa_wrong = 'k15_magic_rmag_anisotropy.txt','k15_magic_rmag_anisotropy_correct.txt', 'k15_magic_rmag_anisotropy_incorrect.txt'
k15_F, k15_F_reference, k15_F_wrong = 'k15_magic_measurements.txt','k15_magic_measurements_correct.txt', 'k15_magic_measurements_incorrect.txt'
# this one is not specifiable on command line, so I rename it later
k15_rmag, k15_rmag_reference, k15_rmag_wrong = 'k15_magic_rmag_results.txt', 'k15_magic_rmag_results_correct.txt', 'k15_magic_rmag_results_incorrect.txt'
k15_list = [(k15_Fsa, k15_Fsa_reference, k15_Fsa_wrong), (k15_Fa, k15_Fa_reference, k15_Fa_wrong), (k15_F, k15_F_reference, k15_F_wrong), (k15_rmag, k15_rmag_reference, k15_rmag_wrong)]
k15_bad_list = [(k15_Fsa, k15_Fsa_reference, k15_Fsa_reference), (k15_Fa, k15_Fa_wrong, k15_Fa_wrong), (k15_F, k15_F_wrong, k15_F_reference), (k15_rmag, k15_rmag_reference, k15_rmag_reference)]

def complete_k15_magic_test():
    obj = env.run('k15_magic.py', '-WD', directory, '-f', k15_in_file, '-Fsa', k15_Fsa, '-Fa', k15_Fa, '-F', k15_F)
    print obj.stdout
    # renames rmag_results.txt to k15_rmag_results.txt (for consistency)
    obj = env.run('mv', file_prefix + 'rmag_results.txt', file_prefix + 'k15_magic_rmag_results.txt')
    # iterate through:
    iterate_through(k15_list)
        
class Bad_k15_magic(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, iterate_through, k15_bad_list)
        print "Error expected"


#kly4s_magic.py test
kly4s_infile = "kly4s_magic_example.dat"
kly4s_F, kly4s_F_reference, kly4s_F_wrong = "kly4s_magic_measurements.txt", "kly4s_magic_measurements_correct.txt", "kly4s_magic_measurements_incorrect.txt"
kly4s_Fa, kly4s_Fa_reference, kly4s_Fa_wrong = "kly4s_rmag_anisotropy.txt", "kly4s_rmag_anisotropy_correct.txt", "kly4s_rmag_anisotropy_incorrect.txt"
kly4s_er, kly4s_er_reference, kly4s_er_wrong = "kly4s_er_specimens.txt", "kly4s_er_specimens_correct.txt", "kly4s_er_specimens_incorrect.txt"
kly4s_list = [(kly4s_F, kly4s_F_reference, kly4s_F_wrong), (kly4s_Fa, kly4s_Fa_reference, kly4s_Fa_wrong), (kly4s_er, kly4s_er_reference, kly4s_er_wrong)]
kly4s_bad_list = [(kly4s_F, kly4s_F_reference, kly4s_F_reference), (kly4s_Fa, kly4s_Fa_wrong, kly4s_Fa_wrong), (kly4s_er, kly4s_er_wrong, kly4s_er_reference)]

def complete_kly4s_magic_test():
    obj = env.run('kly4s_magic.py', '-WD', directory, '-f', kly4s_infile, '-F', kly4s_F, '-Fa', kly4s_Fa)
    print obj.stdout
    obj = env.run('mv', file_prefix + "er_specimens.txt", file_prefix + "kly4s_er_specimens.txt")
    iterate_through(kly4s_list)

class Bad_kly4s_magic(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, iterate_through, kly4s_bad_list)
        print "Error expected"


    # do I need to then delete the test files???
#kly4s_magic.py -f KLY4S_magic_example.dat -F kly4s_magic_measurements.txt -Fa kly4s_rmag_anisotropy.txt


pmag_criteria, pmag_criteria_reference, pmag_criteria_wrong = file_prefix + 'Criteria.txt', file_prefix + 'pmag_results_extract_Criteria_correct.txt', file_prefix + 'pmag_results_extract_Criteria_incorrect.txt'
pmag_directions, pmag_directions_reference, pmag_directions_wrong = file_prefix + 'Directions.txt', file_prefix + 'pmag_results_extract_Directions_correct.txt', file_prefix + 'pmag_results_extract_Directions_incorrect.txt'
pmag_sitenfo, pmag_sitenfo_reference, pmag_sitenfo_wrong = file_prefix + 'SiteNfo.txt', file_prefix + 'pmag_results_extract_SiteNfo_correct.txt', file_prefix + 'pmag_results_extract_SiteNfo_incorrect.txt'
pmag_results_extract_list = [(pmag_criteria, pmag_criteria_reference, pmag_criteria_wrong), (pmag_directions, pmag_directions_reference, pmag_directions_wrong), (pmag_sitenfo, pmag_sitenfo_reference, pmag_sitenfo_wrong)]

def complete_pmag_results_extract_test():
    # WD
    pmag_results_extract_in_file = 'pmag_results_extract.dat'
    obj = env.run('pmag_results_extract.py', '-WD', directory, '-f', 'pmag_results_extract.dat')
    print obj.stdout
    print obj.files_created
    iterate_through(pmag_results_extract_list)
    subprocess.call(['rm', file_prefix + 'Criteria.txt', file_prefix + 'Directions.txt', file_prefix + 'SiteNfo.txt'])
    # needs unittests.  wait until you see what you end up with in this category
    

complete_pmag_results_extract_test()

def do_unittest():
    unittest.main(module='Extra_output') 


def complete_working_test():
    complete_aarm_magic_test()
    complete_atrm_magic_test()
    complete_k15_magic_test()
    complete_kly4s_magic_test()
    complete_pmag_results_extract_test()
#    PmagPy_tests.clean_house()
    do_unittest()


if __name__ == "__main__":
    pass
    #complete_working_test()
# fails to do this because it quits after unittest : (
