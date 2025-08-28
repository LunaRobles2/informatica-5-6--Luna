def main():

    name = input("Please type your name: ")
    amount = 0
    while amount < 50:
        coin = int(input("Please incert a coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount = amount + coin
            print (amount)
        else:
            print ("we just accept coins of $25 $10 or $5: ")

    change = amount - 50
    print ('Here is a Coke for', name)
    print ('Here your change', change)

main()