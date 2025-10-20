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
    user_letters.append(list(alphabet.keys())[random.randint(0,25)])
    i += 1
print(user_letters)

word = input("Enter a word with these letters: ")
o = 0
while o < len(word):
    if word.upper()[o] in user_letters:
        print(word[o])
        o += 1
    else:
        print("Wrong")
        o += 1

with open("scrabble-words.txt", "r") as file:
    lines = file.readline()
dicwords = []
for line in lines:
    dicwords.append(line.replace("\n",""))
if word in dicwords:
    print("it's okay")
else: 
    print("Not okay")