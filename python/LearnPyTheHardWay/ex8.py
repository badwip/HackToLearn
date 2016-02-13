formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# This is where I put a variable inside the same variable
print formatter % (formatter, formatter, formatter, formatter)
# This is another way to call multiple variable
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So, I said goodnight."
)
