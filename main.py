# Guessing game

from functions import get_score_list, get_top_scores, play_game


while True:

    selection = input("Would you like to A) play game, B) see best scores or C) quit? ")
    if selection == "A":
        level = input("Please, choose level 'easy' or 'hard'. ")
        if level == "easy":
            play_game(level="easy")
        elif level == "hard":
            play_game(level="hard")
        else:
            break
    if selection == "B":
        get_top_scores()
    else:
        break

