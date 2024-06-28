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
        print("Wrong guess!")
        remaining_guesses -= 1
        print(remaining_guesses, "guesses remaining")


def play_game():
    print(user_progress)
    user_input = input("Guess a letter: ")
    if user_input == "":
        play_game()
    update_progress(user_input, word_list)


while not game_over:
    play_game()
    if remaining_guesses == 0:
        game_over = True
        print("You lost! The word was:", random_word)
    elif "_" not in user_progress:
        game_over = True
        print("Congratulations! You won!")
