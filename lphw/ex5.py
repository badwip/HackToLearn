name = 'Zed A. Shaw'
age = 35 
height = 74		# inches
cm_height = height * 2.54
weight = 180		# lbs
kg_weight = weight * 0.453592
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % cm_height
print "He's %d kilograms heavy." % kg_weight
print "Actually that's not too heavy."
print "He's got %s hair and %s eyes." % (hair, eyes)
print "His teeth are usually %s depending on the coffee." % teeth

# a tricky line
print "If I add %r, %d and %d I get %d." % (
	age, height, weight, age + height + weight)