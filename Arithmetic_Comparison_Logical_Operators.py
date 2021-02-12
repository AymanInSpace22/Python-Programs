# arithmetic operators

print(10 + 3)
print(10 * 3)
print(10 - 3)

# there are 2 different division symbols
# the first one has uses one slash which returns you a floating point value
print(10 / 3)
# the second one has two slashes. Two slashes will round it to a whole number, and return an integer\
print(10 // 3)

# you also have the modulus operator. This operator returns the remainder from the two operands
print(10 % 3)

# you also have the exponent operator. it is declared with **
print(10 ** 3)

# the augmented assignment operator. Bascially its like the += in C#. So, instead of this
x = 10
x = x + 3
# you can do this
x += 3
x *= 3
x -= 3



#Comparison Operators
x = 3 < 2
x = 3 > 2
x = 3 <= 2
x = 3 >= 2
x = 3 == 2
x = 3 != 2


x = 3 > 2
print(x)




#Logical Operators

# and operator
price = 25
print(price > 10 and price < 30)
# or
print(10 < price < 30)

# or operator
price = 20
print(price < 15 or price > 12)

# not operator. Basically inverses any value you give it
price = 10
print(not price < 15)

# and = both
# or = at least one
# not = inverse the boolean
