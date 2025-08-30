def main():
    print ('This is a month To Do list to organize your time')
    while True:
        next = int(input("Please type -1- to coninue or -2- to end the program: "))
        
        if next == 1:
            name = input("Please type your name: ")
            a = "Pray"
            b = "Read scriptures"
            c = "Be ready to sleep at 10pm"
            d = "go to school"
            line = "-" * 45

            date = input("Please type the date: ")
            list = input("something importat for today is:")
            ok = int(input("Did you want to add more? if yes put -3- if not clic -4-: "))
            if ok == 3:
                other = input("add here: ")
            else:
                other = " "
                print("okay")

            print (line)
            print ('Today is:', date)
            print (name,'Today you need to remember to...')
            print (a)
            print (b)
            print (c)                
            print (d)
            print (list)
            print (other)
            print (line)

        else:
            break

main()