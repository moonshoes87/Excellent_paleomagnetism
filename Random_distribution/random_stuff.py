#! /usr/bin/env python

from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest

file_prefix = '/users/Nebula/Python/Random_distribution/'

#class Random_stuff(Basic_input_output):

def fisher_test():
    obj = env.run('fisher.py', '-k', '30', '-n', '10')
#    obj.stdout = '175, 119'
    output = obj.stdout
    print output
    length = len(output)
    print("length of output: " + str(length))
    if length == 170:
        print "fisher.py appears to work"
    else:
        raise(NameError, "fisher.py is producing the wrong amount of output")

def fishrot_test():
    obj1 = env.run('fishrot.py', '-n', '5', '-D', '23', '-I', '41', '-k', '50')
    output1 = obj1.stdout
    obj2 = env.run('fishrot.py', '-n', '5', '-D', '23', '-I', '41', '-k', '50')
    output2 = obj2.stdout
    print output1
    print len(output1)
    print output2
    print len(output2)
    # they should be random, thus different
    if output1 == output2:
        print "NOOOOOOOOO"
    # but they should be the same length, because of the -n 5 arguments
    if len(output1) == len(output2):
        print "Fishrot.py is producing the correct amount of output"
    else:
        raise(NameError, "Fishrot.py is producing the wrong amount of output")
    obj3 = env.run('fishrot.py')
    output3 = obj3.stdout
    obj4 = env.run('fishrot.py')
    output4 = obj4.stdout
    print output3, "-----", output4
    print len(output3), len(output4)
    if output3 != output4:
        print "Fishrot.py distributions appear to be random"
    else:
        raise(NameError, "Fishrot.py produced identical output twice in a row")

    # this looks like a decent set up for these random distribution ones....
    # add in an option to test the -h, and -i options.
    # if the rest of the possible command line options all have default values, maybe I'll just test them once with defaults and once with Lisa's examples?


# run each four times -- twice with default options, twice with Lisa example options


def gaussian_test():
    obj1 = env.run('gaussian.py', '-s', '3', '-n', '100', '-m', '10.', '-F', 'guass.out')
    output1 = obj1.stdout
    o1 = len(output1.split())
    print "output1: "+ str(output1)
    print("output 1 length: ", o1)
    print obj1.files_created
    obj2 = env.run('gaussian.py', '-s', '3', '-n', '95', '-m', '10.')
    output2 = obj2.stdout
    o2 = len(output2.split())
    print "output2: "+ str(output2)
    print "length of output 2: ", o2
    print obj2.files_created
    obj3 = env.run('gaussian.py', '-s', '3', '-n', '95', '-m', '10.',)
    output3 = obj3.stdout
    o3 = len(output3.split())
    print "output3: " + str(output3)
    print "Output 3 length: ", o3
    print obj3.files_created
    obj4 = env.run('gaussian.py', '-n', '4')
    output4 = obj4.stdout
    o4 = len(output4.split())
    # checking to see if files were created when they were supposed to, and not otherwise
    if obj1.files_created:
        print "Gaussian.py created a file"
    else:
        raise(NameError, "Gaussian.py failed to create a file with the '-F' flag")
    if obj2.files_created or obj3.files_created or obj4.files_created:
        raise(NameError, "Gaussian.py created a file when the '-F' flag was not present")
    # checking to see that distribution is indeed random
    if output2 != output3:
        print "Distributions appear to be random"
    else:
        raise(NameError, "Gaussian.py produced identical distributions")
    # checking to see if gaussian.py is responding correctly to the requested amount of output
    if o1 == 0 and o2 == 95 and o3 == 95 and o4 == 4:
        print "Gaussian.py is giving the correct amount of output"
    else:
        raise(NameError, "Gaussian.py is giving the wrong amount of output")
    # also add -h option (no -i)
    # another way to test the additional command line options?
    # -n is how many lines of output it makes, so I can test that. len(o) should equal the number that follows -n
    



def run_tests():
    gaussian_test()
    fishrot_test()
    fisher_test()



