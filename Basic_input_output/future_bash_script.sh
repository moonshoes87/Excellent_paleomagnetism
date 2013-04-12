#! /bin/bash

python Bootstrap.py > bootstrap_full_output.txt
echo "finished Bootstrap.py"
python Extra_output.py > extra_out_full_output.txt
echo "finished Extra_output.py"
python Rename_me.py > rename_me_full_output.txt
echo "finished Rename_me"
python Random.py > random_full_output.txt
echo "finished Random.py"
python clean_log_output.py -all
echo "ran clean_log_output.py -all" # PUT US BACK IN




# looks like rename_me_errors_list.txt isn't getting put into all_errors_list.txt
# try changing order (rename_me used to be first) # DOESN'T HELP!!
# looks like rename_me_errors_list ends up blank when it is run with the others, but not when it is run alone
# test: do all of them individually, then cross reference against doing all of them together, see if all the same errors show up 
# try checking the rename_me output log and see if you can tell why it isn't logging
# works with just running Rename_me.py, with this bash script, if I run no others
# now trying with Rename_me and Extra_output
# still doesn't log the rename_me errors..  now trying switched order
# works when rename_me.py is not first!  (ran with rename_me and extra-output.  now trying with all)


#cat bootstrap_errors_list.txt rename_me_errors_list.txt random_errors_list.txt extra_output_errors_list.txt > all_errors_list.txt  # PUT ME BACK IN

cat hello.txt rename_me_errors_list.txt extra_output_errors_list.txt > I_Like_Coffee.txt

echo "concatenated bootstrap_errors_list, rename_me_errors_list, random_errors_list, and extra_output_errors_list"


#generated_when_all_together_with_bash_script= 
#ex_out:
#<open file 'extra_output_errors_list.txt', mode 'w' at 0x436390>testing aarm_magic.py: Wrong output -- output list did not match correct_output_list.       piccadilly       test orientation_magic.py: Script returned code: 1       piccadilly

#random: -- same when done alone
#<open file 'random_errors_list.txt', mode 'w' at 0x438cd8>test gaussian.py: global name 'o1' is not defined.     piccadilly       test fisher.py: fisher.py is producing the wrong amount of output.       piccadilly


#bootstrap:
#<open file 'bootstrap_errors_list.txt', mode 'w' at 0x47ab78>test watsonsV.py: Script returned code: 1.       piccadilly

#rename_me: 
#blank (but output and clean output show magic_select as having a problem)

