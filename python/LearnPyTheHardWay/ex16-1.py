from sys import argv

script, filename = argv

target = open(filename)
target.read()

# print "Please input this line below." 

# line1 = raw_input("Line 1: ")
# line2 = raw_input("Line 2: ")
# line3 = raw_input("Line 3: ")

# print "I'm going to write this to the file."

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

# print "And finally, we close it."
target.close()