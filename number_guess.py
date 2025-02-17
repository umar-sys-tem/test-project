import random

def number_guessing_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 50. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
