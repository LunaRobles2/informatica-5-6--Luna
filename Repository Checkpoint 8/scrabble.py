print ("⚫⚪⚫⚪⚫   SCRABBLE   ⚫⚪⚫⚪⚫")
print ("To play the game, each player is given 13 letters, which they must \n rearrange to create words. Different letters have different point \n values, since it's easier to create words with some letters than others.")
print("-" * 45)

import random
import string
alphabet = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, 
    "K": 4, 
    "J": 8, "X": 8, 
    "Q": 10, "Z": 10, 
}
user_letters = []
i = 0
while i < 13:
    i += 1
    num = random.choice(string.ascii_uppercase) 
    user_letters.append(num)
print(user_letters)