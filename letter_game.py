import pandas as pd
import random
import os
import sys

def clean():
    if os.name == "nt": #windows
        os.system("cls")
    else: #mac,linux
        os.system("clear")

def drow(bad_letters, good_letters, secret_word):
    clean()
    
    print("Strike {}/5".format(len(bad_letters)))
    print("")
    
    for letter in bad_letters:
        print(letter, end="")
    print("\n\n")
    
    for letter in secret_word:
        if letter in good_letters:
            print(letter,end="")
        else:
            print("*", end="")
    print("")

def get_guess(bad_letters, good_letters):
    while True:
        guess = input("Your letter: ").lower()
        
        if len(guess) !=1:
            print(" It is not single letter!")
        elif guess in bad_letters or guess in good_letters:
            print(" You have guess that letter.")
        elif not guess.isalpha():
            print(" It is not letter!")
        else:
            return guess

def game(done):
    clean()
    secret_word = random.choice(words)
    bad_letters = []
    good_letters = []
    
    while True:
        drow(bad_letters, good_letters, secret_word)
        guess = get_guess(bad_letters, good_letters)
        
        if guess in secret_word:
            good_letters.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_letters:
                    found = False
            if found:
                print("You win! The word was {}".format(secret_word))
                done =True
        else:
            bad_letters.append(guess)
            if len(bad_letters) == 5:
                drow(bad_letters, good_letters, secret_word)
                print("You lost! The word was {}".format(secret_word))
                done = True
        
        if done:
            new_game = input("Do you want to play? (yes/no) - ").lower()
            if new_game == "yes":
                return game(done = False)
            else:
                print("Bye")
                sys.exit()

animals_data = pd.read_csv("animals.csv")
words = []
for i in animals_data.name:
    words.extend([i])

print("Welcom!")
done = False

while True:
    clean()
    game(done)
