# Application: Strings III - Formatting
# Filename:    ex-15.py
# Version:     1.0
# Author:      Adrian Gould

value = 123.56
mean = value / 6

print("Total: {}.".format(value) )

print("Total: {}  Mean: {}.".format(value, mean) )

print("Total: {:04.2f}  Mean: {: 6.2f}.".format(value, mean) )
print("Total: {:04.2f}  Mean: {:06.2f}.".format(value, mean) )
# https://pyformat.info