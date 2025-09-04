def main():
    num = int(input("enter the number of table you want: "))
    table = 1
    
    while table < (num + 1):
        other = 1 

        while other < (num + 1):
            print(f"{table} x {other} = {table * other}")
            other += 1

        table += 1


main()