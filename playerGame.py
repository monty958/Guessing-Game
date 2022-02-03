from random import *

rand_num = randint(1, 100)
player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
user1_Attempt = 0
user2_Attempt = 0
whoStarts = randint(1, 2)
guess = 0

if whoStarts == 1:
    print(f"{player1} starts the game!")
else:
    print(f"{player2} starts the game!")

while True:
    if whoStarts == 1:
        guess = int(input(f"{player1} enter your number b/w 1 to 100: "))
        user1_Attempt += 1
        whoStarts += 1
        if rand_num > guess:
            print("Guess something bigger next time!")
        elif rand_num < guess:
            print("Guess something smaller next time!")
        else:
            print(f"{player1} won and it took him {user1_Attempt} !")
            break

    else:
        guess = int(input(f"{player2} enter your number b/w 1 to 100: "))
        user2_Attempt += 1
        whoStarts -= 1
        if rand_num > guess:
            print("Guess something bigger next time!")
        elif rand_num < guess:
            print("Guess something smaller next time!")
        else:
            print(f"{player2} won and it took him {user2_Attempt} !")
            break

    if whoStarts == 1:
        print(f"{player1} turn!")
    else:
        print(f"{player2} turn!")
