from random_word import RandomWords
import ASCIIList as hangmen

secretWord = str(RandomWords().get_random_word()).lower() #to stringify even when it returns None

game = "-" * len(secretWord)
game = game[:0] + secretWord[0] + game[0 + 1:]
game = game[:3] + secretWord[3] + game[3 + 1:] #hint at 1st and 3rd words

print(game, end="\n\n")
tries = 0

while "-" in game:
    guess = input("Guess a letter: ").lower()

    for index in range(0, len(secretWord)): 
        if guess == secretWord[index]:
            game = game[:index] + secretWord[index] + game[index + 1:]  #replacing char at x index              
    
    if (not (guess in secretWord)):
        tries += 1

    print(game, end=hangmen.hangmen[tries])

    if tries >= 7:
        print("\n\nYou have lost :( \nHope you will win next time")
        exit() #exit the program

print("\n\nCongratulations! You have won :)")