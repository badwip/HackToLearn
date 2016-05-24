# Here to Remember
# close -- Closes the file. Like `File->Save` in your editor
# read -- Reads the contents of the file. You can assign the result to a varioable.
# readline -- Read just one line of a text file. 
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Write "stuff" to the file. 

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Control-C (^C)."
print "If you do want that, hit Return."

raw_input("?")

print "Opening the file..." 
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now, I'm going to ask you for three lines." 

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write this to the file."

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print "And finally, we close it."
target.close()


# Study Drill
#
# 1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
# 2. Write a script similar to the last exercise that uses `read` and `argv` to read the file you just created.
# 3. There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
# 4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
# 5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open function and see if that's true.
