import random
import time
import json
from pathlib import Path

difficulty = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

"""Load the highscore from the existing file"""
highscore_path = "highscore.json"

if Path(highscore_path).exists():
    with open(highscore_path, "r") as file:
        try:
            highscore = json.load(file)
        except json.JSONDecodeError:
            print("Error: highscore file is corrupted")
else:
    highscore = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0
    }


def main():
    game_start()
    """Using a while loop to continously asking player"""
    while True:
        user_confirmation = input("Do you want to continue playing? (Yes/No?)").lower().strip()
        if user_confirmation == "y" or user_confirmation == "yes":
            print("\n")
            game_start()
        elif user_confirmation == "n" or user_confirmation == "no":
            print("Thank you for playing")
            break
        else:
            print("Invalid answer")


def game_start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have some chances to guess the correct number.")
    print("\n")

    """difficult_level function return 2 values"""
    chances, user_choice = difficult_level()

    print(f"Great! You have selected the {difficulty[user_choice]} difficulty level.")
    print("Let's start the game!")
    print("\n")

    """Start counting time"""
    start_time = time.time()

    """Randomize a number and use a for loop to continously asking player to answer"""
    random_number = random.randint(1, 100)
    attempts = 0

    for i in range(chances):
        """Check if user input is a number or not"""
        try:
            user_number = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("You must input a number between 1-100")
            continue
        """If a valid number, check if user's guess is correct"""
        if user_number == random_number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts} attempts and took {elapsed_time:.1f} seconds.")
            
            """Check if player achieve highscore in this difficulty or highscore not yet set
            And record the highscore into the json file"""
            if highscore[difficulty[user_choice]] == 0:
                save_highscore(difficulty[user_choice], attempts)
            elif highscore[difficulty[user_choice]] != 0 and attempts < highscore[difficulty[user_choice]]:
                print(f"You also achieved highscore in {difficulty[user_choice]} difficulty!")
                save_highscore(difficulty[user_choice], attempts)

            print("\n")
            break
        elif user_number > random_number:
            print(f"Incorrect! The number is less than {user_number}.")
            print("\n")
        else:
            print(f"Incorrect! The number is more than {user_number}.")
            print("\n")
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Unfortunately you have run out of your chances. The number I think of is {random_number}")
        print(f"You took {elapsed_time:.1f} seconds")
        print("\n")


def difficult_level():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    """Using a while loop to keep asking until the player types in valid answer"""
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


def save_highscore(level, score):
    with open(highscore_path, "w") as file:
        highscore[level] = score
        json.dump(highscore, file, indent=2)


if __name__ == "__main__":
    main()