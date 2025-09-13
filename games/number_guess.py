import random

def play_game():
    print("🎲 Welcome to the Number Guessing Game!")
    
    # Let the user set the range
    while True:
        try:
            lower = int(input("Enter the lower bound of the range: "))
            upper = int(input("Enter the upper bound of the range: "))
            if lower >= upper:
                print("❌ Upper bound must be greater than lower bound. Try again.")
                continue
            break
        except ValueError:
            print("❌ Please enter valid numbers.")

    target = random.randint(lower, upper)
    print(f"I'm thinking of a number between {lower} and {upper}.")
    
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        attempts += 1

        if guess < target:
            print("⬆ Too low! Try again.")
        elif guess > target:
            print("⬇ Too high! Try again.")
        else:
            print(f"✅ Congratulations! You guessed it in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        # Ask if the user wants to play again
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
