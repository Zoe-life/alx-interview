# 0x0A-primegame

This project contains a Python function `isWinner(x, nums)` that determines the winner of a game played between Maria and Ben.  The game involves choosing prime numbers from a set of consecutive integers and removing their multiples.  The player who cannot make a move loses.

## Task

The task is to implement the `isWinner` function, which takes the number of rounds `x` and a list of `n` values (representing the upper bound of the integer set for each round) as input. The function should return the name of the player who wins the most rounds ("Maria" or "Ben"). If there's a tie, it should return `None`.

## Functionality

The `isWinner` function simulates the game for each round. It identifies prime numbers within the given range, and then simulates the players' turns, removing chosen primes and their multiples.  It counts the wins for each player and determines the overall winner.

## Example
- Round 1 (n=4): Ben wins
- Round 2 (n=5): Maria wins
- Round 3 (n=1): Ben wins

Result: "Ben"

## Usage

```bash
./main_0.py
