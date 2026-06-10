
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game to practice Python strings, loops, conditionals, and user input while managing game state.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a list of words and randomly choose one word for the player to guess.

#### Requirements
Completed program should:

- Use a predefined list of words
- Randomly select a target word for each game
- Initialize a hidden display for the word using underscores

### 🛠️ Player Input and Guess Tracking

#### Description
Accept letter guesses, update the word display, and track the player's progress.

#### Requirements
Completed program should:

- Prompt the player to guess one letter at a time
- Reveal correct letters in the current word display
- Track letters that have already been guessed
- Deduct attempts only for incorrect guesses

### 🛠️ Win/Lose Logic and Feedback

#### Description
End the game when the player guesses the word or runs out of attempts, then show a result message.

#### Requirements
Completed program should:

- Win when all letters are revealed
- Lose when the player uses all attempts
- Display a clear win or lose message with the correct word
- Optionally offer the player a chance to play again
