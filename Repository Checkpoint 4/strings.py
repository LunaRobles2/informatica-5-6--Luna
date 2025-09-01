#String Length
input_String = input ("please type a message: ")
print (input_String)

print ("-" * len(input_String))

# #String Index
# #print (input_String[0])
# print (input_String[1])
# print (input_String[2])
# print (input_String[-1])

#Example
i=0
while i < len(input_String):
    print (input_String[i])
    i += 1

while i < len(input_String):
    print (input_String[i])
    i += -1

print("h" in input_String)
print("j" in input_String)
print("ello" in input_String)
print(input_String.find("h"))