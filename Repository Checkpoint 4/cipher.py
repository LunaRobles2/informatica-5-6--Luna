def main():
    message = input("Write a message that will be encoded: ").lower()
    encode_message(message)

def encode_message(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0

    while i < len(text):
        char = text[i]
        
        if char in alphabet:
            cipher_index = alphabet.find(char)
            new_message += cipher [cipher_index]
        else:
            new_message += char
        i += 1
    print ('encoded message: ' + new_message)

main()                                                                                                          