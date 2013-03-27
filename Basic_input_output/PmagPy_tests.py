#! /usr/bin/env python                                                                                                                
# don't necessarily need all of these
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'


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

# this function is used to deal with the changing versions of pmagpy
def pmagpy_strip(a_list):
    new_list = []
    for i in a_list:
        if "pmagpy" in i:
            pass
        else:
            new_list.append(i)
    return new_list

def file_parse_by_word_and_pmagpy_strip(a_file): # both parses file, AND strips pmagpy
    print "parsing file: " + str(a_file)
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

def lowercase_all(a_list):
    new_list = []
#    print type(new_list)
 #   print type(a_list)
    for i in a_list:
  #      print type(i)
        n = str(i).lower()
        new_list.append(n)
    return new_list
        
li = ["he", "SHe", "It"]
lowercase_all(li)

def find_a_program(name):
    name = name.lower()
    name = name.strip(".py")
    full_name = "complete_" + name + "_test():"
    Rename = file_parse_by_word(file_prefix + "Rename_me.py")
    new_rename = lowercase_all(Rename)
    print new_rename
    print "name: " + str(name)
    print "full name:" + str(full_name)
    if full_name in new_rename:
        print name + " occurs in Rename_me.py"
    Extra_output = file_parse_by_word(file_prefix + "Extra_output.py")
    new_extra_output = lowercase_all(Extra_output)
    if full_name in new_extra_output:
        print name + " occurs in Extra_output.py"
    Plotting = file_parse_by_word(file_prefix + "Plotting.py")
    new_plotting = lowercase_all(Plotting)
    if full_name in new_plotting:
        print name + " occurs in Plotting.py"
    Bootstrap_plotting = file_parse_by_word(file_prefix + "Bootstrap_plotting.py")
    new_bootstrap_plotting = lowercase_all(Bootstrap_plotting)
    if full_name in new_bootstrap_plotting:
        print name + " occurs in Bootstrap_plotting.py"
    print "end"



if __name__ == "__main__":
    print "Please type the name of the program test you wish to find"
    print "You may enter either: program.py, or: program. No quotation marks, case does not matter"
    search_item = str(raw_input("what program are you looking for?   "))
    find_a_program(search_item)
