birth_year = input("Enter your birth year: ")

 # putting the int before the birth_year variable is how you explicitly convert the variable from type string to int
 # similar to int.Parse, or Convert.ToInt32 in C#
age = 2020 - int(birth_year)
print(age)

# these are the built in functions for converting the type of our variables
int()
float()
bool()
str()

# this is a simple arithmetic program
# remember to explicitly switch the first and second variables to a numeric value becuase if you dont. Python will read it as string and combine the strings
first = input("Enter first number: ")
second = input ("Enter second number: ")
sum = float(first) + float(second)
# you can only concatanate literal strings with string variables. You cant concatanate literal strings and floats, or ints
# so, you must convert your variable back into a string(str) like you see below
print("Sum is: " + str(sum))

# type conversion

# here is another way you can do the above program
# you can convert the user input right when you receive it instead of doing it in the arithmetic
first = float(input("Enter a number: "))
second = float(input("Enter another number: "))
result = first + second
print("Sum is: " + str(result))
