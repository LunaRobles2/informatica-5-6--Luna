def main():
    message = input("Write a message that will be encoded: ").lower()
    encode_message(message)

def encode_message(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = " "
    i=0

    print ("-" * len(message))


    while i < len(text):
        char = text[i]
        

main()                                                                                                         