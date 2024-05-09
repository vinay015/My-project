import random


def guesses():
    while True:
        x = int(input("Enter a Range"))
        if x == 0:
            print("Please enter a number is greater than 0")
        if x > 0:
            break
    random_no = random.randint(1, x)
    guess = 0
    guess_range = 3
    while guess < guess_range:
        guess += 1
        user_guess = int(input(f"enter no  b/w 1 and {x}"))
        if user_guess == random_no:
            print(f"correct guess,  Number is: {random_no} ")
            break
        else:
            if user_guess < random_no:
                print(f"Your Guess {user_guess} is less than random_number ")
            elif user_guess > random_no:
                print(f"Your Guess {user_guess} is greater than  random_number")
        if guess == guess_range:
            print("Times up")
            break
    print(f"you guesses in {guess}")


print(guesses())
