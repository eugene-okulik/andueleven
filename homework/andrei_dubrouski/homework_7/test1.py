stored_number = 11

user_guess = None

while user_guess != stored_number:
    user_guess = int(input("Guess the number: "))

    if user_guess == stored_number:
        break
    else:
        print("Please try again.")

print("Congratulations! You guessed it!")
