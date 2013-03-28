#! /usr/bin/env python

import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'

class in_out(object):

    def __init__(self, name, input_file, output_file = None, correct_output_file = None, incorrect_output_file = None, WD = False, stdin= None):
        self.name = name
        self.input_file = file_prefix + input_file
        if output_file != None:
            self.output_file = file_prefix + output_file
        if correct_output_file != None:
            self.correct_output_file = file_prefix + correct_output_file
        if incorrect_output_file != None:
            self.incorrect_output_file = file_prefix + incorrect_output_file
        self.WD = WD
        if self.WD == True:
            self.input_file, self.output_file, self.correct_output_file, self.incorrect_output_file = input_file, output_file,correct_output_file,incorrect_output_file
        self.stdin = stdin

    def test_interactive(self):
        obj = env.run(self.name, '-i')#, stdin='3')
        print("stdout: "+ str(obj.stdout))
        if len(obj.stdout) > 10:
            print "Interactive mode works"
            print "-"
        else:
            raise NameError("Interactive mode for " + str(self.name) + " came up empty")

    def test_help(self):
        help_message = "help"
        obj = env.run(self.name, '-h')
        message = str(obj.stdout)
        print(len(message))
        if len(message) > 150:
            print "Help message successfully called"
            print "-"
        else:
            raise NameError("Help message for " + str(self.name)+ " failed...")
        
    def test_file(self, reference_output):
        name = self.name
        print("Running: " + str(name) + " using " + str(reference_output) + " as our reference output")
        if self.WD:
            obj = env.run(self.name, '-WD', '/Users/nebula/Python/Basic_input_output/', '-f', self.input_file, '-F', self.output_file, stdin=self.stdin)
        else:
            obj = env.run(self.name, '-f', self.input_file, '-F', self.output_file, stdin=self.stdin)
        print("Standard output: " + str(obj.stdout))
        print("Input file: " + str(self.input_file) +  " output file: " + str(self.output_file))
        parsed_file_out = self.parse_file(self.output_file)
        parsed_file_correct = self.parse_file(reference_output)
        output_file_empty = True
        for z, line in enumerate(parsed_file_out):
            output_file_empty = False
            print(line, " should equal ", parsed_file_correct[z])
            if line == parsed_file_correct[z]:
                print "success"
            else:
                print "Error raised"
                raise NameError(str(self.name) + " expected output does not match actual output")
        if output_file_empty:
            print "OUTPUT FILE WAS EMPTY, error raised"
            raise NameError("Running " + self.name +  "  produced no output")
        print "Test file found no errors, using as reference: "+ str(reference_output)
        print "-"

    def parse_file(self, the_file):
        # changed to 'rU' option, now things work better
        data = open(the_file, 'rU').readlines()
        print "Parsing file:" + str(the_file)
       # print data
        clean_file = []
        for l in data:
            new_line = l.strip('\n')
            clean_file.append(new_line)
        return clean_file

# moved to utility file
#def clean_house():
 #   print "CLEANING HOUSE"
  #  subprocess.call(['rm', '-rf',  'new-test-output/'])


class Bad_test(unittest.TestCase):
    def __init__(self, in_out_obj):
        self.in_out_obj = in_out_obj
    def test_for_error(self):
        print "Testing: " + str(self.in_out_obj.name) + " with incorrect file, expecting error"
        self.assertRaises(NameError, self.in_out_obj.test_file, self.in_out_obj.incorrect_output_file)
        print "Error expected"
        print "-"




def complete_working_test():
    complete_angle_test()
    complete_apwp_test()
    complete_b_vdm_test()
    complete_cart_dir_test()
    complete_convert_samples_test()
    complete_di_geo_test()
    complete_dir_cart_test()
    complete_di_rot_test()
    complete_di_tilt_test()
    complete_di_vgp_test()
    complete_eigs_s_test()
    complete_eq_di_test()
    complete_gobing_test()
    complete_gofish_test()
    complete_gokent_test()
    complete_goprinc_test()
    complete_igrf_test()
    complete_k15_s_test()
    complete_mk_redo_test()
    complete_pt_rot_test()
    complete_s_eigs_test()
    complete_s_geo_test()
    complete_s_tilt_test()
    complete_stats_test()
    complete_vdm_b_test()
#    print "CLEANING HOUSE"
 #   PmagPy_tests.clean_house()
    print "DONE WITH TEST!!!!!!"
    print "-"
    print "-"
   

# List of complete individual tests

def complete_angle_test(): #MOVED
    angle = in_out('angle.py', 'angle.dat', 'angle_results_new.txt', 'angle_results_correct.txt', 'angle_results_incorrect.txt')
    angle.test_interactive()
    angle.test_help()
    angle.test_file(angle.correct_output_file)
    angle_unittest = Bad_test(angle)
    angle_unittest.test_for_error()
    
def complete_apwp_test(): # MOVED
    apwp = in_out('apwp.py', 'apwp_example.dat', 'apwp_results_new.out', 'apwp_results_correct.out', 'apwp_results_incorrect.out')
    apwp.test_help()
    apwp.test_interactive()
    apwp.test_file(apwp.correct_output_file)
    apwp_unittest = Bad_test(apwp)
    apwp_unittest.test_for_error()

def complete_b_vdm_test(): # MOVED
    b_vdm = in_out('b_vdm.py', 'b_vdm_example.dat', 'b_vdm_results_new.out', 'b_vdm_results_correct.out', 'b_vdm_results_incorrect.out')
    b_vdm.test_help()
    b_vdm.test_interactive()
    b_vdm.test_file(b_vdm.correct_output_file)
    b_vdm_unittest = Bad_test(b_vdm)
    b_vdm_unittest.test_for_error()

def complete_cart_dir_test(): # MOVED
    cart_dir = in_out('cart_dir.py', 'cart_dir_example.dat', 'cart_dir_results_new.out', 'cart_dir_results_correct.out', 'cart_dir_results_incorrect.out')
    cart_dir.test_help()
    cart_dir.test_interactive()
    cart_dir.test_file(cart_dir.correct_output_file)
    cart_dir_unittest = Bad_test(cart_dir)
    cart_dir_unittest.test_for_error()

def complete_convert_samples_test(): # MOVED
    convert_samples = in_out('convert_samples.py', 'convert_samples_example.dat', 'convert_samples_Northern_Iceland.txt', 'convert_samples_results_correct.out', 'convert_samples_results_incorrect.out')
    convert_samples.test_help()
    # no interactive mode
    convert_samples.test_file(convert_samples.correct_output_file)
    convert_samples_unittest = Bad_test(convert_samples)
    convert_samples_unittest.test_for_error()

def complete_di_geo_test(): #MOVED
    di_geo = in_out('di_geo.py', 'di_geo_example.dat', 'di_geo_results_new.out', 'di_geo_results_correct.out', 'di_geo_results_incorrect.out')
    di_geo.test_help()
    di_geo.test_file(di_geo.correct_output_file)
    di_geo.test_interactive()
    di_geo_unittest = Bad_test(di_geo)
    di_geo_unittest.test_for_error()

def complete_di_tilt_test(): #MOVED
    di_tilt = in_out('di_tilt.py', 'di_tilt_example.dat', 'di_tilt_results_new.out', 'di_tilt_results_correct.out', 'di_tilt_results_incorrect.out')
    di_tilt.test_help()
    di_tilt.test_interactive()
    di_tilt.test_file(di_tilt.correct_output_file)
    di_tilt_unittest = Bad_test(di_tilt)
    di_tilt_unittest.test_for_error()


def complete_dir_cart_test(): # MOVED
    dir_cart = in_out('dir_cart.py', 'dir_cart_example.dat', 'dir_cart_results_new.out', 'dir_cart_results_correct.out', 'dir_cart_results_incorrect.out')
    dir_cart.test_help()
    dir_cart.test_interactive()
    dir_cart.test_file(dir_cart.correct_output_file)
    dir_cart_unittest = Bad_test(dir_cart)
    dir_cart_unittest.test_for_error()

def complete_di_rot_test(): # MOVED
    di_rot = in_out('di_rot.py', 'di_rot_example.dat', 'di_rot_results_new.out', 'di_rot_results_correct.out', 'di_rot_results_incorrect.out')
    di_rot.test_help()
# no interactive
    di_rot.test_file(di_rot.correct_output_file)
    di_rot_unittest = Bad_test(di_rot)
    di_rot_unittest.test_for_error()
# should this be checked with its additional command line arguments?  I'm thinking no....

def complete_di_vgp_test(): # MOVED
    di_vgp = in_out('di_vgp.py', 'di_vgp_example.dat', 'di_vgp_results_new.out', 'di_vgp_results_correct.out', 'di_vgp_results_incorrect.out')
    di_vgp.test_help()
    di_vgp.test_interactive()
    di_vgp.test_file(di_vgp.correct_output_file)
    di_vgp_unittest = Bad_test(di_vgp)
    di_vgp_unittest.test_for_error()

def complete_eigs_s_test(): # MOVED
    eigs_s = in_out('eigs_s.py', 'eigs_s_example.dat', 'eigs_s_results_new.out', 'eigs_s_results_correct.out', 'eigs_s_results_incorrect.out')
    eigs_s.test_help()
    # no interactive
    eigs_s.test_file(eigs_s.correct_output_file)
    eigs_s_unittest = Bad_test(eigs_s)
    eigs_s_unittest.test_for_error()

def complete_eq_di_test(): # MOVED
    eq_di = in_out('eq_di.py', 'eq_di_example.dat', 'eq_di_results_new.out', 'eq_di_results_correct.out', 'eq_di_results_incorrect.out')
    # no interactive
    eq_di.test_help()
    eq_di.test_file(eq_di.correct_output_file)
    eq_di_unittest = Bad_test(eq_di)
    eq_di_unittest.test_for_error()

def complete_gobing_test(): # MOVED
    gobing = in_out('gobing.py', 'gobing_example.out', 'gobing_results_new.out', 'gobing_results_correct.out', 'gobing_results_incorrect.out')
    gobing.test_help()
    # no interactive
    gobing.test_file(gobing.correct_output_file)
    gobing_unittest = Bad_test(gobing)
    gobing_unittest.test_for_error()

def complete_gofish_test(): #MOVED
    gofish = in_out('gofish.py', 'gofish_example.out', 'gofish_results_new.out', 'gofish_results_correct.out', 'gofish_results_incorrect.out')
    gofish.test_help()
    # no interactive
    gofish.test_file(gofish.correct_output_file)
    gofish_unittest = Bad_test(gofish)
    gofish_unittest.test_for_error()
    
def complete_gokent_test(): #MOVED
    gokent = in_out('gokent.py', 'gokent_example.out', 'gokent_results_new.out', 'gokent_results_correct.out', 'gokent_results_incorrect.out')
    gokent.test_help()
    # no interactive
    gokent.test_file(gokent.correct_output_file)
    gokent_unittest = Bad_test(gokent)
    gokent_unittest.test_for_error()

def complete_goprinc_test(): #MOVED
    goprinc = in_out('goprinc.py', 'goprinc_example.dat', 'goprinc_results_new.out', 'goprinc_results_correct.out', 'goprinc_results_incorrect.out')
    goprinc.test_help()
    #no interactive
    goprinc.test_file(goprinc.correct_output_file)
    goprinc_unittest = Bad_test(goprinc)
    goprinc_unittest.test_for_error()

def complete_igrf_test(): #MOVED
# this guy also has command line options, including a plotting one.  possibly it should get some more/different stuff.
    igrf = in_out('igrf.py', 'igrf_example.dat', 'igrf_results_new.out', 'igrf_results_correct.out', 'igrf_results_incorrect.out')
    igrf.test_help()
    igrf.test_interactive()
    igrf.test_file(igrf.correct_output_file)
    igrf_unittest = Bad_test(igrf)
    igrf_unittest.test_for_error()

def complete_k15_s_test():#MOVED
    # this guy has one additional command line option.  i wonder if it needs to be tested??
    k15_s = in_out('k15_s.py', 'k15_s_example.dat', 'k15_s_results_new.out', 'k15_s_results_correct.out', 'k15_s_results_incorrect.out')
    k15_s.test_help()
    # no real interactive mode (just a way to interactive input the file you want to use)
    k15_s.test_file(k15_s.correct_output_file)
    k15_s_unittest = Bad_test(k15_s)
    k15_s_unittest.test_for_error()

def complete_mk_redo_test():#MOVED
    mk_redo = in_out('mk_redo.py', 'pmag_specimens.txt', 'mk_redo_results_new.out', 'mk_redo_results_correct.out', 'mk_redo_results_incorrect.out', True)
    mk_redo.test_help()
    # no interactive
    mk_redo.test_file(mk_redo.correct_output_file)
    mk_redo_unittest = Bad_test(mk_redo)
    mk_redo_unittest.test_for_error()

#def complete_nrm_specimens_magic_test():
 #   nrm_specimens_magic = in_out('nrm_specimens_magic.py', 'nrm_specimens_magic_measurements.txt', 'nrm_specimens_results_new.out', 'nrm_specimens_results_correct.out', 'nrm_specimens_results_incorrect.out')
def complete_pt_rot_test(): #MOVED
    pt_rot = in_out('pt_rot.py', 'pt_rot_example.dat', 'pt_rot_results_new.out', 'pt_rot_results_correct.out', 'pt_rot_results_incorrect.out', True)
    pt_rot.test_help()
    # no interactive mode
    pt_rot.test_file(pt_rot.correct_output_file)
    # testing -ff option:
    obj = env.run('pt_rot.py', '-WD', '/Users/nebula/Python/Basic_input_output/', '-ff', 'pt_rot_extra_in_nam_180-200.txt', 'pt_rot_extra_in_nam_panA.frp', '-F', 'pt_rot_extra_out.out')
    extra_out_file = pt_rot.parse_file('pt_rot_extra_out.out')
    extra_correct_file = pt_rot.parse_file('pt_rot_extra_correct.out')
    if extra_out_file == extra_correct_file:
        print "Successfully ran pt_rot.py with -ff option"
    else:
        raise NameError("pt_rot.py failed to correctly run with -ff option -- output was different from expected output")
    pt_rot_unittest = Bad_test(pt_rot)
    pt_rot_unittest.test_for_error()

def complete_s_eigs_test(): #MOVED
    s_eigs = in_out('s_eigs.py', 's_eigs_example.dat', 's_eigs_results_new.out', 's_eigs_results_correct.out', 's_eigs_results_incorrect.out')
    s_eigs.test_help()
    # no interactive
    s_eigs.test_file(s_eigs.correct_output_file)
    s_eigs_unittest = Bad_test(s_eigs)
    s_eigs_unittest.test_for_error()

def complete_s_geo_test(): # MOVED
    s_geo = in_out('s_geo.py', 's_geo_example.dat', 's_geo_results_new.out', 's_geo_results_correct.out', 's_geo_results_incorrect.out')
    s_geo.test_help()
    # no interactive
    s_geo.test_file(s_geo.correct_output_file)
    s_geo_unittest = Bad_test(s_geo)
    s_geo_unittest.test_for_error()
    
def complete_s_tilt_test(): # MOVED
    s_tilt = in_out('s_tilt.py', 's_tilt_example.dat', 's_tilt_results_new.out', 's_tilt_results_correct.out', 's_tilt_results_incorrect.out')
    s_tilt.test_help()
    # no interactive
    s_tilt.test_file(s_tilt.correct_output_file)
    s_tilt_unittest = Bad_test(s_tilt)
    s_tilt_unittest.test_for_error()

def complete_stats_test(): # MOVED
    stats = in_out('stats.py', 'stats_example.dat', 'stats_results_new.out', 'stats_results_correct.out', 'stats_results_incorrect.out')
    stats.test_help()
    # no interactive
    stats.test_file(stats.correct_output_file)
    stats_unittest = Bad_test(stats)
    stats_unittest.test_for_error()

def complete_vdm_b_test(): #MOVED
    vdm_b = in_out('vdm_b.py', 'vdm_b_example.dat', 'vdm_b_results_new.out', 'vdm_b_results_correct.out', 'vdm_b_results_incorrect.out')
    vdm_b.test_help()
    vdm_b.test_interactive()
    vdm_b.test_file(vdm_b.correct_output_file)
    vdm_b_unittest = Bad_test(vdm_b)
    vdm_b_unittest.test_for_error()

# list of all the help messages

angle_help_message = """
    NAME
        angle.py
    
    DESCRIPTION
      calculates angle between two input directions D1,D2
    
    INPUT (COMMAND LINE ENTRY) 
           D1_dec D1_inc D1_dec D2_inc
    OUTPUT
           angle
    
    SYNTAX
        angle.py [-h][-i] [command line options] [< filename]
    
    OPTIONS
        -h prints help and quits 
        -i for interactive data entry
        -f FILE input filename
        -F FILE output filename (required if -F set)
        Standard I/O 
    
"""

help_messages = {'angle.py': angle_help_message}

if __name__ == '__main__':

#    complete_working_test()
    print "Full test suite completed"





# end of working program

class Problem():
    def __init__(self, in_out_obj, message = ""):
        self.in_out_obj = in_out_obj
        self.message = message
# accumulate Problems, spit them all out at the end???
# on the other hand, this test suite doesn't take THAT long to execute.  so maybe it's not a big deal
# I could have a problems array, that then is helpful....
# or something, wherever I raise errors... however, this would make the unittests all break.  so, fuck that.  



# creates a set of instances for the unittests to use
"""
angle = in_out('angle.py', 'angle.dat', 'angle_results_new.txt', 'angle_results_correct.txt', 'angle_results_incorrect.txt')
apwp = in_out('apwp.py', 'apwp_example.dat', 'apwp_results_new.out', 'apwp_results_correct.out', 'apwp_results_incorrect.out')
b_vdm = in_out('b_vdm.py', 'b_vdm_example.dat', 'b_vdm_results_new.out', 'b_vdm_results_correct.out', 'b_vdm_results_incorrect.out')
cart_dir = in_out('cart_dir.py', 'cart_dir_example.dat', 'cart_dir_results_new.out', 'cart_dir_results_correct.out', 'cart_dir_results_incorrect.out')
di_geo = in_out('di_geo.py', 'di_geo_example.dat', 'di_geo_results.out', 'di_geo_results_correct.out', 'di_geo_results_incorrect.out', 'Declination: <cntrl-D> to quit   Good-bye')
di_tilt = in_out('di_tilt.py', 'di_tilt_example.dat', 'di_tilt_results_new.out', 'di_tilt_results_correct.out', 'di_tilt_results_incorrect.out', 'Declination: <cntrl-D> to quit   Good-bye')
dir_cart = in_out('dir_cart.py', 'dir_cart_example.dat', 'dir_cart_results_new.out', 'dir_cart_results_correct.out', 'dir_cart_results_incorrect.out')
eigs_s = in_out('eigs_s.py', 'eigs_s_example.dat', 'eigs_s_results_new.out', 'eigs_s_results_correct.out', 'eigs_s_results_incorrect.out')
gobing = in_out('gobing.py', 'gobing_example.out', 'gobing_results_new.out', 'gobing_results_correct.out', 'gobing_results_incorrect.out')
gofish = in_out('gofish.py', 'gofish_example.out', 'gofish_results_new.out', 'gofish_results_correct.out', 'gofish_results_incorrect.out')
gokent = in_out('gokent.py', 'gokent_example.out', 'gokent_results_new.out', 'gokent_results_correct.out', 'gokent_results_incorrect.out')
goprinc = in_out('goprinc.py', 'goprinc_example.dat', 'goprinc_results_new.out', 'goprinc_results_correct.out', 'goprinc_results_incorrect.out')
igrf = in_out('igrf.py', 'igrf_example.dat', 'igrf_results_new.out', 'igrf_results_correct.out', 'igrf_results_incorrect.out')
k15_s = in_out('k15_s.py', 'k15_s_example.dat', 'k15_s_results_new.out', 'k15_s_results_correct.out', 'k15_s_results_incorrect.out')
pt_rot = in_out('pt_rot.py', 'pt_rot_example.dat', 'pt_rot_results_new.out', 'pt_rot_results_correct.out', 'pt_rot_results_incorrect.out', True)
mk_redo = in_out('mk_redo.py', 'pmag_specimens.txt', 'mk_redo_results_new.out', 'mk_redo_results_correct.out', 'mk_redo_results_incorrect.out', True)
"""
"""
class Bad_angle(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, angle.test_file, angle.incorrect_output_file)

class Bad_apwp(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, apwp.test_file, apwp.incorrect_output_file)

class Bad_b_vdm(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, b_vdm.test_file, b_vdm.incorrect_output_file)

class Bad_cart_dir(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, cart_dir.test_file, cart_dir.incorrect_output_file)

class Bad_di_geo(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, di_geo.test_file, di_geo.incorrect_output_file)

class Bad_di_tilt(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, di_tilt.test_file, di_tilt.incorrect_output_file)

class Bad_dir_cart(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, dir_cart.test_file, dir_cart.incorrect_output_file)

class Bad_eigs_s(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, eigs_s.test_file, eigs_s.incorrect_output_file)

class Bad_gobing(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, gobing.test_file, gobing.incorrect_output_file)

class Bad_gofish(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, gofish.test_file, gobing.incorrect_output_file)

class Bad_gokent(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, gokent.test_file, gokent.incorrect_output_file)

# is this useful????
    def test_for_interactive(self):
        self.assertRaises(AssertionError, gokent.test_interactive)

class Bad_goprinc_test(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, goprinc.test_file, goprinc.incorrect_output_file)

class Bad_igrf_test(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, igrf.test_file, igrf.incorrect_output_file)

class Bad_k15_s_test(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, k15_s.test_file, k15_s.incorrect_output_file)

class Bad_mk_redo_test(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, mk_redo.test_file, mk_redo.incorrect_output_file)

class Bad_pt_rot_test(unittest.TestCase):
    def test_for_error(self):
        self.assertRaises(NameError, pt_rot.test_file, pt_rot.incorrect_output_file)

def do_unittest():
    unittest.main(module='Basic_input_output')
"""
