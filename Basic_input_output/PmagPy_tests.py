#! /usr/bin/env python                                                                                                                
# don't necessarily need all of these
import sys
from scripttest import TestFileEnvironment
env = TestFileEnvironment('./new-test-output')
import unittest
import subprocess

file_prefix = '/Users/nebula/Python/Basic_input_output/'
directory =  '/Users/nebula/Python/Basic_input_output'

the_variable = "hello"

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
# copy this!!!
#    subprocess.call('rm ' + directory + '/*_new.out', shell=True)
    subprocess.call('rm ' + file_prefix + 'new-test-output/*', shell=True) # add long path name???

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
        

def remove_new_outfiles(): 
    """
    gets rid of all freshly created outfiles.
    """
    subprocess.call('rm ' + directory + '/*_new.out', shell=True)


def get_short_program_name(name):
    # this doesn't work!  you would need regular expressions.  strip removes all combinations of the letters
    print "get short name"
    print name
    n = name.strip()
    print n
    n -= ".py"
    print n
    n = n.strip("complete")
    print n
    n = n.strip("_test")
    print n
    return n

def clean_program_name(name = None): 
    """
    removes extraneous stuff and gets to the command for running the test
    """
    if name == None:
        n = raw_input("name?  ")
    else:
        n = name
    print "name", name
    print "n", n
    n = str(n)
    print n
    n = n.lower()
    print n
    n = n.strip(" ")
    print n
    n = n.strip(".py")
    print n
    if "test" in n:
        if "()" in n:
            pass
        else:
            n += "()"
    else:
        n += "_test()"
    if "complete" in n:
        pass
    else:
        n = "complete_" + n
    print "final: " + str(n)
    return n

#clean_program_name("complete_angle.py")
#clean_program_name("angle")
#clean_program_name("complete_angle_test()")
#clean_program_name("angle_test")
#clean_program_name("complete_angle")
#clean_program_name("complete_Angle")
#clean_program_name()


def find_a_program(name):
    full_name = clean_program_name(name)
 #   print "FULL NAME", full_name
    Rename = file_parse_by_word(file_prefix + "Rename_me.py")
    new_rename = lowercase_all(Rename)
    print "name: " + str(name)
    print "full name:" + str(full_name)
    found = False
    if full_name in new_rename:
        found = True
        print name + " occurs in Rename_me.py"
    Extra_output = file_parse_by_word(file_prefix + "Extra_output.py")
    new_extra_output = lowercase_all(Extra_output)
    if full_name in new_extra_output:
        found = True
        print name + " occurs in Extra_output.py"
    Bootstrap = file_parse_by_word(file_prefix + "Bootstrap.py")
    new_bootstrap = lowercase_all(Bootstrap)
    if full_name in new_bootstrap:
        found = True
        print name + " occurs in Bootstrap.py"
    Random = file_parse_by_word(file_prefix + "Random.py")
    new_random = lowercase_all(Random)
    if full_name in new_random:
        found = True
        print name + " occurs in Random.py"
    if found:
        print name + " was found"
    else:
        print name + " not found.  Make sure your spelling is good!"

def run_individual_program(mapping): # takes as argument a mapping of function name to the actual function, then runs that function 
    print "running individual program!"
    try:
        ind=sys.argv.index('-r')
        run_program=sys.argv[ind+1]
        print run_program
        if ".py" in run_program:
            run_program = run_program[:-3]
        program = mapping[run_program]
        print program
        print type(program)
        program()
    except KeyError as er:
        print er
        print "Please try again.  Check spelling, etc.  Make sure to input the name of the program with no quotations or extra words: i.e.: angle, or: thellier_magic_redo"
#        break
    except Exception as ex:
        print "printing error:"
        print ex


if __name__ == "__main__":
    file_parse_by_word('hiyo.txt')
    print "Please type the name of the program test you wish to find"
    print "You may enter either: program.py, or: program. No quotation marks, case does not matter"
    search_item = str(raw_input("what program are you looking for?   "))
    find_a_program(search_item)
