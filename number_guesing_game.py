def check_guess(user_guess, secret_number):
    if user_guess > secret_number:
        return "Too high"
    elif user_guess < secret_number:
        return "Too low"
    else:
        return "Correct"
print("Guess the number between 1 and 50")
secret_number = int(input("Enter secret number (1 to 50): "))
chances = 5
for i in range(chances):
    user_guess = int(input(f"Chance {i+1}: Enter your guess: "))
    result = check_guess(user_guess, secret_number)
    print(result)
    if result == "Correct":
        print("You Win")
        break
else:
    print(f"Game Over! The number was {secret_number}")