import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
# randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
# Empty list called display
display = []
discarded_letters = []
# _ for spaces of the word
for letter in chosen_word:
    display.append("_")

print(logo)
print(f"\n")
print(f"The word is a {word_length} letter word")
print(f"\n{' '.join(display)}")
# let user guess again until all the letters are guessed
while not end_of_game: 
# User input for guessing a letter       
    guess = input("\nGuess a letter: ").lower()    
    if guess in display or guess in discarded_letters:
        print("Already chosen")

# loop through each position in the chosen word and fill the blank
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# check if word has already been used and reduce life if guess is incorrect    
    if guess not in discarded_letters:   
        if guess not in chosen_word:
            print("Nahh!!")
            lives -= 1            
            discarded_letters.append(guess)

# End game when lives are finished
    if lives == 0:
        end_of_game = True
        print(f"You Loose! Game Over. The word was {chosen_word}")

# print the correct letters in the correct
    print(f"{' '.join(display)}")    
# End game if all blanks are filled    
    if "_" not in display:
        end_of_game = True
        print("You Win")
        
# Print Image of Hangman based on lives        
    print(stages[lives])
