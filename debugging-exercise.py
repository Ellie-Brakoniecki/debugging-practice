import random


def generate_random_number():
    return random.randint(1, 100)


def guess_the_number(random_number):
    for i in range(10):
        guess = input("Enter your guess between 1 and 100: ")

        if not guess.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        guess = int(guess)

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations, you've found the number: {guess} in {i+1} tries")
            return

    print(f"Sorry, you didn't guess the number. The number was: {random_number}")


def main():
    random_number = generate_random_number()
    guess_the_number(random_number)


if __name__ == "__main__":
    main()