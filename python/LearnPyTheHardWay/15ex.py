from sys import argv

script, filename = argv

# opening file based on the argument and it assigned to a variable
txt = open(filename)

print "Here's your file %r:" % filename	# named the file
print txt.read()			# print variable's content

print "Type the filename again"
file_again = raw_input("> ")		# parameter input by user

# opening file assigned to variable
txt_again = open(file_again)

print txt_again.read()			# print variable's content

txt.close()
txt_again.close()
