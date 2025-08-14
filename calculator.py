#Operations
x = 1
y = 2
z = x + y
print(z)

#Asking for intergers (Numbers with no decimals)
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)
#or you can do...
x = input("(int)What's x? ")
y = input("(int)What's y? ")
print(int(x) + int(y))

#Asking for floats (Numbers with decimals)
x = input("(float)What's x? ")
y = input("(float)What's y? ")
z = (float(x) + float(y))
print (z)

#Asking for coma in floats (Numbers with decimals)
x = input("(float)What's x? ")
y = input("(float)What's y? ")
z = round(float(x) + float(y))
print (f"{z:,}")