import random
from colorama import init, Fore

init()

def hangman():
    words = ["matrix", "neo", "trinity", "morpheus", "agent", "smith", "oracle", "zion", "redpill", "bluepill", "cypher", "architect", "code", "one", "prophecy", "reloaded", "revolutions", "nebuchadnezzar", "sentinels", "virtualreality", "bullettime", "dejavu", "construct", "keymaker", "merovingian", "seraph", "smithclones", "trilogy", "wachowski", "philosophy", "mindbending", "martialarts", "simulation", "freedom", "choice", "reddress", "architectsroom", "whiterabbit", "chateaufight", "oraclescookies", "jumpprogram", "spoon", "speech", "phonebooth", "training", "bug", "trinity", "prophecies", "revolution", "reloaded", "sequels"]
    selected_word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    hangman_stages = [
        """
           _____
          |     |
          |     
          |    
          |      
          |     
         _|_
        """,
        """
           _____
          |     |
          |     O
          |   
          |   
          |   
         _|_
        """,
        """
           _____
          |     |
          |     O
          |     |
          |   
          |   
         _|_
        """,
        """
           _____
          |     |
          |     O
          |    /|
          |   
          |   
         _|_
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |   
          |   
         _|_
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |    /
          |   
         _|_
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |    / \\
          |   
         _|_
        """
    ]

    print("turingblocks' Hangman [Matrix Edition]!")
    print("Try to guess the word by guessing one letter at a time, no spaces.")
    print()

    while True:
        # Display the current state of the word
        display_word = ""
        for letter in selected_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("Word:", display_word)
        print("Guessed Letters:", guessed_letters)
        print("Attempts Left:", max_attempts - attempts)

        # Check if the player has won
        if "_" not in display_word:
            print(Fore.GREEN + "Congratulations! You guessed the word correctly!" + Fore.RESET)
            break

        # Check if the player has lost
        if attempts == max_attempts:
            print(Fore.RED + "Game over! You failed to guess the word." + Fore.RESET)
            print("The word was:", selected_word)
            print(hangman_stages[attempts])
            break

        # Get the player's guess
        guess = input("Enter a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the letter to the guessed letters
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess not in selected_word:
            print("Oops! That letter is not in the word.")
            attempts += 1

        print(hangman_stages[attempts])
        print()

# Run the game
hangman()
