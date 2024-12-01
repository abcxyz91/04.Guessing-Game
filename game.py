import random

difficulty = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

def main():
    game_start()
    while True:
        user_confirmation = input("Do you want to continue playing? (Yes/No?)").lower().strip()
        if user_confirmation == "y" or user_confirmation == "yes":
            print("\n")
            game_start()
        if user_confirmation == "n" or user_confirmation == "no":
            print("Thank you for playing")
            break
        else:
            print("Invalid answer")


def game_start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have some chances to guess the correct number.")
    print("\n")

    chances, user_choice = difficult_level()

    print(f"Great! You have selected the {difficulty[user_choice]} difficulty level.")
    print("Let's start the game!")
    print("\n")

    random_number = random.randint(1, 100)
    attempts = 0

    for i in range(chances):
        try:
            user_number = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Invalid number")
        if user_number == random_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print("\n")
            break
        elif user_number > random_number:
            print(f"Incorrect! The number is less than {user_number}.")
            print("\n")
        else:
            print(f"Incorrect! The number is more than {user_number}.")
            print("\n")
    else:
        print(f"Unfortunately you have run out of your chances. The number I think of is {random_number}")
        print("\n")


def difficult_level():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                return 10, user_choice
            elif user_choice == 2:
                return 5, user_choice
            elif user_choice == 3:
                return 3, user_choice
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")
        

if __name__ == "__main__":
    main()