import sys
import random

def easy():
    number = random.randrange(1, 101)
    chance = 0
    while chance < 10:
        try:
            print("\nGOOD! YOU HAVE SELECTED EASY DIFFICULTY")
            print("LET'S START THE GAME")
            print("YOU HAVE 10 CHANCE TO ANSWER")
            guess = int(input("GUESS NUMBER 1-100: "))
            if guess == number:
                print(f"CONGRATULATIONS!! You guessed the correct number in {chance} attempts.")
                return play()
            elif guess < number:
                print(f"INCORRECT!! TOO LOWER THAN {guess} ")
            elif guess > number:
                print(f"INCORRECT!! TOO HIGHER THAN {guess} ")
            chance += 1
            if chance == 10:
                print(f"GAME OVER!! THE NUMBER IS {number}. \nLET'S TRY AGAIN!! ")
            
        except ValueError as e:
            print(e)
            

def medium():
    number = random.randrange(1, 101)
    chance = 0
    while chance < 5:
        try:
            print("\nGOOD! YOU HAVE SELECTED EASY DIFFICULTY")
            print("LET'S START THE GAME")
            print("YOU HAVE 5 CHANCE TO ANSWER")
            guess = int(input("GUESS NUMBER 1-100: "))
            if guess == number:
                print(f"CONGRATULATIONS!! You guessed the correct number in {chance} attempts.")
                return play()
            elif guess < number:
                print(f"INCORRECT!! TOO LOWER THAN {guess} ")
            elif guess > number:
                print(f"INCORRECT!! TOO HIGHER THAN {guess} ")
            chance += 1
            if chance == 10:
                print(f"GAME OVER!! THE NUMBER IS {number}. \nLET'S TRY AGAIN!! ")
            
        except ValueError as e:
            print(e)

def hard():
    number = random.randrange(1, 101)
    chance = 0
    while chance < 3:
        try:
            print("\nGOOD! YOU HAVE SELECTED EASY DIFFICULTY")
            print("LET'S START THE GAME")
            print("YOU HAVE 3 CHANCE TO ANSWER")
            guess = int(input("GUESS NUMBER 1-100: "))
            if guess == number:
                print(f"CONGRATULATIONS!! You guessed the correct number in {chance} attempts.")
                return play()
            elif guess < number:
                print(f"INCORRECT!! TOO LOWER THAN {guess} ")
            elif guess > number:
                print(f"INCORRECT!! TOO HIGHER THAN {guess} ")
            chance += 1
            if chance == 10:
                print(f"GAME OVER!! THE NUMBER IS {number}. \nLET'S TRY AGAIN!! ")
            
        except ValueError as e:
            print(e)

def play():
    while True:
        try:
            print("\nWELCOME TO NUMBER GUESSING GAME")
            print("SELECT DIFFICULTTY LEVEL:")
            print("1. EASY (10 CHANCE) ")
            print("2. MEDIUM (5 CHANCE) ")
            print("3. HARD (3 CHANCE) ")
            print("4. EXIT")
            user = int(input("ENTER CHOICE - 1/2/3/4: "))
            if user == 1:
                easy()
            elif user == 2:
                medium()
            elif user == 3:
                hard()
            elif user == 4:
                print("THANKYOU FOR PLAYING")
                sys.exit()
            else:
                print("\nPLEASE ENTER AVAILABLE NUMBER!!")
        except ValueError as e:
            print(e)
play()
            

