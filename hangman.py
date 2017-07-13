import os
import random


def main():
    with open('master_list.txt', 'r') as master_file:
        master_list = master_file.readlines()

    should_continue = 'y'
    total_score = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = input("Hey there, what is your name?\n")

    # Start the game
    while 'y' in should_continue.lower():
        actual_answer = list(random.choice(master_list))[:-1]
        guess_string = construct_guess_string(actual_answer)
        incorrect_list = []
        hangman_string = ['H', 'A', 'N', 'G', 'M', 'A', 'N']

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Hangman {}! Let's begin the guessing game".format(
            user_name))
        input("Press the enter key to start the game...\n")

        while len(incorrect_list) < len(hangman_string):
            # This means the user has more chances to play
            print(" ".join(guess_string))
            user_choice = input("What's your guess? ").upper()

            if user_choice == '':
                # User pressed only the Enter key
                continue

            if user_choice in incorrect_list:
                # An alphabet has been re-played. Doesn't count
                print("Alphabet already played. Try a different alphabet")
                continue

            if user_choice in actual_answer:
                # Get all the positions of this alphabet in the actual answer
                positions = [i for i, x in enumerate(actual_answer) if
                             x == user_choice]

                # Update the alphabet in those respective positions
                guess_string = update_guess_string(guess_string, user_choice,
                                                   positions)

                # Check if the full word is done
                if "".join(guess_string) == "".join(actual_answer):
                    break
            else:
                # This alphabet doesn't appear in the word.
                print('Oops! This is not in the word. Try again')
                incorrect_list.append(user_choice)

                # Print H-A-N-G-M-A-N iteratively. One alphabet is printed
                # when each mistake is made.
                print("{}\n".format(
                    "-".join(hangman_string[:len(incorrect_list)])))

        if "".join(guess_string) == "".join(actual_answer):
            # The correct word has been guessed
            print("".join(actual_answer))
            print("You got it right!")
            total_score += 1
        else:
            # Word wasn't guessed in the given 7 wrong chances
            print("Better luck next time! You lost :(")
            print("The actual word was {}".format("".join(actual_answer)))
            total_score -= 1

        # Want to play again?
        should_continue = input("Do you want to play again? (y/n) ")

    # Total score based on the games played so far.
    print("{}, Your total score is {}".format(
        user_name,
        0 if total_score < 0 else total_score))
    print("Hope you enjoyed playing this game. Come back soon!")


def construct_guess_string(answer):
    empty_string = []
    for character in answer:
        if character.isalpha():
            empty_string.append('-')
        else:
            empty_string.append(character)

    return empty_string


def update_guess_string(guess_string, user_choice, positions):
    for position in positions:
        guess_string[position] = user_choice

    return guess_string

if __name__ == "__main__":
    main()
