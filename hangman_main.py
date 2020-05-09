import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_ " * len(word)
    not_guessed = True
    guessed_words = []
    guessed_letters = []
    tries = 6  # (head + body + 2 hands + 2 legs)

    print("Let's play Hangman!!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not_guessed and tries > 0:

        guess = input("Please guess a letter or a word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed ", guess, " earlier!")

            elif guess not in word:
                print(guess, "is not in the word")
                tries = tries - 1
                guessed_letters.append(guess)

            else:
                print("Good Job, ", guess, " is in the word")
                guessed_letters.append(guess)
                word_list = word_completion.split()


                for i in range(len(word)):
                    if word[i] == guess:
                        word_list[i] = guess

                word_completion = ' '.join(word[0] for word in word_list)
                if "_ " not in word_completion:
                    not_guessed = False

        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print("You've already guessed ", guess, " earlier!")

            elif guess != word :
                print(guess, " is not the word.")
                tries = tries-1
                guessed_words.append(guess)

            else:
                not_guessed = False
                word_completion = word

        else:
            print("Not a valid guess")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if not not_guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    answer = input("Play again? Y/N ").upper()
    if answer == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()