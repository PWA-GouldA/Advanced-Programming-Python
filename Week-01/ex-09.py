# Application: Logicals
# Filename:    ex-09.py
# Version:     1.0
# Author:      Adrian Gould

# A | B | A AND B | A OR B
# F | F |    F    |   F
# T | F |    F    |   T
# F | T |    F    |   T
# T | T |    T    |   T

result = 1 == 1 and 2 == 2
# TRUE

a = 3
b = 2
resultAnd = (a == 2) and (b == 2)
print(resultAnd)

a = 3
b = 2
resultOr = (a == 2) or (b == 2)
print(resultOr)