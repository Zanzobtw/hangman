# Step 1:
# get user input and turn it to a list

user_input = input()                    # gets user input
list_input = []                         # list called list_input

for letter in user_input:               # for each letter in the users input
    list_input.append(letter)           # add the letter to the list called list_input
print(list_input)                       # print list_input

for char in list_input:                 # for each character in list_input
    if char == " ":                     # if the character is equal to a blank space
        list_input.remove(char)         # remove the character from list_input
print(list_input)                       # print list_input

# Step 2:
# create list of random words and get
# one word from the list to play on
