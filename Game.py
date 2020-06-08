# This is a program that plays hangman on the command line
# 1: Set A word
# 2: Set a Theme
# 3. Display the # of body parts
# 4. Display the word spaces
# 5. Display used letter
# 6. Display Correct Letter
# 7. End Game

import random
from time import sleep

people = ['Naval Ravikant', 'Paul Graham', 'Kevin Hart', 'Albert Einstein', 'Kanye West', 'Elon Muskrat', 'Neil deGrasse Tyson']
animals = ['Cat', 'Dog', 'Flamingo', 'Dodo Bird', 'Gazelle']
place = ['France', 'Wakanda', 'Burkina Faso', 'Canada']
tv_shows_and_movies = ['The Blacklist', 'Forrest Gump', 'The Social Network', 'The Office', 'How I Met Your Mother', 'Kung Fu Panda']


themes = [people, animals, place, tv_shows_and_movies]
theme_choice = random.choice(themes)
word = random.choice(theme_choice)
word = word.lower()

if len(theme_choice) == 7:
    print("The Theme is People")
elif len(theme_choice) == 6:
    print('The Theme is Tv Shows and Movies')
elif len(theme_choice) == 5:
    print('The Theme is Animal')
else:
    print('The theme is Places')
    
print("Your Hangman has 11 parts: 1 head , 1 body , 2 arms, 2 feet, 1 fedora, 2 eyes, 1 nose and 1 mouth!")

numspaces = ""
if " " not in word:
    numspaces = len(word) * "_ "
    print(numspaces)
else:
    word = word.split()
    count = 0
    while count <= (len(word) - 1):
        numspaces += (len(word[count]) * "_ ") + "  "
        count += 1
    print(numspaces)


def guesses(word_choice, spaces):
    win = False
    lose = False

    if type(word_choice) == list:
        word_choice = " ".join(str(word) for word in word_choice)
    list_word_choice = word_choice.split() #helpful for determining if it's a single word answer or multiple
    incorrect_guesses = []

    while win == False and lose == False:
        hangman_parts = 11 - len(incorrect_guesses)
        if "_" not in spaces: #determines if the game is over
            win = True
            print()
            print("You Won!")
        elif hangman_parts <= 0:
            lose = True
            print()
            print('You Lost.')

        else:
            print()
            print("Make the wrong choice, just type '!back' to go to the guess selection")
            word_or_letter = input('Would you like to guess: W for Word, L for Letter, or D for Dub/Solution: ')
            if word_or_letter.upper() == 'L':
                letter = (input("What letter would you like to guess: ")).lower()
                if letter == '!back':
                    pass

                elif letter in word_choice:
                    letter_index = [i*2 for i, n in enumerate(word_choice) if n == letter] #as letter are spaced out in spaces, the index will be *2 the amount
                    spaces = list(spaces)
                    count = 0

                    for index in letter_index:
                        spaces[letter_index[count]] = letter
                        count += 1
                            
                else:
                    incorrect_guesses.append(letter)
                    incorrect_guess(hangman_parts, incorrect_guesses, spaces)

                spaces = "".join(spaces)
                print(spaces)
                
            elif word_or_letter.upper() == 'W':
                word_guess = input('What Word will you like to guess: ')
                word_index = [word_choice.find(word_guess)]
                
                if word_guess in list_word_choice:
                    word_guess = list(word_guess)
                    word_guess = " ".join(word_guess)  # eg. a p p l e
                    word_index = [i*2 for i in word_index]
                    replace_index = int(word_index[0])
                    spaces = list(spaces)
                    spaces[replace_index] = word_guess
                    del spaces[replace_index+1: (replace_index + len(word_guess))]
                    
                else:
                    incorrect_guesses.append(word_guess)
                    incorrect_guess(hangman_parts, incorrect_guesses, spaces)

                spaces = "".join(spaces)
                sleep(1)
                print(spaces)
                
            elif word_or_letter.upper() == 'D':
                solution_guess = input("What phrase do you think will get you the win? ")
                solution_guess = solution_guess.lower()
                
                if solution_guess == word_choice:
                    solution_guess = list(solution_guess)
                    solution_guess = " ".join(solution_guess)
                    solution_guess = solution_guess.upper()
                    print()
                    print(solution_guess)
                    print()
                    print("You Won!")
                    break
                    
                else:
                    incorrect_guesses.append(solution_guess)
                    incorrect_guess(hangman_parts, incorrect_guesses, spaces)
                    spaces = "".join(spaces)
                    sleep(1)
                    print(spaces)

            else:
                print()
                print("Sorry, that is not an option. You must type either 'W', 'L' or 'D'.")
                print()


def incorrect_guess(hangman_parts, incorrect_guesses, spaces):
    hangman_parts -= 1
    print("Your hangman has...")
    sleep(1)
    if hangman_parts == 1:
        print("%d part left!" % hangman_parts)
    else:
        print("%d parts left!" % hangman_parts)
    sleep(1)
    print("Sorry, that was incorrect")
    sleep(1)
    print("These are your incorrect guesses: %s" % incorrect_guesses)
    print()


guesses(word, list(numspaces))
