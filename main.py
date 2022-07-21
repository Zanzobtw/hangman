import random

# create a list to be played on called game_list
game_list = ["hello"]

# set game_word to a random word from the game_list
game_word = random.choice(game_list)

# set word_length to the length of the word
word_length = len(game_word)

# print out _ the same amount of times as the word length
print(word_length * "_ " + "\n")                                                

# gets user input
user_input = input("Take a guess \n \n")

# list for correct letters
list_input = []

while user_input != "":
    if user_input != game_word:
        for letter in user_input:
            if letter in game_word:
                list_input.append(letter)
                print(letter + " is in the word" + '\n')
                print("These are the correct letters guessed so far:", list_input, "\n")
                # user_input = input("Guess again! \n")
            elif letter not in game_word:
                print(letter + " is not in the word" + '\n')
                # user_input = input("Guess again! \n")
    else:
        print("You guessed the word " + user_input + " and were correct!")
        user_input = input()