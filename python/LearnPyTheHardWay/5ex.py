name = "Muhammad Badwip"
age = 30
height = 170.0	# centimeters
weight = 83		# kilograms
eyes = "brown"
teeth = "white"
hair = "black"

print "Let's talk about %s." % name
print "He's %d inches tall." % (height / 2.54)
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	age,
	height,
	weight,
	age + height + weight)
