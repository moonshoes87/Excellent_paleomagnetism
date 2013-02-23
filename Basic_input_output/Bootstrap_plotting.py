import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import Basic_input_output
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'



def remove_non_integers_from_output(raw_output):
    clean_output = []
    for i in raw_output:
        print "i = " + str(i)
        if i[-1] == ":":
            i = i.strip(":")
        try:
            clean_output.append(float(i))
        except:
            print i
    return clean_output




ten_thousand_1 = ['0.34040287', '29.6', '14.5', '34.5', '171.3', '67.2', '6.7', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.5', '26.7', '13.3', '10.8', '293.8', '12.1', '0.32423124', '296.2', '12.8', '10.9', '178.7', '63.8', '4.9', '31.5', '22.4']
ten_thousand_2 = ['0.34040287', '29.6', '14.5', '33.7', '171.2', '67.4', '6.6', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.6', '294.4', '12.2', '0.32423124', '296.2', '12.8', '10.7', '179.2', '63.5', '4.9', '31.6', '22.8']
thirty_thousand_1 = ['0.34040287', '29.6', '14.5', '33.8', '171.3', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '26.9', '13.3', '10.8', '294.0', '12.2', '0.32423124', '296.2', '12.8', '10.9', '179.5', '63.1', '5.0', '31.7', '23.2']
thirty_thousand_2 = ['0.34040287', '29.6', '14.5', '33.9', '171.2', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.8', '294.4', '12.3', '0.32423124', '296.2', '12.8', '10.8', '179.4', '63.3', '5.0', '31.6', '23.1']
ninety_thousand = ['0.34040287', '29.6', '14.5', '33.5', '171.0', '67.3', '6.6', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.1', '27.0', '13.3', '10.7', '294.1', '12.2', '0.32423124', '296.2', '12.8', '10.8', '179.2', '63.5', '4.9', '31.6', '22.9']

aniso_magic_reference_list = [(.3403, .3402), (29.5, 29.7), (14.4, 14.6), (33., 35.), (170.9, 171.4), (67., 67.4), (6.5, 6.8), (295.9,296.1), (13.3, 13.6), (0.33535, .33537), (166.2, 166.4), (70.4, 70.6), (23.9, 24.7), (26., 28.), (13.1, 13.4), (10.5, 10.9), (293.,
295.), (12., 12.5), (0.324231, .324232), (296.1, 296.3), (12.7, 12.9), (10.6, 11), (178, 180), (63., 64.), (4.8, 5.1), (31.3, 31.9), (21., 24.)]
def complete_aniso_magic_test():
    print "Testing aniso_magic.py"
    # WD
    obj = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_dike_anisotropy.txt', '-F', 'aniso_magic_rmag_anisotropy.txt', '-nb', '2000','-gtc', '110', '2', '-par', '-v', '-crd', 'g', '-P') #stdin='q')
    print obj.stdout
   # obj2 = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_sed_anisotropy.txt', '-F', 'aniso_magic_rmag_results.txt','-d', '3', '0', '90', '-v', '-crd', 'g', stdin='a')                                                                                  
    #print obj2.stdout                                                                                                   
    PmagPy_tests.test_for_bad_file(obj.stdout)
    a_list = str(obj.stdout).split()
    print a_list
    new_list = []
    for i in a_list:
        try:
            f = float(i)
            new_list.append(i)
        except ValueError:
            print i
    print new_list
    # JUST FIGURE OUT HOW TO TEST THESE VALUES                                                                                            # can use stdin = 'q', or 'a' (to save).  Then can optionally test for files_created/files_updated.  currently using -P, which me\ans no plots, hooray.                                                                                                                   # should I make this a Plot object???  It has too many extra args to run tidily. 
#complete_aniso_magic_test()



#FIND EI TEST
reference = [(38.8, 39.0), False, (58.7, 58.9), False, (45., 50.), False, (65., 69.), (1.4, 1.5), False, (1.2, 1.35), False, (1.7, 2.2)]
new_reference = [(38.8, 39.0), (58.7, 58.9), (45., 50.), (65., 69.), (1.4, 1.5), (1.2, 1.35), (1.7, 2.2)]

def run_EI(num):
    obj = env.run('find_EI.py', '-f', file_prefix + 'find_EI_example.dat', '-nb', num, stdin='a')
    print obj.files_created
    output = str(obj.stdout[-210:-143]).split()
    print "Finish run_EI()"
    return output



def do_bootstrap(times):
    raw_out = run_EI(times)
    clean_out = remove_non_integers_from_output(raw_out)
    print "result" + str(clean_out)
    print "reference: " + str(new_reference)
    for num, z in enumerate(clean_out):
        lower_bound = new_reference[num][0]
        upper_bound = new_reference[num][1]
        if z <= upper_bound and z >= lower_bound:
            print "success"
        else:
            print "z was: " + str(z) + ", upper_bound was: " + str(upper_bound) + ", lower_bound was: " + str(lower_bound)
            print "error raised"
            raise ValueError("find_EI.py produced incorrect output")
    print "End of do_bootstrap"

def complete_find_EI_test():
    print "Testing find_EI.py"
    do_bootstrap(200)
#    do_bootstrap(800)
#    do_bootstrap(900)                                                                                                              
    print "Ran find_EI bootstrap test three times"

class Bad_find_EI(unittest.TestCase):
    def test_for_error(self):
        print "TESTING FOR ERROR"
        self.assertRaises(ValueError, do_bootstrap, 25)

complete_find_EI_test()

if __name__ == "__main__":
    pass
 #   unittest.main(module="Bootstrap_plotting")
