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
class Plot(object):
     def __init__(self, name, infile, ref_out, wrong_out, stdin, WD, *args):
         self.name = name
         if infile != None:
              self.infile = file_prefix + infile
         else:
              self.infile = None
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
          print "running program"
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

     def check_output(self, actual_out, reference_out):
          print "checking output"
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


def complete_zeq_test(): # MOVED
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


def complete_ani_depthplot_test(): # MOVED
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

def complete_basemap_magic_test(): # MOVED
     basemap_magic_infile = 'basemap_example.txt'
     basemap_magic_reference = "{'Site_map.pdf': <FoundFile ./new-test-output:Site_map.pdf>}"
     basemap_magic_wrong = "wrong"
     basemap_magic = Plot('basemap_magic.py', basemap_magic_infile, basemap_magic_reference, basemap_magic_wrong, 'a', True)
     basemap_plot = basemap_magic.run_program(plot=True)
     basemap_magic.check_output(basemap_plot, basemap_magic_reference)
     basemap_magic_unittest = Bad_test(basemap_magic)
     basemap_magic_unittest.test_for_error()

def complete_biplot_magic_test():#MOVED
     # not WD
     biplot_magic_infile = 'biplot_magic_example.dat'
     biplot_magic_reference = """LP-X  selected for X axis
LT-AF-I  selected for Y axis
All
measurement_magn_mass  being used for plotting Y
measurement_chi_mass  being used for plotting X.
S[a]ve plots, [q]uit,  Return for next plot Good-bye"""
     biplot_magic_wrong = 1235.
     biplot_magic = Plot('biplot_magic.py', biplot_magic_infile, biplot_magic_reference, biplot_magic_wrong, 'q', False, '-x', 'LP-X', '-y', 'LT-AF-I') 
     biplot_magic_output = biplot_magic.run_program()
     biplot_magic.check_output(biplot_magic_output, biplot_magic.ref_out)
     biplot_magic_unittest = Bad_test(biplot_magic)
     biplot_magic_unittest.test_for_error()

def complete_chartmaker_test(): #MOVED
     chartmaker_infile = None
     chartmaker_reference = "{'chart.txt': <FoundFile ./new-test-output:chart.txt>}"
     chartmaker_wrong = "wrong"
     chartmaker = Plot('chartmaker.py', chartmaker_infile, chartmaker_reference, chartmaker_wrong, 'q', False)
     plot = chartmaker.run_program(plot=True)
     chartmaker.check_output(plot, chartmaker.ref_out)
     clean_output = PmagPy_tests.file_parse(file_prefix + 'new-test-output/chart.txt')
     reference_output = PmagPy_tests.file_parse(file_prefix + 'chartmaker_reference_correct.txt')
     PmagPy_tests.compare_two_lists(clean_output, reference_output) # compares a clean version of the prototype file with what we just created
     chartmaker_unittest = Bad_test(chartmaker)
     chartmaker_unittest.test_for_error()
     

def complete_chi_magic_test(): # MOVED
     chi_magic_infile = 'chi_magic_example.dat'
     chi_magic_reference = "{'IRM-OldBlue-1892_2.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_2.svg>, 'IRM-OldBlue-1892_3.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_3.svg>, 'IRM-OldBlue-1892_1.svg': <FoundFile ./new-test-output:IRM-OldBlue-1892_1.svg>}"
     chi_magic_wrong = "wrong"
     chi_magic = Plot('chi_magic.py', chi_magic_infile, chi_magic_reference, chi_magic_wrong, 'a', False)
     plot = chi_magic.run_program(plot=True)
     chi_magic.check_output(plot, chi_magic.ref_out)
     chi_magic_unittest = Bad_test(chi_magic)
     chi_magic_unittest.test_for_error()

def complete_common_mean_test(): # MOVED
     common_mean_infile = 'common_mean_ex_file1.dat'
     common_mean_reference = "{'CD_X.svg': <FoundFile ./new-test-output:CD_X.svg>, 'CD_Y.svg': <FoundFile ./new-test-output:CD_Y.svg>, 'CD_Z.svg': <FoundFile ./new-test-output:CD_Z.svg>}"
     common_mean_wrong = "wrong"
     common_mean_f2 = file_prefix + 'common_mean_ex_file2.dat'
     common_mean = Plot('common_mean.py', common_mean_infile, common_mean_reference, common_mean_wrong, 'a', False, '-f2', common_mean_f2)
     plot = common_mean.run_program(plot=True)
     common_mean.check_output(plot, common_mean.ref_out)
     common_mean_unittest = Bad_test(common_mean)
     common_mean_unittest.test_for_error()
     # testing with -dir instead of -f2
     obj = env.run('common_mean.py', '-f', file_prefix + common_mean_infile, '-dir', '0', '9.9', stdin='a')
     output2 = str(obj.files_updated)
     output_with_dir_option = "{'CD_X.svg': <FoundFile ./new-test-output:CD_X.svg>, 'CD_Y.svg': <FoundFile ./new-test-output:CD_Y.svg>, 'CD_Z.svg': <FoundFile ./new-test-output:CD_Z.svg>}"
     if output2 == output_with_dir_option:
          print "OK"
     else:
          raise NameError("running common_mean.py with -dir 0 9.9 did not produce expected plots")

def complete_core_depthplot_test(): # MOVED
#core_depthplot.py -f core_depthplot_example.dat -LP AF 15
     core_depthplot_infile = 'core_depthplot_example.dat'
     core_depthplot_reference = "{'DSDP Site 522_m:_LT-AF-Z_core-depthplot.svg': <FoundFile ./new-test-output:DSDP Site 522_m:_LT-AF-Z_core-depthplot.svg>}"
     core_depthplot_wrong = "wrong"
     core_depthplot_fsa = 'core_depthplot_er_samples.txt'
     core_depthplot = Plot('core_depthplot.py', core_depthplot_infile, core_depthplot_reference, core_depthplot_wrong, 'a', True, '-fsa', core_depthplot_fsa, '-LP', 'AF', '15')
#     obj = env.run('core_depthplot.py', '-WD', directory, '-LP',  'AF', '15', '-log', '-d', '50', '150', '-ts', 'gts04', '23', '34', '-D', '-f', core_depthplot_infile, '-fsa', core_depthplot_fsa, stdin='a')
#     print obj.files_created
 #    print obj.stdout
     plot = core_depthplot.run_program(plot=True)
     core_depthplot.check_output(plot, core_depthplot.ref_out)
     core_depthplot_unittest = Bad_test(core_depthplot)
     core_depthplot_unittest.test_for_error()

def complete_dayplot_magic_test(): # MOVED
     dayplot_magic_infile = 'dayplot_magic_example.dat'
     dayplot_magic_reference = "{'LO:_unknown_SI:__SA:__SP:__TY:_day_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_day_.svg>, 'LO:_unknown_SI:__SA:__SP:__TY:_S-Bc_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_S-Bc_.svg>, 'LO:_unknown_SI:__SA:__SP:__TY:_S-Bcr_.svg': <FoundFile ./new-test-output:LO:_unknown_SI:__SA:__SP:__TY:_S-Bcr_.svg>}"
     dayplot_magic_wrong = "wrong"
     dayplot_magic = Plot('dayplot_magic.py', dayplot_magic_infile, dayplot_magic_reference, dayplot_magic_wrong, 'a', True)
     plot = dayplot_magic.run_program(plot=True)
     dayplot_magic.check_output(plot, dayplot_magic.ref_out)
     dayplot_magic_unittest = Bad_test(dayplot_magic)
     dayplot_magic_unittest.test_for_error()


def complete_dmag_magic_test(): # MOVED
     dmag_magic_infile = 'dmag_magic_example.dat'
     dmag_magic_reference = "{'McMurdo_LT-AF-Z.svg': <FoundFile ./new-test-output:McMurdo_LT-AF-Z.svg>}"
     dmag_magic_wrong = "wrong"
     dmag_magic = Plot('dmag_magic.py', dmag_magic_infile, dmag_magic_reference, dmag_magic_wrong, 'a', False)
     plot = dmag_magic.run_program(plot=True)
     dmag_magic.check_output(plot, dmag_magic.ref_out)
     dmag_magic_unittest = Bad_test(dmag_magic)
     dmag_magic_unittest.test_for_error()

def complete_eqarea_test():
     eqarea_infile = 'eqarea_example.dat'
     eqarea_reference = "{'eq.svg': <FoundFile ./new-test-output:eq.svg>}"
     eqarea_wrong = "wrong"
     eqarea = Plot('eqarea.py', eqarea_infile, eqarea_reference, eqarea_wrong, 'a', False)
     plot = eqarea.run_program(plot=True)
     eqarea.check_output(plot, eqarea.ref_out)
     eqarea_unittest = Bad_test(eqarea)
     eqarea_unittest.test_for_error()

def complete_eqarea_ell_test():
     eqarea_ell_infile = 'eqarea_ell_example.dat'
     eqarea_ell_reference ="""Zdec   137.8
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
     eqarea_ell = Plot('eqarea_ell.py', eqarea_ell_infile, eqarea_ell_reference, eqarea_ell_wrong, 'q', False, '-ell', 'B')
     output = eqarea_ell.run_program()
     print output
     eqarea_ell.check_output(output, eqarea_ell.ref_out)
     eqarea_ell_unittest = Bad_test(eqarea_ell)
     eqarea_ell_unittest.test_for_error()


def complete_eqarea_magic_test():
     print "Testing eqarea_magic.py"
     eqarea_magic_infile = 'eqarea_magic_example.dat'
     eqarea_magic_reference = "{'LO:_Snake River_SI:__SA:__SP:__CO:_gu_TY:_eqarea_.svg': <FoundFile ./new-test-output:LO:_Snake River_SI:__SA:__SP:__CO:_gu_TY:_eqarea_.svg>}"
#['24', 'records', 'read', 'from', '/Users/nebula/Python/Basic_input_output/eqarea_magic_example.dat', 'All', 'sr01', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T:LP-PI-ALT-PTRM:LP-PI-TRM-ZI', '330.1', '64.9', 'sr03', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '151.8', '-57.5', 'sr04', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '16.5', '54.6', 'sr09', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '14.6', '77.9', 'sr11', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '346.3', '73.8', 'sr12', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '15.3', '44.8', 'sr16', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '347.4', '65.6', 'sr21', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '172.5', '-66.9', 'sr22', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '6.3', '29.7', 'sr23', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '14.5', '45.5', 'sr24', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '163.3', '-62.2', 'sr25', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '2.9', '61.9', 'sr26', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '358.6', '62.5', 'sr28', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '197.4', '-51.2', 'sr29', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '9.5', '62.8', 'sr30', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T:LP-PI-ALT-PTRM:LP-PI-TRM-ZI', '7.5', '66.7', 'sr31', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '23.2', '54.0', 'sr34', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T:LP-PI-ALT-PTRM:LP-PI-TRM-ZI', '205.8', '-49.4', 'sr36', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '197.6', '-65.5', 'sr39', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T:LP-PI-ALT-PTRM:LP-PI-TRM-ZI', '188.1', '-47.2', 'sr40', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '192.9', '-60.7', 'Normal', 'Pole', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '6.1', '59.6', 'Reverse', 'pole', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '185.1', '-58.8', 'Grand', 'Mean', 'pole', 'GM-ARAR-AP:LP-DC5:LP-DIR-AF:LP-DIR-T', '5.7', '59.3', 'mode', '1', 'Zdec', '111.3', 'Edec', '206.2', 'Eta', '7.7', 'n', '1', 'Einc', '28.9', 'Zinc', '8.8', 'Zeta', '3.3', 'dec', '6.1', 'inc', '59.5', 'mode', '2', 'Zdec', '248.2', 'Edec', '150.4', 'Eta', '4.2', 'n', '1', 'Einc', '26.4', 'Zinc', '15.3', 'Zeta', '8.1', 'dec', '185.1', 'inc', '-58.9', 'S[a]ve', 'to', 'save', 'plot,', '[q]uit,', 'Return', 'to', 'continue:']
     eqarea_magic_wrong = "wrong"
     eqarea_magic = Plot('eqarea_magic.py', eqarea_magic_infile, eqarea_magic_reference, eqarea_magic_wrong, 'a', True, '-obj', 'loc', '-crd', 'g', '-ell', 'Be')
     output = eqarea_magic.run_program(plot=True)
     eqarea_magic.check_output(output, eqarea_magic.ref_out)
     # this seems to be bootstrap-y
     # SHOULD I TEST THIS IN BOOTSTRAP PLOTTING??????????


def complete_fishqq_test():
     fishqq_infile = 'fishqq_example.dat'
     fishqq_reference = "{'exp1.svg': <FoundFile ./new-test-output:exp1.svg>, 'unf1.svg': <FoundFile ./new-test-output:unf1.svg>}"
     print fishqq_reference
     fishqq_wrong = "wrong"
     fishqq = Plot('fishqq.py', fishqq_infile, fishqq_reference, fishqq_wrong, 'a', False)
     plot = fishqq.run_program(plot=True)
     fishqq.check_output(plot, fishqq.ref_out)
     fishqq_unittest = Bad_test(fishqq)
     fishqq_unittest.test_for_error()
     
def complete_foldtest_magic_test():
     foldtest_magic_infile = 'foldtest_magic_example.txt'
     foldtest_magic_reference = None
     foldtest_magic_wrong = [1, 2, 3]
     foldtest_magic_fsa = 'foldtest_magic_er_samples.txt'
     foldtest_magic = Plot('foldtest_magic.py', foldtest_magic_infile, foldtest_magic_reference, foldtest_magic_wrong, 'a', True,  '-fsa', foldtest_magic_fsa, '-n', '100')
     foldtest_magic.run_program()
     # this works, in this folder: foldtest_magic.py -f foldtest_magic_example.txt -fsa foldtest_magic_er_samples.txt
complete_foldtest_magic_test()
     



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
    complete_biplot_magic_test()
    complete_chartmaker_test()
    complete_chi_magic_test()
    complete_common_mean_test()
    complete_core_depthplot_test()
    complete_dayplot_magic_test()
    complete_dmag_magic_test()
    complete_eqarea_test()
    complete_eqarea_ell_test() # has stdout : )
    complete_eqarea_magic_test() # bootstrap-y... may wish to update this
    complete_fishqq_test()
    complete_foldtest_test()
    complete_histplot_test()
    complete_irmaq_magic_test()
    complete_lnp_magic_test()
    complete_lowrie_test()
    complete_lowrie_magic_test()
    complete_plot_cdf_test()
    complete_plotdi_a_test() # had a weird error, but not when run alone.
    complete_qqplot_test()
    complete_quick_hyst_test()
    complete_revtest_test()
    complete_strip_magic_test() # error when run with the lot, but works fine alone???  update: now fine.  huh
    complete_thellier_magic_test()
    complete_vgpmap_magic_test()
    complete_zeq_test()
    complete_zeq_magic_test()  

if __name__ == '__main__':
    pass
#    complete_working_test()



