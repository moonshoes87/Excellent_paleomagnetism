#! /bin/bash

# making sure all files are created afresh
rm *new.out*  # removes all output files from the last round of testing
rm *full_output.txt*  # removes long files with stdout from tests
rm *clean_output.txt* # removes shorter files with shortened stdout from tests
rm *errors_list.txt* # removes files with a list of the problem programs

python Bootstrap.py > bootstrap_full_output.txt
echo "finished Bootstrap.py"
python Extra_output.py > extra_out_full_output.txt
echo "finished Extra_output.py"
python Random.py > random_full_output.txt
echo "finished Random.py"
python Rename_me.py > rename_me_full_output.txt
echo "finished Rename_me"
python clean_log_output.py -all
echo "ran clean_log_output.py -all"

#full test (with shortened rename_me), started at 10:55 a.m., done at 11:09 a.m.  Jeez

# looks like rename_me_errors_list.txt isn't getting put into all_errors_list.txt
# when I do clean_log_output.py on the rename_me stuff, it errases the rename_me_errors_list, for some reason
# any time I run clean_log_output.py at all, it removes the rename_me errors list.  weird. 
# it was because clean_log_output.py was importing Rename_me, so it reset the error file.  Jesus H

cat bootstrap_errors_list.txt rename_me_errors_list.txt random_errors_list.txt extra_output_errors_list.txt > all_errors_list.txt  # PUT ME BACK IN

echo "concatenated bootstrap_errors_list, rename_me_errors_list, random_errors_list, and extra_output_errors_list"

