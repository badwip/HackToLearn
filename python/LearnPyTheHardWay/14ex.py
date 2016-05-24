from sys import argv

script, username = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (username, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "where do you live %s?" % username
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


# Study Drills 
# 
# 1. Find out what Zork and Adventure were. Try to find a copy and play it.
# 2. Change the `prompt` variable to something else entirely.
# 3. Add another argument and use it in your script, the same way you did 
# in the previous exercise with `first, second = ARGV`.
# 4. Make sure you understand how I combined a """ style multiline string with
# the `%` format activator as the last print.
