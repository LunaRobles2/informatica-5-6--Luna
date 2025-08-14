(#("Ask the user for their name"
name = input("What's your name? ")
print("hello,")
print(name)

# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)

print(*objects, sep=' ', end='\n', file=None, flush=False)

# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)

# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
#Notice the f in print(f"hello, {name}"). This f is a special indicator for Python 
# to treat this string in a special way, different from the previous approaches we 
# have illustrated in this lesson.

#Strip Method
# Ask the user for their name
name = input("What's your name? ")
# Remove whitespace from the str
name = name.strip()
# Print the output
print(f"hello, {name}")

#"Title Method"
#Using the title method, it would title case the user’s name:
# Ask the user for their name
name = input("What's your name? ")
# Remove whitespace from the str
name = name.strip()
# Capitalize the first letter of each word
name = name.title()
# Print the output
print(f"hello, {name}")

#Notice that you can modify your code to be more efficient:
# Ask the user for their name
name = input("What's your name? ")
# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()
# Print the output
print(f"hello, {name}")
​
We could even go further!
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()
# Print the output
print(f"hello, {name}")))