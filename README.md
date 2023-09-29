# Scrabble Score Tracker

This is a Python project for tracking and calculating scores in a game of Scrabble among friends. The project uses dictionaries to organize players, words, and points.

## Introduction

In this project, we process data from a group of friends playing Scrabble. We have provided two lists, `letters` and `points`, representing the Scrabble letter tiles and their corresponding point values. The goal is to create a dictionary that maps each letter to its point value.

## Implementation

We start by combining the `letters` and `points` lists into a dictionary named `letter_to_points`. This dictionary is used for scoring words played in the game.

We define a function called `score_word(word)` that calculates the score for a given word based on the `letter_to_points` dictionary.

We then create a dictionary called `player_to_words` that maps players to a list of words they have played. Additionally, an empty dictionary named `player_to_points` is created to calculate each player's total points.

The `update_point_totals()` function iterates through the `player_to_words` dictionary, calculates the points for each player, and updates the `player_to_points` dictionary.

The `play_word(player, word)` function allows players to add words they've played to their respective lists in `player_to_words`. It also updates the points for the player using `update_point_totals()`.

## Example Usage

Here's how you can use the functions in this project:

```python
# Calculate the score for a word
print(score_word("BROWNIE"))  # Output: 15

# Add a word played by a player
play_word("player1", "patates")

# Print the updated player data
print(player_to_words)
print(player_to_points)
