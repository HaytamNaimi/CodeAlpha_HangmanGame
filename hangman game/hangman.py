import random

with open("words.txt", "r") as file:
    lines = file.readlines()
    lst = [line.strip() for line in lines]

final = "yes"

while final == "yes":
    word = random.choice(lst)
    print("--------------HANGMAN GAME----------------:")
    c = input("Do you wish to play?(yes/no): ")

    if c.lower() == "yes":
        print("--------------WELCOME TO HANGMAN GAME--------------")
        print("Try to guess the word (you have 6 attempts):")

        display = ["_"] * len(word)
        print(" ".join(display), "\n")

        user_guesses = []
        wrong_guesses = 0
        max_attempts = 6

        while wrong_guesses < max_attempts and "_" in display:
            # Input validation
            while True:
                attempt = input("Enter a single letter: ").lower()
                if len(attempt) == 1 and attempt.isalpha():
                    if attempt in user_guesses:
                        print("You already guessed that letter! Try again.")
                    else:
                        break
                else:
                    print("Invalid input. Please enter exactly one letter.")

            # Track guesses
            user_guesses.append(attempt)

            # Check guess
            if attempt.lower() not in word.lower():
                wrong_guesses += 1
                remaining_attempts = max_attempts - wrong_guesses
                print("Wrong guess! Remaining attempts:", remaining_attempts)
            else:
                print("Correct guess!")

            # Update display
            for i in range(len(word)):
                if word[i].lower() == attempt:
                    display[i] = word[i]

            # Show updated display
            print(" ".join(display), "\n")
            print("Letters guessed so far:", ", ".join(user_guesses), "\n")

        # End game message
        if "_" not in display:
            print("---------CONGRATULATIONS! YOU WON!---------")
        else:
            print("---------GAME OVER! The word was:", word, "---------")

    # Ask to play again after each game
    final = input("Do you want to play again? (yes/no): ").lower()





