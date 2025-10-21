def main():
    print("⚫⚪⚫⚪⚫   SCRABBLE   ⚫⚪⚫⚪⚫")
    print("To play the game, each player is given 13 letters, which they must")
    print("rearrange to create words. Different letters have different point")
    print("values, since it's easier to create words with some letters than others.")
    print("-" * 45)

    import random
    alphabet = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    # Picks 13 random letters from the alphabet
    user_letters = []
    i = 0
    while i < 13:
        user_letters.append(list(alphabet.keys())[random.randint(0,25)])
        i += 1
    print(user_letters)

    #Ask the usser for a word with the given letters
    word = input("Enter a word with these letters: ").upper()

    # Checks if the word exist and counts
    score = 0
    while True:
        while True:        
            # Check if the word is in the dictionary                                                
            with open("scrabble-words.txt" ,"r") as file:           
                lines = file.readlines()                            
            dictwords = []
            for line in lines:
                dictwords.append(line.replace("\n",""))
            
            # Told you if the word is in the dictionary
            if word.lower() in dictwords:                          
                print("Valid")
                break

            # Told you if the word is not in the dictionary
            else: 
                word = input("Not valid, try again: ").upper()
                if word == "":
                    break

         # Checks if the input is ENTER
        if word != "": 

            # Removes the letters the user entered
            for letter in word:                                     
                user_letters.pop(user_letters.index(letter))        
            
            # Adds the value of every letter
            for value in word:                                      
                score += alphabet[value]
            
            print(f"Your total score is: {score}")
            print(f"Remaining letters: \n{user_letters}")
            word = input("Enter a word with the remaining letters, press ENTER to stop: ").upper()
            if word == "":
                break
        else: break
    print(f"Thank you for playing! Your final score is {score}")

main()