i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	

print "The numbers: "

for num in numbers:
	print num
	
# Study Drills
# 1. Convert this while-loop to a function that you can call,
#	 and replace 6 in the test (i < 6) with a variable.

print "\nConverting while-loop to a function, drill_1"

def drill_1(n):
	i = 0
	numbers1 = []
	
	while i < n:
	# while-loop will end at n
		print "item: %d" % i
		numbers1.append(i)
		i = i + 1
		
	print numbers1

# 2. Use this function to rewrite the script to try different numbers.

print "\nCall for n = 3"
drill_1(3)

print "\nCall for n = 9"
drill_1(9)

# 3. Add another variable to the function arguments that you can pass in that lets you 
#	 change the + 1 on line 8 so you can change how much it increments by.

def drill_3(n, s):
	i = 0
	numbers3 = []
	
	while i < n:
		print "item: %d" % i
		numbers3.append(i)
		i = i + s
		
	print numbers3

# 4. Rewrite the script again to use this function to see what effect that has.

print "\nCall for upper number = 15 and using step = 3"
drill_3(15, 3)
	
# 5. Write it to use for-loops and range. Do you need the incrementor 
#	 in the middle anymore? What happens if you do not get rid of it?

def drill_5(n, s):
	numbers5 = range(2, n, s)
	
	for i in numbers5:
		print "item: %d" % i
#		i = i + s
#		it doesn't need the incrementor anymore.
#		if it's not got rid, it doesn't matter either.
	
	print numbers5

print "\nCall for range from 0 to 20, 3 step at a time."
drill_5(20, 3)