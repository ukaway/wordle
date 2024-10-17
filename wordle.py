import random

# empty list of words
words = []

# open file and add words to the list
with open('words.txt', 'r') as file:
    for line in file:
        line = line.rstrip()  # remove spaces from the line
        words.append(line)

# Choose a target word randomly
target = random.choice(words)

# The player has 6 chances to guess the word
MAX_TURNS = 6
current_turn = 1

# ANSI color codes
RESET = '\033[0m'
GREY = '\033[90m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

print("================================================")
print("Welcome to Wordle!")
print("• Guess the Wordle in 6 tries.")
print("• Each guess must be a valid 5-letter word.")
print("• The color of the tiles will change to ")
print("  show how close your guess was to the word.")
print(f"• {GREEN}Green{RESET} is in the word and in the correct spot.")
print(f"• {YELLOW}Yellow{RESET} is in the word but in the wrong spot.")
print(f"• {GREY}Grey{RESET} is not in the word in any spot.")
print("=================================================")

for g in range(MAX_TURNS):
    # keep asking for input until it gets the existing 5-letter word
    while True:
        try:
            guess = input(f"GUESS {g+1}:  ").lower()
            if not guess.isalpha():  # If the input has letters other than alphabets
                raise Exception("Alphabets only.")
            elif len(guess) != 5:  # if the input is not a 5-letter word
                raise Exception("5 letters only.")
            elif guess not in words:  # if the input is not an existing word
                raise Exception("Not a word.")
        except Exception as e:
            print(f"{e} Try again.")
        else:
            break

    # Make lists of letters from the guess word and the target word
    guess_letters = list(guess)
    target_letters = list(target)

    # Initialize feedback list with incorrect letters
    feedback = [GREY + letter + RESET for letter in guess]

    # Check for correct letters and positions (Make it green)
    for i in range(5):
        if guess_letters[i] == target_letters[i]:
            feedback[i] = GREEN + guess_letters[i] + RESET
            target_letters[i] = None  # Mark the letter as checked

    # Check for misplaced letters (Make it yellow)
    for i in range(5):
        if GREEN not in feedback[i]:  # Skip already green letters
            if guess_letters[i] in target_letters:
                feedback[i] = YELLOW + guess_letters[i] + RESET
                target_letters[target_letters.index(guess_letters[i])] = None  # Mark the letter as checked

    # Print the feedback
    print(f"FEEDBACK: {''.join(feedback)}")

    # Check if the game is won
    win = True
    for i in range(5):
        if GREEN not in feedback[i]:
            win = False
            break

    if win:
        print("Congratulations!")
        break
    else:
        current_turn += 1  # Increment current_turn by 1

    # Game over message if max turns are reached
    if current_turn > MAX_TURNS:
        print(f"Game Over! The correct word was {target}.")

