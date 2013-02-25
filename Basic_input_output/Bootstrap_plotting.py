#! /usr/bin/env python

import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import Basic_input_output
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'


example_list = [3.34, 2.222, 1.0, 2.345, 4.89, 5.6]
def create_bootstrap_reference(in_list):
    for l in in_list:
        string = str(l)
        length = len(string)
        print string, length
        if length > 3:
            last_digit = string[-1]
            if last_digit >= 5:
                print last_digit + " is greater than five"
                upper_limit_stripped = string[:-1]
                upper_limit_last = str(int(string[-1]) - 5)
                final_upper_limit = upper_limit_stripped + upper_limit_last
                print "string " + string
                print "upper limit" + final_upper_limit
            else:
                print last_digit + " is less than five"
#            lower_bound = string[:-1]
 #           upper_bound = int(string[:-1]) + 5

create_bootstrap_reference(example_list)


def remove_non_integers_from_output(raw_output):
    clean_output = []
    for i in raw_output:
        if i[-1] == ":":
            i = i.strip(":")
        try:
            clean_output.append(float(i))
        except:
            pass
    return clean_output

def check_bootstrap(actual_output, reference_output):
    for num, z in enumerate(actual_output):
        lower_bound = reference_output[num][0]
        upper_bound = reference_output[num][1]
        if z <= upper_bound and z >= lower_bound:
            print "success"
        else:
            print "z was: " + str(z) + ", upper_bound was: " + str(upper_bound) + ", lower_bound was: " + str(lower_bound)
            print "error raised"
            raise ValueError("program produced incorrect output")
    print "End of check_bootstrap"


ninety_thousand = ['0.34040287', '29.6', '14.5', '33.5', '171.0', '67.3', '6.6', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.1', '27.0', '13.3', '10.7', '294.1', '12.2', '0.32423124', '296.2', '12.8', '10.8', '179.2', '63.5', '4.9', '31.6', '22.9']

aniso_magic_reference = [(.3402, .34042), (29.5, 29.7), (14.4, 14.6), (30., 37.), (170., 172.), (66., 69.), (6.3, 7.), (295.7,296.1), (13., 14.), (0.33535, .33537), (166.2, 166.4), (70.4, 70.6), (23.5, 24.7), (25., 28.), (12., 14.), (10.5, 11.2), (293.,
295.), (11., 13.), (0.324231, .324232), (296.1, 296.3), (12.7, 12.9), (10.6, 11), (177, 181.), (62., 65.), (4.8, 5.1), (31.3, 31.9), (21., 24.)]


def do_aniso_magic(times):
    print "Testing aniso_magic.py, running bootstrap: " + str(times) + " times"
    # WD
    obj = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_dike_anisotropy.txt', '-F', 'aniso_magic_rmag_anisotropy.txt', '-nb', times, '-gtc', '110', '2', '-par', '-v', '-crd', 'g', '-P') #stdin='q')
    print obj.stdout
    PmagPy_tests.test_for_bad_file(obj.stdout)
    a_list = str(obj.stdout).split()
    print a_list
    clean_list = remove_non_integers_from_output(a_list)
    return clean_list

def complete_aniso_magic_test():
    output1 = do_aniso_magic(20000)
    check_bootstrap(output1, aniso_magic_reference)
    output2 =  do_aniso_magic(10000)
    check_bootstrap(output2, aniso_magic_reference)
    output3 = do_aniso_magic(10000)
    check_bootstrap(output3, aniso_magic_reference)


test_50000=[0.33505, 0.00021, 5.3, 14.7, 10.3, 260.7, 38.8, 13.5, 111.8, 46.8, 0.33334, 0.0002, 124.5, 61.7, 6.0, 225.3, 5.9, 17.2, 318.6, 28.6, 0.33161, 0.00014, 268.8, 23.6, 10.7, 358.0, 3.9, 12.5, 96.7, 65.8]
test_100000=[0.33505, 0.00021, 5.3, 14.7, 10.3, 260.7, 38.9, 13.6, 111.7, 46.8, 0.33334, 0.00021, 124.5, 61.7, 6.1, 225.3, 5.9, 17.2, 318.5, 28.6, 0.33161, 0.00014, 268.8, 23.6, 10.7, 358.2, 4.2, 12.5, 97.5, 65.8]
bootams_reference=[(0.3350, 0.3351), (0.0002, 0.0003), (5.1, 5.5), (14.5, 14.9), (10.1, 10.5), (260.5, 261.5), (37.5, 39.1), (13.2, 13.9), (111.6, 112.4), (46., 48.), (.3333, .3334), (.00009, .0003), (124.5, 124.7), (61.5, 61.9), (5.8, 6.2), (225., 225.6), (5.6, 6.2), (17., 17.4), (318.3, 318.9), (28.3, 28.9), (.33150, .3317), (.0001, .0002), (268.5, 269.), (23.3, 23.9), (10.4, 11.), (357.6, 359.5), (3.6, 6.5), (12.2, 12.8), (96.4, 101.5), (65., 66.)]


def do_bootams(num):
    bootams_infile = file_prefix + 'bootams_example.dat'
    obj = env.run('bootams.py', '-f', bootams_infile, '-nb', num)
    a_list = str(obj.stdout).split()
    clean_list = remove_non_integers_from_output(a_list)
    print clean_list
    return clean_list

def complete_bootams_test():
    output1 = do_bootams(100000)
    check_bootstrap(output1, bootams_reference)
    output2 = do_bootams(100000)
    check_bootstrap(output2, bootams_reference)




#EI

find_EI_reference = [(38.8, 39.0), (58.7, 58.9), (45., 50.), (65., 69.), (1.4, 1.5), (1.2, 1.35), (1.7, 2.2)]

def run_EI(num):
    obj = env.run('find_EI.py', '-f', file_prefix + 'find_EI_example.dat', '-nb', num, stdin='a')
    print obj.files_created
    output = str(obj.stdout[-210:-143]).split()
    clean_out = remove_non_integers_from_output(output)
    print "Finish run_EI()"
    return clean_out

def complete_find_EI_test():
    print "Testing find_EI.py"
    output1 = run_EI(400)
    check_bootstrap(output1, find_EI_reference)
    output2 = run_EI(800)
    check_bootstrap(output2, find_EI_reference)
    output3 = run_EI(900)
    check_bootstrap(output3, find_EI_reference)
    print "Ran find_EI bootstrap test three times"

class Bad_find_EI(unittest.TestCase):
    def test_for_error(self):
        print "TESTING FOR ERROR"
        bad_out = run_EI(25)
        self.assertRaises(ValueError, check_bootstrap, bad_out, find_EI_reference)

class Bad_aniso_magic(unittest.TestCase):
    def test_for_error(self):
        print "TESTING FOR ERROR"
        bad_out = do_aniso_magic(100)
        self.assertRaises(ValueError, check_bootstrap, bad_out, aniso_magic_reference)

class Bad_bootams(unittest.TestCase):
    def test_for_error(self):
        print "TESTING FOR ERROR"
        bad_out = do_bootams(100)
        self.assertRaises(ValueError, check_bootstrap, bad_out, bootams_reference)

#complete_aniso_magic_test()        
#complete_find_EI_test()
complete_bootams_test()

if __name__ == "__main__":
#    pass
    unittest.main(module="Bootstrap_plotting")
