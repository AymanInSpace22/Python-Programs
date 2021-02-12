# uppercase and lowercase functions
course = "python for beginners"
print(course.upper())
print(course.lower())

# the find function returns the position of the character you pass in
# remember indexing is zero based
print(course.find('o'))

# the replace method finds and replaces words in your string. SO COOL!
print(course.replace("beginners", "bitches" ))

# the "in" keyword returns a boolean to display whether or not the work you are looking for is in the string
print('python' in course)
print("bitch" in course)
