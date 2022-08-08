import sys

from words_wordle import words_dict
import random

choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
ANSWER_KEY = random.choice(choices)
ANSWER = random.choice(words_dict[ANSWER_KEY])
# ANSWER = "colin"
MAX_TURNS = 6


class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PERSISTENT_COLORS = [RED, GREEN]


class Wordle:
    counter = 0
    green_chars = set()
    all_guesses = []
    alphabets_status = {'a': 'a',
                        'b': 'b',
                        'c': 'c',
                        'd': 'd',
                        'e': 'e',
                        'f': 'f',
                        'g': 'g',
                        'h': 'h',
                        'i': 'i',
                        'j': 'j',
                        'k': 'k',
                        'l': 'l',
                        'm': 'm',
                        'n': 'n',
                        'o': 'o',
                        'p': 'p',
                        'q': 'q',
                        'r': 'r',
                        's': 's',
                        't': 't',
                        'u': 'u',
                        'v': 'v',
                        'w': 'w',
                        'x': 'x',
                        'y': 'y',
                        'z': 'z'}

    def __init__(self, user_guess: str):
        self.user_guess = user_guess
        self.guess_chars = list(self.user_guess)

    def is_valid(self):
        return self.user_guess in words_dict[self.user_guess[0]]

    def brain_game(self):
        self.check_guess()
        ans = "".join(self.guess_chars)
        Wordle.all_guesses.append(ans)
        print(ans)

    def print_all_guesses(self):
        for ele in Wordle.all_guesses:
            print(ele)

    def increase_counter(self):
        Wordle.counter += 1

    def check_perfect_guess(self):
        if self.user_guess == ANSWER:
            ans = "".join(self.guess_chars)
            Wordle.all_guesses.append(f"{Color.GREEN}{ans}{Color.YELLOW}")
            print(f"You have won in {Wordle.counter} chance/s! :)")
            self.print_all_guesses()
            sys.exit(1)

    def check_game_over(self):
        if MAX_TURNS == Wordle.counter:
            print(f"You lost! Better luck next time!")
            print(f"The word was {ANSWER}")
            sys.exit(1)

    def check_guess(self):
        for i in range(5):
            if self.guess_chars[i] == ANSWER[i]:
                Wordle.green_chars.add(self.guess_chars[i])
                self.change_alphabet_status(self.guess_chars[i], "green")
                self.guess_chars[i] = f"{Color.GREEN}{self.guess_chars[i]}{Color.BASE}"
            elif self.guess_chars[i] in ANSWER and self.guess_chars[i] not in Wordle.green_chars:
                self.change_alphabet_status(self.guess_chars[i], "yellow")
                self.guess_chars[i] = f"{Color.YELLOW}{self.guess_chars[i]}{Color.BASE}"
            else:
                self.change_alphabet_status(self.guess_chars[i], "grey")

        self.print_alphabet_status()

    def change_alphabet_status(self, char, color):
        if color == "green":
            Wordle.alphabets_status[char] = f"{Color.GREEN}{char}{Color.BASE}"
        elif color == "yellow":
            Wordle.alphabets_status[char] = f"{Color.YELLOW}{char}{Color.BASE}"
        elif color == "grey":
            Wordle.alphabets_status[char] = f"{Color.GREY}{char}{Color.BASE}"

    def print_alphabet_status(self):
        for key, value in Wordle.alphabets_status.items():
            print(value, end=" ")
        print("")
