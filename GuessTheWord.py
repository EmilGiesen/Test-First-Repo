import random

game_name = "Guess The Word"
word_bank = []
missplaced_letters = []
not_in_word = []
trys = 1

with open ("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

word = random.choice(word_bank)
print("Whalecum to the game" + game_name)
print("You have 5 trys to guess a 5 Letter word")

while trys <= 5:
    print("These Letters are in the Word that you know alreasy: " + str(missplaced_letters) + "\nThese Letter are not in the Word: " + str(not_in_word))
    guess = input("Input Your " + str(trys) + " guess \n")
    guess = guess.strip() 
    guess = guess.lower()

    if not guess.isalpha() or len(guess) != 5:
        print("Only Input 5 Letters asshole")
        continue
    elif guess == word:
        print("WOW you guess the Word correctly it was " + word + " you guessed it in " + str(trys) + " tries")
        break
    elif trys == 5 and guess != word:
        print("Whomp looks like you suck at this the word would have been " + word)
        break
    else:
        trys += 1
    for x in range(0,5):
        letter_word_checks = 0
        letter_guess_check = 0
        if guess[x] == word[x]:
            print("The " + str(x + 1) + " letter in your Guess is Correct")
            missplaced_letters.append(guess[x])
            missplaced_letters = list(dict.fromkeys(missplaced_letters))
        elif guess[x] in word:
            print("The " + str(x + 1) + " letter in your Guess is in the Word")
            missplaced_letters.append(guess[x])
            missplaced_letters = list(dict.fromkeys(missplaced_letters))
        else:
            not_in_word.append(guess[x])
            not_in_word = list(dict.fromkeys(not_in_word))


                


