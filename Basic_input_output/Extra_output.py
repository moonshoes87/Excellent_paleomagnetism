#! /usr/bin/env python                                                                                                                
import sys
import traceback
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess
import Rename_me
import PmagPy_tests as PT
import clean_log_output
import error_logging as EL


file_prefix = PT.file_prefix
directory =  PT.directory

class Ex_out(Rename_me.Test_instance):
    def __init__(self, name, infile, tag1, outfile1, tag2, outfile2, correctfile1, correctfile2, wrongfile1, wrongfile2, stdin, WD, *args):
        self.name = name
        self.infile = file_prefix + infile
        self.tag1 = tag1
        self.outfile1 = file_prefix + outfile1
        self.tag2 = tag2
        if outfile2 == None:
            self.outfile2 = None
        else:
            self.outfile2 = file_prefix + outfile2
        self.correctfile1 = file_prefix + correctfile1
        self.correctfile2 = file_prefix + correctfile2
        self.wrongfile1 = file_prefix + wrongfile1
        self.wrongfile2 = file_prefix + wrongfile2
        self.stdin = stdin
        self.WD = WD
        self.args = args
        if self.WD:
            self.infile, self.outfile1, self.outfile2, self.correctfile1, self.correctfile2, self.wrongfile1, self.wrongfile2 = infile, outfile1, outfile2, correctfile1, correctfile2, wrongfile1, wrongfile2
        self.arg1 = None
        self.parse_args()

    def parse_args(self):
        if len(self.args) > 0:
            self.arg1 = self.args[0]

    def run_program(self):
        #PT.clean_house()        
        if self.WD:
            print "about to run WD program"
            print (self.name, '-WD', directory, '-f', self.infile, self.tag1, self.outfile1, self.tag2, self.outfile2, self.arg1, 'stdin=' + str(self.stdin))
            obj = env.run(self.name, '-WD', directory, '-f', self.infile, self.tag1, self.outfile1, self.tag2, self.outfile2, self.arg1, stdin=self.stdin)
        else:
            print "about to run non-WD program"
            print (self.name, '-f', self.infile, self.tag1, self.outfile1, self.tag2, self.outfile2, self.arg1, 'stdin=' + self.stdin)
            obj = env.run(self.name, '-f', self.infile, self.tag1, self.outfile1, self.tag2, self.outfile2, self.arg1, stdin= self.stdin)
        if len(obj.stdout) < 1000:
            print "stdout: " +str(obj.stdout)
        else:
            print "STDOUT: " + str(obj.stdout)[:500] + " .... "
            print " " + str(obj.stdout)[-500:]
        print "files created: " + str(obj.files_created)
        print "files updated: " + str(obj.files_updated)

    def check_list_output(self, output_list, correct_output_list):
        print "checking list output"
        print "output_list:         " + str(output_list)[:100] +  " ...]"
        print "correct_output_list: " + str(correct_output_list)[:100]  + " ...]"
        print "Comparing two lists"
        list_empty = True
        for num, i in enumerate(output_list):
            list_empty = False
            if i == correct_output_list[num]:
                pass
               # print i, "   ",  correct_output_list[num]
               # print "correct"
            else:
                print "Output contained:    " + str(i)
                print "but should have had: " + str(correct_output_list[num])
                print "Error raised"
                raise NameError("Wrong output -- output list did not match correct_output_list" ) # can this message be more informative??
        if list_empty:
            print "ONE OR BOTH LISTS DID NOT HAVE CONTENT"
            raise NameError("Output list empty")
        print "Lists were the same"
        print str(self.name) + " produced correct output"

    def check_list_output_expect_error(self, output_list, incorrect_output_list):
        print "Testing list output (for error)"
        diff_found = False
        for n, i in enumerate(output_list):
            if i != incorrect_output_list[n]:
                diff_found = True
                print "output was:          " +str(i)
                print "wrong reference was: " + str(incorrect_output_list[n])
            else: 
                pass
#                print i, "   ", incorrect_output_list[n]
        if diff_found:
            print "Difference found"
        else:
            print "No difference found"
            print "error raised"
            raise NameError("Difference should have been found, but was not")

    def check_file_output(self, outfile, reference_file, reference="correct"):
        """
        parses each file word by word, then checks to see if the outfile matches the reference file.
        """
        print "testing: " + str(outfile) + " against reference file: " + str(reference_file)
        if reference == "correct":
            print "NOT expecting an error"
        if reference == "incorrect":
            print "expecting an error"
        out = PT.file_parse_by_word_and_pmagpy_strip(outfile)
        print "file length = " + str(len(out))
        ref = PT.file_parse_by_word_and_pmagpy_strip(reference_file)
        print "file length = " + str(len(ref))
        if reference == "incorrect":
            self.check_list_output_expect_error(out, ref)
        else:
            self.check_list_output(out, ref)

    def ex_out_sequence(self):
        self.run_program()
        print "ran program: " + str(self.name)
        self.standard_check_file_sequence()
        self.extra_output_unittest()

    def standard_check_file_sequence(self):
        print "checking outfile1 against correctfile1"
        self.check_file_output(self.outfile1, self.correctfile1, reference="correct")
        print "-"
        print "checking outfile2 against correctfile2"
        self.check_file_output(self.outfile2, self.correctfile2, reference="correct")
        print "-"
        print "checking outfile1 against wrongfile1"
        self.check_file_output(self.outfile1, self.wrongfile1, reference="incorrect")
        print "-"
        print "checking outfile 2 against wrongfile2"
        self.check_file_output(self.outfile2, self.wrongfile2, reference="incorrect")
        print "-"
   
    def extra_output_unittest(self):
        print "STARTING UNITTEST"
        unittest = Bad_test(self)
        print "expecting error!"
        unittest.test_outfile1_with_wrongfile1()
        print "-"
        print "expecting error!"
        unittest.test_outfile1_with_correctfile1()
        print "-"
        print "expecting error!"
        unittest.test_outfile2_with_wrongfile2()
        print "-"
        print "expecting error!"
        unittest.test_outfile2_with_correctfile2()

class Bad_test(unittest.TestCase):
    def __init__(self, ex_out_obj):
        self.ex_out = ex_out_obj

    def test_ex_out_for_error(self):
        self.assertRaises(NameError, self.ex_out.check_outputs, the_list="bad")
        print "Error expected"
        print "-"

    def test_outfile1_with_wrongfile1(self):
        print "running: test_outfile1_with_wrongfile1"
        self.assertRaises(NameError, self.ex_out.check_file_output, self.ex_out.outfile1, self.ex_out.wrongfile1, reference="correct")
        print "error expected"

    def test_outfile1_with_correctfile1(self):
        print "running: test_outfile1_with_correctfile2"
        self.assertRaises(NameError, self.ex_out.check_file_output, self.ex_out.outfile1, self.ex_out.correctfile1, reference="incorrect")
        print "error expected"

    def test_outfile2_with_wrongfile2(self):
        print "running: test_outfile2_with_wrongfile2()"
        self.assertRaises(NameError, self.ex_out.check_file_output, self.ex_out.outfile2, self.ex_out.wrongfile2, reference="correct")
        print "error expected"

    def test_outfile2_with_correctfile2(self):
        print "running: test_outfile2_with_correctfile2()"
        self.assertRaises(NameError, self.ex_out.check_file_output, self.ex_out.outfile2, self.ex_out.correctfile2, reference="incorrect")
        print "error expected"

    def test_file1_with_file2(self, file1, file2, ref):
        print "running: test_file1_with_file2 using " + str(file1) + " and " + str(file2)
        self.assertRaises(NameError, self.ex_out.check_file_output, file1, file2, reference=ref)
        print "error expected"



#  def __init__(self, name, infile, tag1, outfile1, tag2, outfile2, correctfile1, correctfile2, wrongfile1, wrongfile2, stdin, WD, *args):
def complete_aarm_magic_test():
    """testing aarm_magic.py"""
    print "Testing aarm_magic"
    infile = "aarm_measurements.txt"
    aarm_Fa, aarm_Fr = 'aarm_magic_anisotropy_new.out', 'aarm_magic_results_new.out'
    tag1, tag2 = "-Fa", "-Fr"
    aarm_Fa_reference, aarm_Fr_reference = 'aarm_magic_anisotropy_incorrect.out', 'aarm_magic_results_correct.out' # should be correct
    aarm_Fa_wrong, aarm_Fr_wrong = 'aarm_magic_anisotropy_incorrect.out', 'aarm_magic_results_incorrect.out'
    aarm_magic = Ex_out('aarm_magic.py', infile, tag1, aarm_Fa, tag2, aarm_Fr, aarm_Fa_reference, aarm_Fr_reference, aarm_Fa_wrong, aarm_Fr_wrong, None, True)
    aarm_magic.ex_out_sequence()



def complete_atrm_magic_test():
    """test atrm_magic.py"""
    atrm_infile = 'atrm_magic_measurements.txt'
    atrm_Fa, atrm_Fr = "atrm_anisotropy_new.out", "atrm_results_new.out"
    tag1, tag2 = '-Fa', '-Fr'
    atrm_Fa_reference, atrm_Fr_reference = "atrm_anisotropy_correct.txt", "atrm_results_correct.txt"
    atrm_Fa_wrong, atrm_Fr_wrong = "atrm_anisotropy_incorrect.txt", "atrm_results_incorrect.txt"
    atrm = Ex_out('atrm_magic.py', atrm_infile, tag1, atrm_Fa, tag2, atrm_Fr, atrm_Fa_reference, atrm_Fr_reference, atrm_Fa_wrong, atrm_Fr_wrong, None, True)
    print "Testing atrm_magic.py:"
    atrm.ex_out_sequence()
 #   obj = env.run('atrm_magic.py', '-WD', directory, '-f', atrm_infile, '-Fa', atrm_Fa, '-Fr', atrm_Fr)
#    print obj.stdout

def complete_CIT_magic_test():
    """test CIT_magic.py"""
    CIT_magic_infile = 'CIT_magic_example.sam'
    CIT_magic_outfile1 = None
    CIT_magic_outfile2 = None

# er_sites.txt is supposed to be designatable on the command-line with -Fsp, but is not.  fix this....


def complete_hysteresis_magic_test(): # irregular.  a file has to be renamed because it just comes out a default way, it is not specifiable on the command line
    """test hysteresis_magic.py"""
    tag1, tag2 = '-F', None
    outfile2 = None
    hysteresis_magic_infile = 'hysteresis_magic_example.dat'
    hysteresis_F, hysteresis_F_reference, hysteresis_F_wrong = 'hysteresis_magic_rmag_new.out',  'hysteresis_magic_rmag_correct.txt', 'hysteresis_magic_rmag_incorrect.txt'
    hysteresis_remanence, hysteresis_remanence_reference, hysteresis_remanence_wrong = 'rmag_remanence.txt', 'hysteresis_magic_remanence_correct.txt', 'hysteresis_magic_remanence_incorrect.txt'
    hysteresis_magic_list = [(hysteresis_F, hysteresis_F_reference, hysteresis_F_wrong), (hysteresis_remanence, hysteresis_remanence_reference, hysteresis_remanence_wrong)]
    hysteresis_magic = Ex_out('hysteresis_magic.py', hysteresis_magic_infile, tag1, hysteresis_F, tag2, outfile2, hysteresis_F_reference, hysteresis_remanence_reference, hysteresis_F_wrong, hysteresis_remanence_wrong, 'q', True, '-P')
    print "Testing hysteresis_magic.py"
    hysteresis_magic.run_program()
    subprocess.call(['mv', file_prefix + 'rmag_remanence.txt', file_prefix + 'hysteresis_magic_remanence_new.out']) # renames file so it is easier to find
    print hysteresis_magic.outfile2
    hysteresis_magic.outfile2 = "hysteresis_magic_remanence_new.out"
    print hysteresis_magic.outfile2
    hysteresis_magic.ex_out_sequence() # this re runs hysteresis magic, but that is not a problem
    print hysteresis_magic.outfile2
    subprocess.call(['rm', file_prefix + 'rmag_remanence.txt']) # remove extra rmag_remanence that doesn't get renamed


def complete_k15_magic_test(): # irregular -- has 4 output files!!!!
    """test k15_magic.py"""
    print "Testing k15_magic.py"
    k15_infile = 'k15_magic_example.dat'
    tag1 = "-Fsa"
    tag2 = "-Fa"
    k15_Fsa, k15_Fsa_reference, k15_Fsa_wrong = 'k15_magic_er_samples_new.out', 'k15_magic_er_samples_correct.txt', 'k15_magic_er_samples_incorrect.txt'
    k15_Fa, k15_Fa_reference, k15_Fa_wrong = 'k15_magic_rmag_anisotropy_new.out','k15_magic_rmag_anisotropy_correct.txt', 'k15_magic_rmag_anisotropy_incorrect.txt'
    k15_F, k15_F_reference, k15_F_wrong = 'k15_magic_measurements_new.out','k15_magic_measurements_correct.txt', 'k15_magic_measurements_incorrect.txt'
# this one is not specifiable on command line, so I rename it later.  the output is named rmag_results.txt no matter what.
    k15_rmag, k15_rmag_reference, k15_rmag_wrong = 'k15_magic_rmag_results_new.out', 'k15_magic_rmag_results_correct.txt', 'k15_magic_rmag_results_incorrect.txt'
    k15_magic = Ex_out('k15_magic.py', k15_infile, tag1, k15_Fsa, tag2, k15_Fa, k15_Fsa_reference, k15_Fa_reference, k15_Fsa_wrong, k15_Fa_wrong, None, True)
    obj = env.run('k15_magic.py', '-WD', directory, '-f', k15_infile, '-Fsa', k15_Fsa, '-Fa', k15_Fa, '-F', k15_F)
    print obj.stdout
    # renames rmag_results.txt to k15_rmag_results.txt (for consistency)
    obj = env.run('mv', file_prefix + 'rmag_results.txt', file_prefix + 'k15_magic_rmag_results_new.out')
    k15_magic.standard_check_file_sequence()
    # extra, because of additional options
    k15_magic.check_file_output(k15_F, k15_F_reference, reference="correct")
    print "6..."
    k15_magic.check_file_output(k15_F, k15_F_wrong, reference="incorrect")
    print "7..."
    k15_magic.check_file_output(k15_rmag, k15_rmag_reference, reference="correct")
    print "8..."
    k15_magic.check_file_output(k15_rmag, k15_rmag_wrong, reference="incorrect")
    # unittests
    k15_magic.extra_output_unittest()
    k15_unittest = Bad_test(k15_magic)
    k15_unittest.test_file1_with_file2(k15_F, k15_F_reference, "incorrect")
    k15_unittest.test_file1_with_file2(k15_F, k15_F_wrong, "correct")
    k15_unittest.test_file1_with_file2(k15_rmag, k15_rmag_reference, "incorrect")
    k15_unittest.test_file1_with_file2(k15_rmag, k15_rmag_wrong, "correct")


def complete_kly4s_magic_test(): # irregular, with 3 output files
    """test kly4s_magic.py"""
    print "Testing kly4s_magic.py"
    kly4s_infile = "kly4s_magic_example.dat"
    tag1, tag2 = '-F', '-Fa'
    kly4s_F, kly4s_F_reference, kly4s_F_wrong = "kly4s_magic_measurements_new.out", "kly4s_magic_measurements_correct.txt", "kly4s_magic_measurements_incorrect.txt"
    kly4s_Fa, kly4s_Fa_reference, kly4s_Fa_wrong = "kly4s_rmag_anisotropy_new.out", "kly4s_rmag_anisotropy_correct.txt", "kly4s_rmag_anisotropy_incorrect.txt"
    kly4s_er, kly4s_er_reference, kly4s_er_wrong = "kly4s_er_specimens_new.out", "kly4s_er_specimens_correct.txt", "kly4s_er_specimens_incorrect.txt"
    kly4s = Ex_out('kly4s_magic.py', kly4s_infile, tag1, kly4s_F, tag2, kly4s_Fa, kly4s_F_reference, kly4s_Fa_reference, kly4s_F_wrong, kly4s_Fa_wrong, None, True)
    obj = env.run('kly4s_magic.py', '-WD', directory, '-f', kly4s_infile, '-F', kly4s_F, '-Fa', kly4s_Fa)
    print obj.stdout
    obj = env.run('mv', file_prefix + "er_specimens.txt", file_prefix + "kly4s_er_specimens_new.out") # renames
    print "Renamed er_specimens.txt to kly4s_er_specimens.txt"
    kly4s.standard_check_file_sequence()
    # extra checks
    kly4s.check_file_output(kly4s_er, kly4s_er_reference, reference="correct")
    kly4s.check_file_output(kly4s_er, kly4s_er_wrong, reference="incorrect")
    kly4s.extra_output_unittest()
    # extra unittests
    kly4s_unittest = Bad_test(kly4s)
    kly4s_unittest.test_file1_with_file2(kly4s_er, kly4s_er_reference, "incorrect")
    kly4s_unittest.test_file1_with_file2(kly4s_er, kly4s_er_wrong, "correct")

#complete_kly4s_magic_test()

def complete_pmag_results_extract_test():
    """test pmag_results_extract.py"""
    print "Testing pmag_results_extract.py"
    pmag_intensities, pmag_intensities_reference, pmag_intensities_wrong = file_prefix + 'Intensities.txt', file_prefix + 'pmag_results_extract_Intensities_correct.txt', file_prefix + 'pmag_results_extract_Intensities_incorrect.txt'
    pmag_directions, pmag_directions_reference, pmag_directions_wrong = file_prefix + 'Directions.txt', file_prefix + 'pmag_results_extract_Directions_correct.txt', file_prefix + 'pmag_results_extract_Directions_incorrect.txt'
    pmag_sitenfo, pmag_sitenfo_reference, pmag_sitenfo_wrong = file_prefix + 'SiteNfo.txt', file_prefix + 'pmag_results_extract_SiteNfo_correct.txt', file_prefix + 'pmag_results_extract_SiteNfo_incorrect.txt'
    pmag_results_extract_list = [(pmag_intensities, pmag_intensities_reference, pmag_intensities_wrong), (pmag_directions, pmag_directions_reference, pmag_directions_wrong), (pmag_sitenfo, pmag_sitenfo_reference, pmag_sitenfo_wrong)]
    pmag_results_extract_infile = 'pmag_results_extract.dat'
    pmag_results = Ex_out('pmag_results_extract.py', pmag_results_extract_infile, None, pmag_intensities, None, pmag_directions, pmag_intensities_reference, pmag_directions_reference, pmag_intensities_wrong, pmag_directions_wrong, None, True)
    obj = env.run('pmag_results_extract.py', '-WD', directory, '-f', 'pmag_results_extract.dat')
    print obj.stdout
    print obj.files_created
    print obj.files_updated
    pmag_results.standard_check_file_sequence()
    # extra options below
    pmag_results.check_file_output(pmag_sitenfo, pmag_sitenfo_reference, reference="correct")
    pmag_results.check_file_output(pmag_sitenfo, pmag_sitenfo_wrong, reference="incorrect")
    pmag_results.extra_output_unittest()
    # extra unittests
    pmag_unittest = Bad_test(pmag_results)
    pmag_unittest.test_file1_with_file2(pmag_sitenfo, pmag_sitenfo_reference, "incorrect")
    pmag_unittest.test_file1_with_file2(pmag_sitenfo, pmag_sitenfo_wrong, "correct")
    subprocess.call(['rm', file_prefix + 'Intensities.txt', file_prefix + 'Directions.txt', file_prefix + 'SiteNfo.txt'])


def complete_orientation_magic_test():
    """test orientation_magic.py"""
    print "Testing orientation_magic.py"
    infile = "orientation_magic_exa.txt"
    tag1, tag2 = "-Fsi", "-Fsa"
    orient_Fsi, orient_Fsa = "orientation_magic_er_sites_new.out", "orientation_magic_er_samples_new.out"
    orient_Fsi_reference, orient_Fsa_reference = "orientation_magic_er_sites_correct.out", "orientation_magic_er_samples_correct.out"
    orient_Fsi_wrong, orient_Fsa_wrong = "orientation_magic_er_sites_incorrect.out", "orientation_magic_er_samples_incorrect.out"
    orientation_magic = Ex_out('orientation_magic.py', infile, tag1, orient_Fsi, tag2, orient_Fsa, orient_Fsi_reference, orient_Fsa_reference, orient_Fsi_wrong, orient_Fsa_wrong, None, True)
    orientation_magic.ex_out_sequence()
                    
#complete_orientation_magic_test()    

def complete_thellier_magic_redo_test(): # quite irregular
    """test thellier_magic_redo.py"""
    print "Testing thellier_magic_redo.py"
    infile = 'thellier_magic_redo_example.dat'
    outfile = "thellier_magic_redo_specimens_new.out"
    in_tag1, in_tag2, in_tag3 = '-fnl', '-fre', '-fan'
    in1, in2, in3 = "thellier_magic_redo_measurements.txt", "thellier_magic_redo2.txt", "thellier_magic_redo_rmag_anisotropy.txt"
    out_tag1, out_tag2 = "-Fnl", "Fac"
    out1, out2 = "thellier_magic_redo_NLT_specimens_new.out", "thellier_magic_redo_AC_specimens_new.out"
    correct_out1, correct_out2 = "thellier_magic_redo_NLT_specimens_correct.txt", "thellier_magic_redo_AC_specimens_correct.txt"
    wrong_out1, wrong_out2 = "thellier_magic_redo_NLT_specimens_incorrect.txt", "thellier_magic_redo_AC_specimens_incorrect.txt"
    arg1, arg2 = "-NLT", "-ANI"
    thellier_magic_redo_reference = None
    thellier_magic_redo = Ex_out('thellier_magic_redo.py', infile, out_tag1, out1, out_tag2, out2, correct_out1, correct_out2, wrong_out1, wrong_out2, None, True)
    obj = env.run("thellier_magic_redo.py", "-WD", directory, "-f", infile, in_tag1, in1, in_tag2, in2, in_tag3, in3, "-F", outfile, out_tag1, out1, out_tag2, out2, arg1, arg2)
    print "STDOUT: " + str(obj.stdout)[:700] 
    print " .... " 
    print str(obj.stdout)[-700:]
    print "FILES UPDATED: " + str(obj.files_updated)
    print "FILES CREATED: " + str(obj.files_created)
    thellier_magic_redo.standard_check_file_sequence()
    thellier_magic_redo.extra_output_unittest()

#complete_thellier_magic_test()
ignore = """
thellier_magic_redo.py -f thellier_magic_redo_example.dat  -fnl thellier_magic_redo_measurements.txt -fre thellier_magic_redo2.txt -fan thellier_magic_redo_rmag_anisotropy.txt  -F thellier_magic_redo_specimens.txt -Fnl thellier_magic_redo_NLT_specimens.txt  -Fac thellier_magic_redo_AC_specimens.txt -NLT -ANI
"""


# listings and such that make this whole business work

ex_out_function_mapping = {"aarm_magic": complete_aarm_magic_test, "atrm_magic": complete_atrm_magic_test, "hysteresis_magic": complete_hysteresis_magic_test, "k15_magic": complete_k15_magic_test, "kly4s_magic": complete_kly4s_magic_test, "pmag_results_extract": complete_pmag_results_extract_test, "orientation_magic": complete_orientation_magic_test, "thellier_magic_redo": complete_thellier_magic_redo_test}

Extra_output_tests = [complete_aarm_magic_test, complete_atrm_magic_test, complete_hysteresis_magic_test, complete_k15_magic_test, complete_kly4s_magic_test, complete_pmag_results_extract_test, complete_orientation_magic_test]# complete_thellier_magic_redo_test]

# ADD LAST TEST BACK IN!!!!!!!!

ex_out_errors_list = open('extra_output_errors_list.txt', 'w')

# an interactive option that runs just one program, as instructed
# if no interactive tag is given, it will just run through
if __name__ == "__main__": 
    if "-r" in sys.argv: # 
        PT.run_individual_program(ex_out_function_mapping)
    else:
        new_list = EL.go_through(Extra_output_tests, ex_out_errors_list) # (list of tests, file to log them in) this creates a list of which programs are messed up, along with their error message.  
        EL.redo_broken_ones(new_list) # this goes through the messed up ones again and adds to the output
        print "finished with Extra_output.py testing and re-testing"


# run as: python Extra_output.py > extra_out_full_output.txt
# then command: python clean_output.py
    # extra_out_all_output.txt
    # extra_out_clean_output.txt
# to run an individual program: python Extra_output.py hiccup 'program_to_run'



def complete_working_test():
    PT.remove_new_outfiles()
    complete_aarm_magic_test()
    complete_atrm_magic_test()
    complete_hysteresis_magic_test()
    complete_k15_magic_test()
    complete_kly4s_magic_test()
    complete_pmag_results_extract_test()
    complete_orientation_magic_test()
    complete_thellier_magic_redo_test()
    PT.clean_house()

#if __name__ == "__main__":
 #   pass
#    complete_working_test()




