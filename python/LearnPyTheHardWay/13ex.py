# This is how you add features to your script from the Python modules set
from sys import argv

script = argv		# unpack `argv` into var

print "The script is called:", script 
# print "Your first variable is:", first
second = raw_input("Your second variable is: ") 
third = raw_input("Your third variable is: ") 


# Study Drills
# 1. Try giving fewer than three arguments to your script. See that error you
# get? See if you can explain it.
# 2. Write a script that has fewe arguments and one that has more.
# Make sure you give the unpacked variables good names.
# 3. Combine `raw_input` with `argv` to make a script that gets more input from
# a user.
# 4. Remember that modules give you features. Modules. Modules.
# Remember this because we'll need it later. 
