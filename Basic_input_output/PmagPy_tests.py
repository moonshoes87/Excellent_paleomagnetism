#! /usr/bin/env python                                                                                                                
# don't necessarily need all of these
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess

#class Basic_test():
# iterates through a list of tuples with files, and compares them.  Order is: (output, correct_reference, incorrect_reference)
def iterate_through(some_list):
    print "Iterating through: " + str(some_list)
    z = 0
    for i in some_list:
        thing = file_parse(some_list[z][0])
        correct_thing = file_parse(some_list[z][1])
        incorrect_thing = file_parse(some_list[z][2])
        # for line in correct thing?? and loop it again
        for n, line in enumerate(thing):
            if line == correct_thing[n]:
                pass
            else:
                print "output was: "
                print line
                print "output should have been: "
                print correct_thing[n]
                raise NameError
        if thing != incorrect_thing:
            pass
        else:
            print "Iterate_through() did not catch the difference between " + str(some_list[z][0]) + " and " + str(some_list[z][2])
            print "Diff is: "
            subprocess.call(['diff', some_list[z][0], some_list[z][2]])
            raise NameError

         
        """        
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
        """

def file_parse(the_file):
    data = open(the_file, 'rU').readlines()
    print("Parsing file:", the_file)
    clean_file = []
    for l in data:
        new_line = l.strip('\n')
        new_line = new_line.strip(" ")
        clean_file.append(new_line)
    return clean_file # returns a list.  each line is a list item


def file_parse_by_word(the_file):
    data = open(the_file, 'rU').readlines()
    clean_data = []
    for line in data:
        line = line.split()
        clean_data += line
#    clean_file = str(data)
    return clean_data # returns a list.  each word is an item


def output_parse(the_output):
    data = str(the_output)
    data = data.split()
    return data # returns a list.  each word is an item.  


def pmagpy_strip(a_file):
    data = file_parse_by_word(a_file)
  #  print data
    end_data = []
    for d in data:
        if "pmagpy" in d:
            pass
        else:
            end_data.append(d)
    return end_data

def clean_house():
    print "CLEANING HOUSE"
    print "-"
    print "-"
    print "-"
    subprocess.call(['rm', '-rf',  'new-test-output/']) # add long path name???

def test_for_bad_file(output):
    output = str(output)
    if "bad file" in output:
        raise NameError("Output said 'bad file'")



def compare_two_lists(output, correct_output):
    print "Comparing two lists"
    for num, i in enumerate(output):
        if i == correct_output[num]:
            print i, correct_output[num]
#            print "Lists were the same"
        else:
            print "Output contained: " + str(i) + " where it should have had " + str(correct_output[num])
            print "Error raised"
            raise ValueError("Wrong output")


universal_variable = "sup"
#put iterate_through, parse_file, test_help, and so on, in here.
