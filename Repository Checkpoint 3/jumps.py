def main():

    number = int(input("Please type in a number: "))
    limit = number
    steps = 2
    while steps < limit:

        steps = steps + 1

        even = steps % 2
        if even == 0:
            print(steps)

main()