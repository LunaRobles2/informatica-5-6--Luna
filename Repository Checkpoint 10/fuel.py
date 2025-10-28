def main():
    print("Fuel gauges indicate, often with fractions, just how much fuel is in a tank.")
    print("For instance 1/4 indicates that a tank is 25%, full, 1/2 indicates that a tank")
    print("is 50%, full, and 3/4 indicates that a tank is 75%, full.")
    print(" ")
    print("This program checks how much fuel is in a tank, to do this you must create a fraction ")
    print("without integers forming X/Y, where in each of X and Y is a positive integer")
    print("so that the program gives it to you in percentage rounded to the nearest integer.")

    x = read_input("Please type in a number for your X: ")
    y = read_input("Please type in a number for your Y: ")
    per = (x/y) * 100
    print(x, "/", y, " indicates that a tank is", per, "%, full")

def read_input(xx, yy):
    while True:
        try: 
            n = int(input(xx))
            m = int(input(yy))
            if xx < yy: 
                return xx
            else: 
                print("It is not necessary for Y to be", yy)
        except ZeroDivisionError:
            print("It is not necessary for Y to be", yy)
        except ValueError:
            print("It is not necessary for Y to be", yy)
        