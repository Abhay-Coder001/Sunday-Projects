import random
import time
# Initial steps to invite in the game.
print("Welcome to Hangman game \n")
name = input("Enter your name : ")
print("Hello "+name+"! Best of luck!")
time.sleep(2) #time.sleep(2) basically 2 indicates here the delay of next line will appear in 2 seconds.
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3) #same goes for here but time delay will be 3 seconds.
print("Words for guess :-\nJanuary,","border,","image,","film,","promise,","kids,","lungs,","doll,","rhyme,","damage,","plants.")
time.sleep(2)
#Now we create a main function
def main(): 
    #All these used in below code afterwards..
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["January","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"] #Here we create a list of all the choices we give
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_'*length #This draws a line for us according to the length of word.
    already_guessed = [] #This would contain the string indices of the currently guessed word.
    play_game = ""

# Now we create a loop to re-execute the game when the first round ends.
def play_loop(): #This function takes argument to either continue the game after it is played once or end it according to what user suggest.
    global play_game
    while play_game not in ['Y','y','n','N']:
        play_game = input("Do you want to play again?\n Y = yes   N = no""\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing ! We expect you back again.")

# Initializing all the conditions required for the game 
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " \nEnter your guess: ")
    guess = guess.strip() #Removes the letter from the given word.
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()