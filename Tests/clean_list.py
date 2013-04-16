#! /usr/bin/env python

import sys

def remove_numbers(the_file):
    data = open(the_file, 'rU').readlines()
    print data
    new_data = []
    for i in data:
        print i
        try:
            int(i)
        except:
            new_data.append(str(i) + "\n")
    new_file = open('full_list_of_programs.txt', 'w')
    new_file.write(str(new_data))

if __name__ == "__main__":
    remove_numbers('list_of_programs.txt')
