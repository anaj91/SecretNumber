# Lekcija 6 (2. domača naloga)

SecretNumber = 19

print("Try to guess the secret number. You can pick numbers between 1-40. You have 5 guesses.")


for x in range(5):
    Guess = input("Your guess:")
    if SecretNumber == Guess:
        print("You are the luckiest person I know. You picked the right number.")
        break
    else:
        print("Sorry, your guess is not correct. The secret number is not" " " + str(Guess))


