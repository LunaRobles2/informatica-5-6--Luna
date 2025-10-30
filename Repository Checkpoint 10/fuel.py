def main():
    print(" ⏱️   ⚫ " * 10)
    print("Fuel gauges indicate, often with fractions, just how much fuel is in a tank.⛽")
    print("For instance 1/4 indicates that a tank is 25%, full, 1/2 indicates that a tank")
    print("is 50%🚩, full, and 3/4 indicates that a tank is 75%, full🚩.")
    print(" ")
    print("This program checks how much fuel is in a tank🚗, to do this you must create a fraction ")
    print("without integers forming X/Y, where in each of X and Y is a positive integer")
    print("so that the program gives it to you in percentage rounded to the nearest integer⏱️.")

    x = input("⛽Please type the fuel level as a fraction: ").split("/")
    print("-" * 45)
    xx = x[0]
    yy = x[1]
    read_input(xx, yy)
    #print(xx, "/", yy, " indicates that a tank is", , "%, full")

def read_input(xx, yy):
    while True:
        try:
            if int(xx) < int(yy):
                per = round(int(xx)/int(yy) * 100)
                if per == 1 or per < 1:
                    print("🔴E🔴")
                    print(" ")
                    break
                elif per == 99 or per > 99:
                    print("🟢F🟢")
                    print(" ")
                    break
                else:
                    print("⏩⏩⏩", xx, "/", yy, " indicates that a tank ⛽ is", per, "%, full⛽")
                    print(" ")
                    break
            else:
                print("It is not necessary for Y to be", yy)
        except ZeroDivisionError or ValueError or TypeError:
            print("It is not necessary for Y to be", yy)
        except IndexError:
            print("Sorry but you have to type a number, a dash and another number")
main()