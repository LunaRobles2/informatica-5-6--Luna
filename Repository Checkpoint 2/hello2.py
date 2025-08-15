def hello():
    print("hello")

name = input("whats your name? ").strip().title()
hello()
print(f"hello, {name}")