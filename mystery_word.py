import random
import string


# file = "test-word.txt"
file = "words.txt"
fileList = []


# opens test files and returns a list of words
def open_and_read_file(file):
    file1 = open(file)
    fileList = file1.readlines()
    fileList = [line.strip() for line in fileList]
    return fileList


# selects random word from the list
def random_word_selector(fileList):
    num = random.randint(0, len(fileList)) 
    randomWord = fileList[num-1]
    print(randomWord)
    return randomWord


# compares user input to word that computer chose
def compare_input_to_chosen_word(randomWord, userInput, word, char):
    if userInput in randomWord:
        print('you guessed correctly')
        replace_underscore_in_sequence(randomWord, userInput, word)
        char += (userInput + " ")
    else:
        print('character not in word. Try again')
        char += (userInput + " ")
    return word, char


'''
# this is spicy section! choice changes as user guesses more
def narrow_down_word_choice(userInput):
    pass
'''


# validates that user put in only chars that have not been guessed
def input_validation(userInput, char):
    while userInput not in string.ascii_letters:
        userInput = input("Invalid entry! Guess a letter between a and z: ")

    while userInput in char:
        userInput = input("Already guessed this letter! Guess a letter between a and z: ")

    return userInput.lower()


# replaces underscore of each correct char in the correct location
def replace_underscore_in_sequence(randomWord, guess, word):
    for index in range(len(randomWord)):
        if randomWord[index] == guess:
            word[index] = guess


# houses program display
def display(word):
    print(" ".join(word))
    

def play_game():
    char = ''
    count = 15
    fileList = open_and_read_file(file)
    randomWord = random_word_selector(fileList)
    word = ['_' for x in randomWord]

    while "".join(word) != randomWord and count > 0:
        print(f'You have {count} guesses remaining!')

        guess = input("guess a letter between a and z: ")
        guess = input_validation(guess, char)
        word, char = compare_input_to_chosen_word(randomWord, guess, word, char)
        display(word)
        count -= 1

    print('congrats!!! you win')


if __name__ == "__main__":
    play_game()
