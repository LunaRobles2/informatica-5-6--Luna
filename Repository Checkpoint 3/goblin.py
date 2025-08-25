import random
print ("Wlcome to the Goblin Game")
print ("The best game ever")
player_name = input("Write your name: ")
print (player_name, "can you find the goblin?")
print ("|_||_||_||_||_|")
goblin_position = random.randint (1, 5)
Keep_trying = True
while Keep_trying:
    guessed_position = int(input("Can you guess where the goblin is?"))

    if goblin_position == guessed_position:
        print ("🟢Well done!! you find the goblin🟢")
        Keep_trying = False
    else: print ("🔴NO, The goblin still hide somewhere else🔴")
