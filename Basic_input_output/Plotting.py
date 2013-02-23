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


class Plot(object):

     def __init__(self, name, infile, ref_out, wrong_out, stdin, WD, *args):
         self.name = name
         self.infile = file_prefix + infile
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
             print(self.name, '-WD', directory, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, 'stdin='+str(self.stdin))
             obj = env.run(self.name, '-WD', directory, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin)
         else:
             print "Non-WD program about to run:"
             print self.name, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5,  'stdin=' + str(self.stdin)
             obj = env.run(self.name, '-f', self.infile, self.arg_0, self.arg_1, self.arg_2, self.arg_3, self.arg_4, self.arg_5, stdin=self.stdin)
         if plot:
             print obj.files_created
             return obj.files_created
         else:
             print obj.stdout
             return obj.stdout

     
     def check_plots_created(self):
         pass # is this reasonable??

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

class Bad_test(unittest.TestCase):
    def __init__(self, plotting_obj):
        self.plotting_obj = plotting_obj

    def test_for_error(self):
        print "Running unittest(s) for:  " + str(self.plotting_obj.name)
        self.assertRaises(NameError, self.plotting_obj.check_output, self.plotting_obj.wrong_out, self.plotting_obj.ref_out)
        print "Error expected"

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
 s[a]ve plot, [b]ounds for pca and calculate, change [h]orizontal projection angle, [q]uit:"""
    zeq_reference_output_without_extra_commandline_options = """0      0.0 9.283e-05   339.9    57.9 
1      2.5 7.582e-05   325.7    49.1 
2      5.0 6.292e-05   321.3    45.9 
3     10.0 5.209e-05   314.8    41.7 
4     15.0 4.455e-05   310.3    38.7 
5     20.0 3.954e-05   305.0    37.0 
6     30.0 3.257e-05   303.9    34.7 
7     40.0 2.567e-05   303.0    32.3 
8     50.0 2.252e-05   303.6    32.4 
9     60.0 1.982e-05   299.8    30.8 
10     70.0 1.389e-05   292.5    31.0 
11     80.0 1.257e-05   297.0    25.6 
12     90.0 5.030e-06   299.3    11.3 
 s[a]ve plot, [b]ounds for pca and calculate, change [h]orizontal projection angle, [q]uit: """
    zeq_wrong_output = "Hi there"
    zeq = Plot('zeq.py', zeq_infile, zeq_reference_output, zeq_wrong_output, 'q', False, '-u', 'C')
    zeq_output = zeq.run_program()
    zeq.check_output(zeq_output, zeq.ref_out)
    zeq_test = Bad_test(zeq)
    zeq_test.test_for_error()


def complete_ani_depthplot_test():
    # done
    # WD
    print "Testing ani_depthplot.py"
    ani_depthplot_infile = 'ani_depthplot_rmag_anisotropy.txt'
    ani_depthplot_reference = "{'U1359A_ani-depthplot.svg': <FoundFile ./new-test-output:U1359A_ani-depthplot.svg>}"
    ani_depthplot_wrong = "No way"
    ani_depthplot_fsa = 'ani_depthplot_er_samples.txt'
    ani_depthplot = Plot('ani_depthplot.py', ani_depthplot_infile, ani_depthplot_reference, ani_depthplot_wrong, 'a', True, '-fsa', ani_depthplot_fsa)
    ani_depthplot_plot = ani_depthplot.run_program(True)
    ani_depthplot.check_output(ani_depthplot_plot, ani_depthplot.ref_out)
    ani_depthplot_unittest = Bad_test(ani_depthplot)
    ani_depthplot_unittest.test_for_error()
    
trying_to_move_this = """
ten_thousand_1 = ['0.34040287', '29.6', '14.5', '34.5', '171.3', '67.2', '6.7', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.5', '26.7', '13.3', '10.8', '293.8', '12.1', '0.32423124', '296.2', '12.8', '10.9', '178.7', '63.8', '4.9', '31.5', '22.4']
ten_thousand_2 = ['0.34040287', '29.6', '14.5', '33.7', '171.2', '67.4', '6.6', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.6', '294.4', '12.2', '0.32423124', '296.2', '12.8', '10.7', '179.2', '63.5', '4.9', '31.6', '22.8']
thirty_thousand_1 = ['0.34040287', '29.6', '14.5', '33.8', '171.3', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '26.9', '13.3', '10.8', '294.0', '12.2', '0.32423124', '296.2', '12.8', '10.9', '179.5', '63.1', '5.0', '31.7', '23.2']
thirty_thousand_2 = ['0.34040287', '29.6', '14.5', '33.9', '171.2', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.8', '294.4', '12.3', '0.32423124', '296.2', '12.8', '10.8', '179.4', '63.3', '5.0', '31.6', '23.1']
ninety_thousand = ['0.34040287', '29.6', '14.5', '33.5', '171.0', '67.3', '6.6', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.1', '27.0', '13.3', '10.7', '294.1', '12.2', '0.32423124', '296.2', '12.8', '10.8', '179.2', '63.5', '4.9', '31.6', '22.9']

aniso_magic_reference_list = [(.3403, .3402), (29.5, 29.7), (14.4, 14.6), (33., 35.), (170.9, 171.4), (67., 67.4), (6.5, 6.8), (295.9,296.1), (13.3, 13.6), (0.33535, .33537), (166.2, 166.4), (70.4, 70.6), (23.9, 24.7), (26., 28.), (13.1, 13.4), (10.5, 10.9), (293., 295.), (12., 12.5), (0.324231, .324232), (296.1, 296.3), (12.7, 12.9), (10.6, 11), (178, 180), (63., 64.), (4.8, 5.1), (31.3, 31.9), (21., 24.)]
def complete_aniso_magic_test():
    print "Testing aniso_magic.py"
    # WD
    obj = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_dike_anisotropy.txt', '-F', 'aniso_magic_rmag_anisotropy.txt', '-nb', '2000','-gtc', '110', '2', '-par', '-v', '-crd', 'g', '-P') #stdin='q')
    print obj.stdout
   # obj2 = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_sed_anisotropy.txt', '-F', 'aniso_magic_rmag_results.txt', '-d', '3', '0', '90', '-v', '-crd', 'g', stdin='a')
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
    print obj.files_created
    print obj.files_updated
    # JUST FIGURE OUT HOW TO TEST THESE VALUES
    # can use stdin = 'q', or 'a' (to save).  Then can optionally test for files_created/files_updated.  currently using -P, which means no plots, hooray.
    # should I make this a Plot object???  It has too many extra args to run tidily.  

complete_aniso_magic_test()


#FIND EI TEST
reference = [(38.8, 39.0), False, (58.7, 58.9), False, (45., 50.), False, (65., 69.), (1.4, 1.5), False, (1.2, 1.35), False, (1.7, 2.2)]
def run_EI(num):
    obj = env.run('find_EI.py', '-f', file_prefix + 'find_EI_example.dat', '-nb', num, stdin='a')
    print obj.files_created
    output = str(obj.stdout[-210:-143]).split()
    print "Finish run_EI()"
    return output
def do_bootstrap(times):
        #obj = env.run('find_EI.py', '-f', file_prefix + 'find_EI_example.dat', '-nb', '500', stdin='a')
        #print "stdout: " + str(obj.stdout)
#        print obj.files_created
#        output = str(obj.stdout[-210:-143]).split()
               #['38.9', '=>', '58.8', '_', '47.9', '^', '67.8:', '1.4679', '_', '1.2849', '^', '1.9088']
# might be able to do this more nicely.  i.e., maybe use a try except, and if the list item can't be turned into an integer, then lose it from the list. 
    result = run_EI(times)
    z = 0
    print "result" + str(result)
    print "reference: " + str(reference)
    for i in reference:
        print "i = " + str(i)
        if i != False:
            if result[z][-1] == ":":
#                output[z][-1] = str(output[z][-1])
                result[z] = result[z].strip(":")
                print ":"
                print result[z]
            lower_bound = reference[z][0]
            upper_bound = reference[z][1]
            print lower_bound, upper_bound
            out = float(result[z])
            print "out = " + str(out)
            if out > lower_bound and out < upper_bound:
                print "OK"
            else:
                print "Error raised"
                raise NameError("Value: "+ str(out) +", lower-bound: " + str(lower_bound) + ", upper-bound: " + str(upper_bound))
        else:
            pass
        z += 1
    print "End of do_bootstrap"

def complete_find_EI_test():
    print "Testing find_EI.py"
    do_bootstrap(400)
 #   do_bootstrap(800)
#    do_bootstrap(900)
    print "Ran find_EI bootstrap test three times"

class Bad_find_EI(unittest.TestCase):
    def test_for_error(self):
        print "TESTING FOR ERROR"
        self.assertRaises(NameError, do_bootstrap, 25)
"""

def complete_foldtest_test():
    # doesn't produce stdout :(
    # Lisa is editing
    print "Testing foldtest.py"
    foldtest_infile = file_prefix + 'foldtest_example.dat'
    obj = env.run('foldtest.py', '-f', foldtest_infile, '-n', '50', stdin='a')
    print "Stdout: " + str(obj.stdout)
    print obj.files_created
    print obj.files_updated
#    PmagPy_tests.clean_house()

def complete_histplot_test():
    # no useful stdout : (
    # done
    print "Testing histplot.py"
    histplot_infile = 'extra_histplot_sample.out'
    histplot_reference = "{'hist.svg': <FoundFile ./new-test-output:hist.svg>}"
    histplot_wrong = "wrong"
    histplot = Plot('histplot.py', histplot_infile, histplot_reference, histplot_wrong, 'a', False)
    histplot_plot = histplot.run_program(plot=True)
    histplot.check_output(histplot_plot, histplot.ref_out)
    histplot_unittest = Bad_test(histplot)
    histplot_unittest.test_for_error()

def complete_irmaq_magic_test():
    # NO STDOUT
    # WD
    # DONE
    print "Testing irmaq_magic.py"
    irmaq_magic_infile = 'irmaq_magic_measurements.txt'
    irmaq_magic_reference = "{'U1359A_LP-IRM.svg': <FoundFile ./new-test-output:U1359A_LP-IRM.svg>}"
    irmaq_magic_wrong = 8
    irmaq_magic = Plot('irmaq_magic.py', irmaq_magic_infile, irmaq_magic_reference, irmaq_magic_wrong, 'a', True)
    irmaq_magic_plot = irmaq_magic.run_program(plot=True)
    irmaq_magic.check_output(irmaq_magic_plot, irmaq_magic.ref_out)
    irmaq_magic_unittest = Bad_test(irmaq_magic)
    irmaq_magic_unittest.test_for_error()



def complete_lnp_magic_test():
    #WD
    # long output, so tests output against a file instead of a string or list
    # DONE
    print "Testing lnp_magic.py"
    lnp_magic_infile = 'lnp_magic_pmag_specimens.txt'
    lnp_magic_reference = PmagPy_tests.file_parse_by_word(file_prefix + 'lnp_magic_output_correct.txt')
    lnp_magic_wrong = [1, 2, 3, 4, 5]
    lnp_magic = Plot('lnp_magic.py', lnp_magic_infile, lnp_magic_reference, lnp_magic_wrong, None, True, '-crd', 'g', '-P')
    output = lnp_magic.run_program()
    clean_output = PmagPy_tests.output_parse(output)
    print clean_output
    print lnp_magic_reference
    PmagPy_tests.compare_two_lists(clean_output, lnp_magic_reference)
    lnp_magic_unittest = Bad_test(lnp_magic)
    lnp_magic_unittest.test_for_error()
# this works but the problem is if even a few words change..... then Lisa has to re enter the correct output

def complete_lowrie_test():
    # doesn't produce stdout : (
    # can't actually save anything
    # DONE
    print "Testing lowrie.py"
    lowrie_infile = 'lowrie_example.dat'
    lowrie_reference = """318-U1359A-002H-1-W-109
S[a]ve figure? [q]uit, <return> to continue"""
    lowrie_wrong = "wrong"
    lowrie = Plot('lowrie.py', lowrie_infile, lowrie_reference, lowrie_wrong, 'q', False)
    result = lowrie.run_program()
    lowrie.check_output(result, lowrie.ref_out)
    lowrie_unittest = Bad_test(lowrie)
    lowrie_unittest.test_for_error()

def complete_lowrie_magic_test():
    # WD
    # doesn't produce stdout : (
    # also, I can't save a plot because then it asks for raw input.  so stdin must equal q : (
    # DONE
    print "Testing lowrie_magic.py"
    infile = 'lowrie_magic_example.dat'
    reference = """318-U1359A-002H-1-W-109
S[a]ve figure? [q]uit, <return> to continue"""
    wrong = "1, 2, 3, 4"
    lowrie_magic = Plot('lowrie_magic.py', infile, reference, wrong, 'q', True)
    result = lowrie_magic.run_program()
    lowrie_magic.check_output(result, lowrie_magic.ref_out)
    unittest = Bad_test(lowrie_magic)
    unittest.test_for_error()

def complete_plot_cdf_test():
    # doesn't produce STDOUT
    # THIS ONE HAS CLEANER SYNTAX
    # DONE
    print "Testing plot_cdf.py"
    infile =  "plot_cdf_example.dat"
    reference = "{'CDF_.svg': <FoundFile ./new-test-output:CDF_.svg>}"
    wrong = "Not right"
    plot_cdf = Plot('plot_cdf.py', infile, reference, wrong, 'a', False)
    plot = plot_cdf.run_program(plot=True)
    plot_cdf.check_output(plot, plot_cdf.ref_out)
    plot_cdf_unittest = Bad_test(plot_cdf)
    plot_cdf_unittest.test_for_error()


def complete_plotdi_a_test():
    # no useful STDOUT
    # DONE
    print "Testing plotdi_a.py"
    plotdi_a_infile = "plotdi_a_example.dat"
    plotdi_a_reference = "{'eq.svg': <FoundFile ./new-test-output:eq.svg>}"
    plotdi_a_wrong = ['1', 'one']
    plotdi_a = Plot('plotdi_a.py', plotdi_a_infile, plotdi_a_reference, plotdi_a_wrong, 'a', False)
    plotdi_a_plot = plotdi_a.run_program(plot=True)
    plotdi_a.check_output(plotdi_a_plot, plotdi_a.ref_out)
    plotdi_a_unittest = Bad_test(plotdi_a)
    plotdi_a_unittest.test_for_error()

def complete_qqplot_test():
    # DONE
    qqplot_infile = "qqplot_example.dat"
    qqplot_reference_output = [10.12243251, 2.79670530387, 0.0558584072909, 0.0886]
    qqplot_wrong_output = "wrong"
    qqplot = Plot('qqplot.py', qqplot_infile, qqplot_reference_output, qqplot_wrong_output, 'a', False)
    qqplot_output = qqplot.run_program()
    qqplot_raw_out = str(qqplot_output).split()
    qqplot_clean_out = []
    print qqplot_raw_out
    for num, i in enumerate(qqplot_raw_out):
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
    qqplot_test = Bad_test(qqplot)
    qqplot_test.test_for_error()

def complete_quick_hyst_test():
    # no useful stdout
    # WD
    #DONE
    quick_hyst_infile = 'quick_hyst_example.dat'
    quick_hyst_reference = """IS06a-1 1 out of  8
working on t:  273
S[a]ve plots, [s]pecimen name, [q]uit, <return> to continue
 Good bye"""
    quick_hyst_wrong = "not correct"
    quick_hyst = Plot('quick_hyst.py', quick_hyst_infile, quick_hyst_reference, quick_hyst_wrong, 'q', True)
    quick_hyst_output = quick_hyst.run_program()
    quick_hyst.check_output(quick_hyst_output, quick_hyst.ref_out)
    quick_hyst_unittest = Bad_test(quick_hyst)
    quick_hyst_unittest.test_for_error()

def complete_revtest_test():
    # no useful stdout
    # LISA IS ADDING -- NOT DONE
    revtest_infile = file_prefix + 'revtest_example.dat'
    obj = env.run('revtest.py', '-f', revtest_infile, stdin='q')
    print obj.stdout

def complete_revtest_magic_test():
    # no useful stdout
    # Lisa is adding  NOT DONE
    pass

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
    site_edit = Plot('site_edit_magic.py', site_edit_magic_infile, site_edit_magic_reference, site_edit_magic_wrong, 'q', True, '-fsa', site_edit_fsa)
    output = site_edit.run_program()
    site_edit.check_output(output, site_edit.ref_out)
    site_edit_magic_test = Bad_test(site_edit)
    site_edit_magic_test.test_for_error()
#    subprocess.call(['site_edit_magic.py', '-WD', directory, '-f', site_edit_magic_infile, '-fsa', site_edit_fsa])  # the cool thing here is that the raw_input thing doesn't kill it.  The uncool thing is that it won't take a letter as standard input
# what would really be ideal is if I could run it, edit, and then run it again to see that it had removed the bad data.  But.... can't.  humph

def complete_strip_magic_test():
    #WD
    # no useful stdout
    # DONE
    strip_magic_infile = 'strip_magic_example.txt'
    strip_magic_reference = "{'strat.svg': <FoundFile ./new-test-output:strat.svg>}"
    strip_magic_wrong = "hello there"
    strip_magic = Plot('strip_magic.py', strip_magic_infile, strip_magic_reference, strip_magic_wrong, 'a', True, '-x', 'age', '-y', 'lat')
    strip_magic_plot = strip_magic.run_program(True)
    strip_magic.check_output(strip_magic_plot, strip_magic.ref_out)
    strip_magic_test = Bad_test(strip_magic)
    strip_magic_test.test_for_error()



thellier_magic_reference = """starting new specimen interpretation file:  thellier_specimens.txt
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
               
Return for next specimen 
Good bye
"""

def complete_thellier_magic_test():
    # DONE
    thellier_magic_infile = 'thellier_magic_measurements.txt'
#    thellier_magic_reference = See above
    thellier_magic_wrong = "wrong"
    thellier_magic = Plot('thellier_magic.py', thellier_magic_infile, thellier_magic_reference, thellier_magic_wrong,  'q', False)
    thellier_output = thellier_magic.run_program()
    thellier_magic.check_output(thellier_output, thellier_magic.ref_out)
    thellier_magic_unittest = Bad_test(thellier_magic)
    thellier_magic_unittest.test_for_error()
    # can be run with '-sav' option, but it takes FOREVER

def complete_vgpmap_magic_test():
    #WD
    # DONE
    vgpmap_magic_infile = 'vgpmap_magic_pmag_results.txt'
    vgpmap_magic_reference = "{'VGP_map.pdf': <FoundFile ./new-test-output:VGP_map.pdf>}"
    vgpmap_magic_wrong = "wrong"
    vgpmap_magic = Plot('vgpmap_magic.py', vgpmap_magic_infile, vgpmap_magic_reference, vgpmap_magic_wrong, 'a', True, '-prj', 'ortho')
    vgpmap_magic_plot = vgpmap_magic.run_program(plot=True)
    vgpmap_magic.check_output(vgpmap_magic_plot, vgpmap_magic.ref_out)
    vgpmap_magic_unittest = Bad_test(vgpmap_magic)
    vgpmap_magic_unittest.test_for_error()
#    obj = env.run('vgpmap_magic.py', '-WD', directory, '-f', vgpmap_magic_infile, '-crd', 'g', '-prj', 'ortho', '-eye', '60', '0', '-sym', 'ko', '10', '-fmt', 'png', stdin='a')


zeq_magic_reference="""sr01a1 0 out of  177
    looking up previous interpretations...
Specimen  N    MAD    DANG  start     end      dec     inc  type  component coordinates
sr01a1 9     1.8     1.2   200.0   550.0   331.0    64.4  DE-BFL  A       g 

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

def complete_zeq_magic_test():
    # done
    zeq_magic_infile = 'zeq_magic_measurements.txt'
#    zeq_magic_reference = See above
    zeq_magic_wrong = "wrong"
    fsa = 'zeq_magic_er_samples.txt'
    fsp = 'zeq_magic_specimens.txt' 
    zeq_magic = Plot('zeq_magic.py', zeq_magic_infile, zeq_magic_reference, zeq_magic_wrong, 'q', True, '-fsa', fsa, '-fsp', fsp, '-crd', 'g')
    zeq_magic_output = zeq_magic.run_program()
    zeq_magic.check_output(zeq_magic_output, zeq_magic_reference)
    zeq_magic_unittest = Bad_test(zeq_magic)
    zeq_magic_unittest.test_for_error()
# could do the below, but it takes forever and creates a TON of files
#    extra_zeq_magic = Plot('zeq_magic.py', zeq_magic_infile, zeq_magic_reference, zeq_magic_wrong, None, True, '-fsa', fsa, '-fsp', fsp, '-sav')


def do_unittest():
    unittest.main(module='Plotting')

#print "Almost at the end"

#print "But don't print me"



# FOR MYSTERIOUS REASONS, having do_unittest() makes the whole program run twice.  

def complete_working_test():
    complete_ani_depthplot_test()
    complete_foldtest_test()
    complete_histplot_test()
#    complete_hysteresis_magic_test()  # looks like I moved this, not sure where
    complete_irmaq_magic_test()
    complete_lnp_magic_test()
    complete_lowrie_test()
    complete_lowrie_magic_test()
    complete_plot_cdf_test()
    complete_plotdi_a_test()
    complete_qqplot_test()
    complete_quick_hyst_test()
    complete_revtest_test()
    complete_strip_magic_test() # error when run with the lot, but works fine alone???  update: now fine.  huh
    complete_thellier_magic_test()
    complete_vgpmap_magic_test()
    complete_zeq_test()
    complete_zeq_magic_test()  

if __name__ == '__main__':
#    pass
    complete_working_test()


"""
z = 0
for i in a_list:
    lower_bound = reference[z][0]
    upper_bound = reference[z][1]
    print lower_bound, upper_bound
    i = str(i)
    if i > lower_bound and i < upper_bound:
        print "OK"
    z += 1
"""   

"""
obj.stdout[-115:-46]
u'\n   38.9  =>     58.8 _    48.1 ^    66.7:  1.4679 _ 1.3231 ^ 1.9259\n'
>>> obj.stdout[-113:-47]
u'  38.9  =>     58.8 _    49.0 ^    67.6:  1.4679 _ 1.3117 ^ 1.9791'
>>> obj.stdout[-113:-47]
u'  38.9  =>     58.8 _    47.9 ^    67.8:  1.4679 _ 1.2849 ^ 1.9088'
"""





