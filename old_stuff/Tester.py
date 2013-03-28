#! /usr/bin/env python

example_list = [3.341, 2.222, 1.0101, 2.345, 4.893, 5.6, 5.9, 5.02]
dictionary = {}
for i in example_list:
    dictionary[i] = None

print dictionary

def create_bootstrap_reference(in_list):
    for l in in_list:
        string = str(l)
        length = len(string)
        print string, length
        if length > 3:
            last_digits = string[-2:]
            last_digits = int(last_digits)
            if last_digits >= 10:
                print str(last_digits) + "  are greater than 10"
                last_digits -= 10
                print last_digits
                last_digits = str(last_digits)
                lower_limit = string[:-2]
                lower_limit += last_digits
                print "lower limit = " + lower_limit
            else:
                lower_limit = string
            last_digits = string[-2:]
            last_digits = int(last_digits)
#            if last_digits <= 10:  # for the lower_bound
 #               last_digits = string[-3:]
  #              last_digits = int(last_digits) - 10
   #             last_digits = str(last_digits)
    #            lower_limit = string[:-3]
     #           lower_limit += last_digits
      #          print "lower limit is: " + lower_limit
            last_digits = string[-2:]
            last_digits = int(last_digits)
            if last_digits <= 90:  # for upper bound
                last_digits += 10
                last_digits = str(last_digits)
                upper_limit = string[:-2]
                upper_limit += last_digits
                print "upper limit = " + upper_limit
            else:
                upper_limit = string
                print "upper limit: " + upper_limit
            dictionary[l] = (lower_limit, upper_limit)

print dictionary
            
       # commenty part doesn't work         




ignore_me = """                upper_limit_stripped = string[:-1]
                upper_limit_last = str(int(string[-1]) - 5)
                final_upper_limit = upper_limit_stripped + upper_limit_last
                print "string " + string
                print "upper limit" + final_upper_limit
            else:
                print last_digit + " is less than five"
#            lower_bound = string[:-1]                                                                                                
 #           upper_bound = int(string[:-1]) + 5                                                                                      """ 

create_bootstrap_reference(example_list)
print dictionary
