# Lekcija 6 (2. domača naloga)

import json
import datetime
import random

secret = random.randint(1, 30)
attempts = 0
user = input("Write your name:")


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list2 = sorted(score_list, key=lambda x: x["attempts"])
    print("Top scores: " + str(score_list2[:3]))

for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}." \
                 " Wrong guesses were {4}.".format(score_dict.get("user"),
                                            score_dict.get("attempts"),
                                            score_dict.get("date"),
                                            score_dict.get("secret_number"),
                                            score_dict.get("wrong_guesses"))

wrong_guesses = []
while True:
     guess = int(input("Guess the secret number (between 1 and 30): "))
     attempts += 1

     if guess == secret:
         score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "user": user, "secret_number": secret, "wrong_guesses": wrong_guesses})
         with open("score_list.json", "w") as score_file:
             score_file.write(json.dumps(score_list))

         print("You've guessed it - congratulations! It's number " + str(secret))
         print("Attempts needed: " + str(attempts))
         break
     elif guess > secret:
         print("Your guess is not correct... try something smaller")

     elif guess < secret:
         print("Your guess is not correct... try something bigger")

     wrong_guesses.append(guess)