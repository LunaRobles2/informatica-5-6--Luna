#Sintax Error
#print("Hello world)

#Value Error
#try:
#    x = int(input("What is x? "))
#    x = print(f"x is equal to {x}")
#except ValueError:
#    print("x is not a number")

#
# def spam(dibide_by):
#     try:
#         return 42 / dibide_by
#     except ZeroDivisionError:
#         print("Invalid Argument")

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# #Guess
# def spam(dibide_by):
#     if dibide_by>0:
#         return 42 / dibide_by
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#
# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not a number")
#     else:
#         break

# x = print(f"x is equal to {x}")

def read_small_interger():
    while True:
        try:
            input_str = ("Please type in an intergerinput: ")
            number = int(input_str)
            if number < 100 and number >= 0:
                return number
            
        except ValueError:
            pass
        print("This input is invaliud")

    
number = read_small_interger()
print(number, "to the power of three is", number**3)