def main():
    num = int(input("enter the number of table you want: "))
    table = 1
    while table < 11:
        print(f"{num} x {table} = {num * table}")
        table += 1

main()