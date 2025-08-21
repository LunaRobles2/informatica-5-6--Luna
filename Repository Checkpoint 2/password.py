# def main():
#     you = int(input("Guess my pasword (is a 4 digit pasword) and put your number here: "))
#     input('Press enter to continue.')
#     pasword=1423

#     if you == pasword:
#         print("yey!!! 1423 was my correct pasword.")
#     if you > pasword:
#         print("no no no, try again!!!")
#     if you < pasword:
#         print("no no no, try again!!!")

# main()

def check_password(p):
    guess = input ("Enter password: ")
    if p == guess:
        print("Correct password")

def main():
    password = input("Enter password: ")
    input("press enter to log in.")
    check_password(password)

main()
