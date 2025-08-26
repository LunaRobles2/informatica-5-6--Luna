def main():
    n1 = int(input("Write a integer number: "))
    n3 = n1 % 3
    n5 = n1 % 5

    if n3 == 0 and n5 == 0:
        result = "fizzbuzz"
    elif n3 == 0:
        result = "fizz"
    elif n5 == 0:
        result = "buzz"
    else: 
        result = n1
        

    print(f"{result} is your result.")

main()