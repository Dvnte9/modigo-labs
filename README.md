# modigo-labs
My coding labs and checkpoints from Modigo learning platform.

Number Guessing Game

You'll build a classic guessing game: the program picks (stores) a secret number, and the user keeps guessing until they land on it — getting a hint after every wrong guess.

Instructions
Write a program that:

Stores a secret number in a variable (e.g., secret_number = 7).
Asks the user to guess the number using exactly this prompt: "Guess the number: "
If the guess is higher than the secret number, prints: "Too high!"
If the guess is lower than the secret number, prints: "Too low!"
If the guess is correct, prints: "Correct! You guessed the number." and stops.
Keeps asking until the user guesses correctly — there is no attempt limit.

Rules
You must use a while loop.
You must use if / elif / else to compare the guess against the secret number.
The program must stop immediately once the correct number is guessed — no further prompts after that.
Do not use a for loop.
Do not use functions.
Remember input() returns a string — convert the guess to an integer before comparing it to the secret number.
