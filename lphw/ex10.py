tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \ a \ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat 
	
# Escape Sequences

## Escape 	What it does.
## \\ 			Backslash ()
## \' 			Single-quote (')
## \" 			Double-quote (")
## \a 			ASCII bell (BEL)
## \b 			ASCII backspace (BS)
## \f 			ASCII formfeed (FF)
## \n 			ASCII linefeed (LF)
## \N{name} 	Character named name in the Unicode database (Unicode only)
## \r ASCII 	Carriage Return (CR)
## \t ASCII 	Horizontal Tab (TAB)
## \uxxxx 		Character with 16-bit hex value xxxx (Unicode only)
## \Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
## \v 			ASCII vertical tab (VT)
## \ooo 		Character with octal value ooo
## \xhh 		Character with hex value hh


# Study Drill

## Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?

## Combine escape sequences and format strings to create a more complex format.
## 

## Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
