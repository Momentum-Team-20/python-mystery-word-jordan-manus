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


# selects random word from the list by getting a random number within the length of fileList and using that as an index
def random_word_selector(fileList):
    num = random.randint(0, len(fileList)) 
    randomWord = fileList[num] #removed -1 from equation
    print(randomWord)
    return randomWord


# compares user input to word that computer chose
def compare_input_to_chosen_word(randomWord, userInput, word, char):
    if userInput in randomWord:
        replace_underscore_in_sequence(randomWord, userInput, word)
        char += (userInput + " ")
    else:
        print(f"Sorry, there are no {userInput}'s")
        char += (userInput + " ")
    return word, char


'''
# this is spicy section! choice changes as user guesses more
def narrow_down_word_choice(userInput):
    pass
'''


# validates that user put in only chars that have not been guessed
def input_validation(userInput, char):
    # makes sure the user's input is a letter only
    while userInput not in string.ascii_letters:
        userInput = input("Invalid entry! Guess a letter between a and z: ")

    # makes sure the user's input is not in the already guessed list
    while userInput in char:
        userInput = input("Already guessed this letter! Guess a letter between a and z: ")

    return userInput.lower()


# replaces underscore of each correct char in the correct location
def replace_underscore_in_sequence(randomWord, guess, word):
    count = 0
    for index in range(len(randomWord)):
        if randomWord[index] == guess:
            word[index] = guess
            count += 1
    print(f'Yes, there is {count} of {guess}')


# houses program display
def display(word, count, char):
    print(f'You have {count} guesses remaining!')
    print(f'Used letters: {char}')
    print(f'Word: {" ".join(word)}')


# allows user to play the game. includes calls to most of the functions
def play_game():
    char = ''
    count = 15
    fileList = open_and_read_file(file)
    randomWord = random_word_selector(fileList)
    word = ['_' for x in randomWord]

    while "".join(word) != randomWord and count > 0:
        display(word, count, char)        
        guess = input("guess a letter between a and z: ")
        guess = input_validation(guess, char)
        word, char = compare_input_to_chosen_word(randomWord, guess, word, char)
        count -= 1
    
    return word, randomWord


if __name__ == "__main__":
    word, randomWord = play_game()

    if "".join(word) == randomWord:
        print(word)
        print('Congrats!! You win!')
    else:
        print(f'You lose! The word was {randomWord}')

    # asks user if they want to play again and puts it in a loop until they quit 
    playAgain = input("Press 'y' to play again: ")

    while playAgain == 'y':
        
        word, randomWord = play_game()

        if "".join(word) == randomWord:
            print(word)
            print('Congrats!! You win!')
            playAgain = input("Press 'y' to play again: ")
        else:
            print(f'You lose! The word was {randomWord}')
            playAgain = input("Press 'y' to play again: ")