#! /usr/bin/env python                                                                                                                        
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import Basic_input_output
import PmagPy_tests

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'

nothing = """
def file_parse(the_file):
    data = open(the_file, 'rU').readlines()
    print("Parsing file:", the_file)
    clean_file = []
    for l in data:
        new_line = l.strip('\n')
        clean_file.append(new_line)
    return clean_file
"""

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


def complete_ani_depthplot_test():
    # doesn't produce standard output
    # WD
    print "Testing ani_depthplot.py"
    obj = env.run('ani_depthplot.py', '-WD', directory, '-f', 'ani_depthplot_rmag_anisotropy.txt', '-fsa', 'ani_depthplot_er_samples.txt', '-sav') #stdin="a")
    print obj.stdout
    print obj.files_created
    # need to edit ani_depthplot to return the value of interest

ten_thousand_1 = ['0.34040287', '29.6', '14.5', '34.5', '171.3', '67.2', '6.7', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.5', '26.7', '13.3', '10.8', '293.8', '12.1', '0.32423124', '296.2', '12.8', '10.9', '178.7', '63.8', '4.9', '31.5', '22.4']
ten_thousand_2 = ['0.34040287', '29.6', '14.5', '33.7', '171.2', '67.4', '6.6', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.6', '294.4', '12.2', '0.32423124', '296.2', '12.8', '10.7', '179.2', '63.5', '4.9', '31.6', '22.8']
thirty_thousand_1 = ['0.34040287', '29.6', '14.5', '33.8', '171.3', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '26.9', '13.3', '10.8', '294.0', '12.2', '0.32423124', '296.2', '12.8', '10.9', '179.5', '63.1', '5.0', '31.7', '23.2']
thirty_thousand_2 = ['0.34040287', '29.6', '14.5', '33.9', '171.2', '67.3', '6.7', '296.0', '13.4', '0.33536589', '166.3', '70.5', '24.2', '27.3', '13.2', '10.8', '294.4', '12.3', '0.32423124', '296.2', '12.8', '10.8', '179.4', '63.3', '5.0', '31.6', '23.1']
ninety_thousand = ['0.34040287', '29.6', '14.5', '33.5', '171.0', '67.3', '6.6', '296.0', '13.5', '0.33536589', '166.3', '70.5', '24.1', '27.0', '13.3', '10.7', '294.1', '12.2', '0.32423124', '296.2', '12.8', '10.8', '179.2', '63.5', '4.9', '31.6', '22.9']

aniso_magic_reference_list = [(.3403, .3402), (29.5, 29.7), (14.4, 14.6), (33., 35.), (170.9, 171.4), (67., 67.4), (6.5, 6.8), (295.9,296.1), (13.3, 13.6), (0.33535, .33537), (166.2, 166.4), (70.4, 70.6), (23.9, 24.7), (26., 28.), (13.1, 13.4), (10.5, 10.9), (293., 295.), (12., 12.5), (0.324231, .324232), (296.1, 296.3), (12.7, 12.9), (10.6, 11), (178, 180), (63., 64.), (4.8, 5.1), (31.3, 31.9), (21., 24.)]
def complete_aniso_magic_test():
    print "Testing complete_aniso_magic.py"
    # WD
    obj = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_dike_anisotropy.txt', '-F', 'aniso_magic_rmag_anisotropy.txt', '-nb', '2000','-gtc', '110', '2', '-par', '-v', '-crd', 'g', '-P') #stdin='q')
    print obj.stdout
   # obj2 = env.run('aniso_magic.py', '-WD', directory, '-f', 'aniso_magic_sed_anisotropy.txt', '-F', 'aniso_magic_rmag_results.txt', '-d', '3', '0', '90', '-v', '-crd', 'g', stdin='a')
    #print obj2.stdout
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
    # can use stdin = 'q', or 'a' (to save).  Then can optionally test for files_created/files_updated



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


def complete_foldtest_test():
    # doesn't produce stdout :(
    print "Testing foldtest.py"
    foldtest_infile = file_prefix + 'foldtest_example.dat'
    obj = env.run('foldtest.py', '-f', foldtest_infile, '-n', '50', stdin='a')
    print "Stdout: " + str(obj.stdout)
    print obj.files_created
    print obj.files_updated
#    PmagPy_tests.clean_house()

def complete_histplot_test():
    # no useful stdout : (
    print "Testing histplot.py"
    histplot_infile = file_prefix + 'extra_histplot_sample.out'
    obj = env.run('histplot.py', '-f', histplot_infile, stdin='a')
    print "Stdout: " + str(obj.stdout)


def complete_hysteresis_magic_test():
    # hysteresis_magic.py needs additional lisa fixing
    # doesn't seem to produce useful stdout : (
    # WD
    print "Testing hysteresis_magic.py"
    hysteresis_magic_infile = 'hysteresis_magic_example.dat'
    print hysteresis_magic_infile
    obj = env.run('hysteresis_magic.py', '-WD', directory, '-f', hysteresis_magic_infile, '-sav')
    # stdin = 'a', kind of doesn't work because there is more raw input later
    print "stdout: " + str(obj.stdout)
    print obj.files_created
    print obj.files_updated
#    PmagPy_tests.clean_house()

def complete_irmaq_magic_test():
    # NEEDS STDOUT
    # WD
    print "Testing irmaq_magic.py"
    irmaq_magic_infile = 'irmaq_magic_measurements.txt'
    obj = env.run('irmaq_magic.py', '-WD', directory,  '-f', irmaq_magic_infile, stdin='a')
    print obj.stdout
    print obj.files_created
#    PmagPy_tests.clean_house()

def complete_lnp_magic_test():
    #WD
    print "Testing lnp_magic.py"
    lnp_magic_infile = 'lnp_magic_pmag_specimens.txt'
    obj = env.run('lnp_magic.py', '-WD', directory, '-f', lnp_magic_infile, '-crd', 'g', '-P')
    # -P means no plot.  
 #   print obj.stdout
    a_list = str(obj.stdout).split()
#    print a_list
    for i, z in enumerate(a_list):
        if z == lnp_magic_reference[i]:
            pass
        else:
            print "Error raised"
            print "output was: " + z + " but should have been: " + lnp_magic_reference[i]
# this works but the problem is if even a few words change..... then Lisa has to re enter the correct output
# make a utility function that converts correct output into the right sort of format...  basically, new_list = str(output).split()

lnp_magic_reference = ['sv01', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv01', '0', '5', '286', '6.6', '179.0', '-54.3', '4.9948', '%', 'tilt', 'correction:', '0', 'sv02', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv02', '4', '2', '113', '6.6', '338.8', '38.6', '5.9647', '%', 'tilt', 'correction:', '0', 'sv03', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv03', '5', '3', '108', '5.5', '344.0', '53.1', '7.9491', '%', 'tilt', 'correction:', '0', 'sv04', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv04', '5', '0', '286', '4.5', '346.9', '50.7', '4.9860', '%', 'tilt', 'correction:', '0', 'sv05', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv05', '5', '3', '165', '4.5', '164.1', '-51.3', '7.9667', '%', 'tilt', 'correction:', '0', 'sv06', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv06', '2', '3', '81', '9.7', '351.4', '-32.0', '4.9691', '%', 'tilt', 'correction:', '0', 'sv07', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv07', '7', '1', '318', '3.1', '350.3', '61.8', '7.9796', '%', 'tilt', 'correction:', '0', 'sv08', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv08', '7', '0', '151', '4.9', '165.7', '-46.1', '6.9603', '%', 'tilt', 'correction:', '0', 'sv09', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv09', '5', '0', '10', '26.2', '251.6', '-57.1', '4.5791', '%', 'tilt', 'correction:', '0', 'sv10', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv10', '0', '5', '65', '13.9', '188.9', '-47.3', '4.9770', '%', 'tilt', 'correction:', '0', 'sv11', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv11', '2', '2', '116', '10.0', '193.6', '-43.2', '3.9827', '%', 'tilt', 'correction:', '0', 'sv12', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv13', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv15', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv15', '6', '0', '175', '5.1', '352.8', '25.5', '5.9714', '%', 'tilt', 'correction:', '0', 'sv16', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv16', '4', '1', '166', '6.1', '356.0', '24.1', '4.9789', '%', 'tilt', 'correction:', '0', 'sv17', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv18', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv18', '5', '0', '704', '2.9', '192.8', '-55.9', '4.9943', '%', 'tilt', 'correction:', '0', 'sv19', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv20', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv21', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv22', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv23', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv23', '4', '1', '464', '3.7', '19.5', '29.0', '4.9925', '%', 'tilt', 'correction:', '0', 'sv24', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv24', '7', '0', '109', '5.8', '339.2', '63.7', '6.9452', '%', 'tilt', 'correction:', '0', 'sv25', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv26', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv26', '4', '2', '109', '6.7', '159.0', '-69.1', '5.9633', '%', 'tilt', 'correction:', '0', 'sv27', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv27', '4', '1', '241', '5.1', '354.0', '55.9', '4.9854', '%', 'tilt', 'correction:', '0', 'sv28', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv30', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv31', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv31', '5', '0', '394', '3.9', '12.7', '46.2', '4.9898', '%', 'tilt', 'correction:', '0', 'sv32', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv32', '5', '0', '384', '3.9', '342.9', '60.3', '4.9896', '%', 'tilt', 'correction:', '0', 'sv50', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv50', '2', '1', '1', '180.0', '266.8', '-40.9', '1.9606', '%', 'tilt', 'correction:', '0', 'sv51', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv51', '4', '0', '2', '84.3', '207.2', '-39.4', '2.6222', '%', 'tilt', 'correction:', '0', 'sv52', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv52', '4', '0', '199', '6.5', '182.7', '-54.9', '3.9850', '%', 'tilt', 'correction:', '0', 'sv53', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv53', '3', '0', '3', '86.4', '178.0', '-26.5', '2.3622', '%', 'tilt', 'correction:', '0', 'sv54', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv54', '5', '0', '30', '14.1', '175.3', '-46.7', '4.8684', '%', 'tilt', 'correction:', '0', 'sv55', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv55', '4', '0', '409', '4.5', '181.2', '-45.0', '3.9927', '%', 'tilt', 'correction:', '0', 'sv56', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv56', '4', '1', '3', '50.1', '171.1', '-68.8', '3.9527', '%', 'tilt', 'correction:', '0', 'sv57', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv57', '5', '0', '20', '17.8', '199.6', '-46.4', '4.7950', '%', 'tilt', 'correction:', '0', 'sv58', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv58', '4', '0', '570', '3.9', '182.0', '-62.3', '3.9947', '%', 'tilt', 'correction:', '0', 'sv59', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv59', '4', '0', '1128', '2.7', '178.8', '-51.3', '3.9973', '%', 'tilt', 'correction:', '0', 'sv60', 'skipping', 'site', '-', 'not', 'enough', 'data', 'with', 'specified', 'coordinate', 'system', 'sv61', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv61', '3', '1', '7', '39.5', '2.9', '77.8', '3.6408', '%', 'tilt', 'correction:', '0', 'sv62', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv62', '0', '3', '308', '38.3', '133.7', '-52.3', '2.9984', '%', 'tilt', 'correction:', '0', 'sv63', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv63', '4', '0', '489', '4.2', '351.5', '45.1', '3.9939', '%', 'tilt', 'correction:', '0', 'sv64', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv64', '6', '0', '172', '5.1', '170.4', '-51.6', '5.9710', '%', 'tilt', 'correction:', '0', 'sv65', 'Site', 'lines', 'planes', 'kappa', 'a95', 'dec', 'inc', 'sv65', '4', '1', '90', '8.3', '31.0', '54.4', '4.9611', '%', 'tilt', 'correction:', '0']

def complete_lowrie_test():
    # doesn't produce stdout : (
    print "Testing lowrie.py"
    lowrie_infile = file_prefix + 'lowrie_example.dat'
    obj = env.run('lowrie.py', '-f', lowrie_infile, stdin='q')
    print obj.stdout

def complete_lowrie_magic_test():
    # WD
    # doesn't produce stdout : (
    # also, I can't save a plot because then it asks for raw input.  so stdin must equal q : (
    print "Testing lowrie_magic.py"
    lowrie_magic_infile = 'lowrie_magic_example.dat'
    obj = env.run('lowrie_magic.py', '-WD', directory,  '-f', lowrie_magic_infile, stdin='q')
    print obj.stdout

def complete_plot_cdf_test():
    # doesn't produce STDOUT
    print "Testing plot_cdf.py"
    plot_cdf_infile = file_prefix + "plot_cdf_example.dat"
    obj = env.run("plot_cdf.py", '-f', plot_cdf_infile, stdin='a')
    print obj.stdout
    print obj.files_created

def complete_plotdi_a_test():
    # no useful STDOUT
    print "Testing plotdi_a.py"
    plotdi_a_infile = file_prefix + "plotdi_a_example.dat"
    obj = env.run("plotdi_a.py", '-f', plotdi_a_infile, stdin='a')
    print obj.stdout
    print obj.files_created

def complete_qqplot_test():
    print "Testing qqplot.py"
    qqplot_infile = file_prefix + "qqplot_example.dat"
    reference_out = ['10.12243251', '2.79670530387', '0.0558584072909', '0.0886']
    obj = env.run('qqplot.py', '-f', qqplot_infile, stdin='a')
    print obj.stdout
    the_list = str(obj.stdout).split()
    new_list = the_list[3:7]
    print the_list
    # this doesn't work because it skips over when you remove one.  the indexing gets all not fucked.
    a_cool_idea = """
    for num, i in enumerate(the_list):
        print num
        try:
            float(i)
        except ValueError:
            print str(i) + " sinks"
            the_list.remove(i)
            print the_list
    """
    if new_list == reference_out:
        print "OK!"
        print "Output: " + str(new_list)
        print "Reference: " + str(reference_out)
    # THIS IS GREAT. JUST NEEDS A UNITTEST.  

def complete_quick_hyst_test():
    # no useful stdout
    # WD
    quick_hyst_infile = 'quick_hyst_example.dat'
    obj = env.run('quick_hyst.py', '-WD', directory, '-f', quick_hyst_infile, stdin='q')
    print obj.stdout

def complete_revtest_test():
    # no useful stdout
    revtest_infile = file_prefix + 'revtest_example.dat'
    obj = env.run('revtest.py', '-f', revtest_infile, stdin='q')
    print obj.stdout

def complete_strip_magic_test():
    #WD
    # no useful stdout
    strip_magic_infile = 'strip_magic_example.txt'
    obj = env.run('strip_magic.py', '-WD', directory, '-f', strip_magic_infile, '-x', 'age', '-y', 'lat', stdin='a')
    print obj.stdout
    print obj.files_created



# the irritating thing here is making sure you have the correct returns and spaces.  
thellier_magic_output = """starting new specimen interpretation file:  thellier_specimens.txt
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
    thellier_magic_infile = file_prefix + 'thellier_magic_measurements.txt'
    obj = env.run('thellier_magic.py', '-f', thellier_magic_infile, '-sav')
    output = obj.stdout
    thing= PmagPy_tests.output_parse(output)
    print obj.stdout
    print obj.files_created
    stuff = """
    if thing == thellier_magic_output:
        print "Thellier_magic.py output as expected"
    else:
        print "Thellier_magic.py raised error"
        print "Output was: " + str(thing)
        print "Output should have been: " + thellier_magic_output
        raise NameError("Thellier_magic.py produced incorrect output")
       """
  #  print obj.files_created
    # needs unittests.  
    # also, figure out how to test help messages for these guys
    # there are a few other configurations of options....
    # this looks like a good candidate for a class

complete_thellier_magic_test()



def do_unittest():
    unittest.main(module='Plotting')

#print "Almost at the end"



#print "But don't print me"



# FOR MYSTERIOUS REASONS, having do_unittest() makes the whole program run twice.  

def complete_working_test():
#    complete_ani_depthplot_test()  NOT USEFUL YET
    complete_aniso_magic_test()
    complete_find_EI_test()
#    complete_foldtest_test()  NOT USEFUL YET
    # complete_histplot_test() NOT USEFUL YET
    complete_hysteresis_magic_test()
    complete_irmaq_magic_test()
    complete_lnp_magic_test()
    complete_lowrie_test()
    complete_lowrie_magic_test()
    complete_plot_cdf_test()
    complete_plotdi_a_test()
    complete_qqplot_test()
    complete_quick_hyst_test()
    complete_revtest_test()
    complete_strip_magic_test()
    complete_thellier_magic_test()
    #PmagPy_tests.clean_house()
    do_unittest()

if __name__ == '__main__':
    pass
#    complete_working_test()


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





