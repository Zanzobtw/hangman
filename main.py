import random
# Step 2:
# create list of random words and get
# one word from the list to play on

game_list = ["computer", "keyboard", "monitor", "camera", "mouse", ""]          # create a list to be played on called game_list
game_word = random.choice(game_list)                                            # set game_word to a random word from the game_list
word_length = len(game_word)
print(word_length * "_ " + "\n")

# Step 2:
# get user input and turn it to a list

user_input = input()                    # gets user input
list_input = []                         # list for correct letters

# Step 3:
# look at user input and compare to game word

if user_input != game_word:
    for letter in user_input:
        if letter in game_word:
            list_input.append(letter)
            print(letter + " is in the word" + '\n')
            print("These are the correct letters guessed so far:", list_input)
        else:
            print(letter + " is not in the word" + '\n')
else:
    print("You guessed the word " + user_input + " and were correct!")