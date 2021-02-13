# Lists

# this is how you print out all the elements in your list
names = ["Gon", "Kilua", "Hisoka", "Kurapika", "Leorio"]
print(names)


# this is how you print an individual element or subscript/index
# similar to C# with the square brackets
names = ["Gon", "Kilua", "Hisoka", "Kurapika", "Leorio"]
print(names[0])
print(names[4])


# you can update an element from your list by doing this
names = ["Gon", "Kilua", "Hisoka", "Kurapika", "Leorio"]
names[0] = 'Netero'
print(names)
print(names[0])

# you can also use a negative subscript/index. It will just give you the last position


# if you want to print a specific set of subscripts. You can do that by doing this
names = ["Gon", "Kilua", "Hisoka", "Kurapika", "Leorio"]
print(names[0:3])
# this will print out the subscripts from position 0 to position 2
