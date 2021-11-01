import json
import datetime
import random

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    score_list2 = sorted(score_list, key=lambda x: x["attempts"])
    return top_score_list

class Results:
    def __init__(self, score, user, date):
        self.score = score
        self.user = user
        self.date = date

def play_game(level="level"):
    score_list = get_score_list()
    secret = random.randint(1, 30)
    user = input("Write your name:")
    attempts = 0
    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        wrong_guesses.append(guess)

        if guess == secret:
            result = Results(score=attempts, user=user, date=str(datetime.datetime.now()))

            score_list.append(result.__dict__)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")

        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
        else:
            print("Your guess is not correct.")
