while True:
    n = input("Type greeting: ")


    if n.startswith("hello"):
        result = "$0"
    elif n.startswith("h"):
        result = "$20"
    else: 
        result = "$100"
    
        

    print(f"you get {result} .")

    if result == "$100":
        break
