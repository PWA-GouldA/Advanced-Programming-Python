# Application: Strings II - Slicing
# Filename:    ex-14.py
# Version:     1.0
# Author:      Adrian Gould

theString = "Demo Adventure!"

print( theString[2:7] )

print( theString[-5:-3] )

print( theString[4:] )

print( theString[:-5] )

print( theString[6] )

print( theString[99:] )

letter = theString[6]
print(letter, type(letter))

letter = theString[-2]
print(letter, type(letter))

upper = theString.upper()
print(upper)

lower = theString.lower()
print(lower)

text = " Tell me more!  Go on!       "
print(text)
print( text.lstrip() )
print( text.rstrip() )
print( text.strip() )

quickie = "Quick!"
print( quickie.ljust(40, "-") )
print( quickie.rjust(40, "-") )
print( quickie.center(40, "-") )

print( text.count("o") )
print( text.index("o") )
print( text.split(" ") )
