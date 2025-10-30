def main():
    print("🟥 🟨 🟦 " * 7)
    print("Lets play with factorial numbers!!!")
    num = int(input("Type a positive integer: "))
    print(f"{num}! = {formula(num)}")

def formula(n):
    if n < 0 or n == 0:
        raise ValueError(f"The input was negative or zero: {n}")
    else:
        new_n = 1
        print(list(range(2, n + 1)))
        for i in range(2, n + 1):
            new_n = new_n * 1
        return new_n
    
main()