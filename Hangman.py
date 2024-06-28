import random

game_over = False
remaining_guesses = 3

word_options = ["pulchowk", "ioe", "kathmandu", "lalitpur", "bhaktapur", "balen"]

random_word = word_options[random.randint(0, len(word_options) - 1)]

word_list = list(random_word)
user_progress = list("_" for _ in word_list)


def update_progress(guess, word_list):
    global remaining_guesses
    found = False
    for index, letter in enumerate(word_list):
        if letter == guess:
            user_progress[index] = letter
            found = True
    if not found:
        print("\nWrong guess!")
        remaining_guesses -= 1
        print(f"\n{remaining_guesses} guesses remaining")


def play_game():
    global game_over
    print("\n-------------------")
    print("Welcome to Hangman!")
    print("-------------------")
    print("\nTry to guess the word!")

    while not game_over:
        print("\n", " ".join(user_progress))
        user_input = input("\nGuess a letter: ").lower()
        if user_input == "":
            continue
        update_progress(user_input, word_list)

        if remaining_guesses == 0:
            game_over = True
            print(f"\nYou lost! The word was: {random_word}\n")
        elif "_" not in user_progress:
            game_over = True
            print("\n", " ".join(user_progress))
            print("\nCongratulations! You won!\n")

    print("=====================")
    print("Thank you for playing!")
    print("=====================")


if __name__ == "__main__":
    play_game()
