def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)

def read_input(prompt, check): 
    while True:
        try:
            check = int(input(prompt))
            if check < 10 and check > 5:
                return check
        except ValueError:
            pass

main()