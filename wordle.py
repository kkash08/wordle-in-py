from words_dictionary import words_dict
import random

# ANSWER = random.choice(words_dict)
ANSWER ="colin"
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
    correct_index = set()

    def __init__(self, user_guess: str):
        self.user_guess = user_guess
        self.guess_chars = list(self.user_guess)

    def is_valid(self):
        return self.user_guess in words_dict

    def brain_game(self):
        if self.is_winner():
            print("You have won!")
            return False
        if Wordle.counter >= MAX_TURNS:
            if self.is_winner():
                print("You have won!")
                return False
        self.check_guess()
        self.game_over()

    def increase_counter(self):
        Wordle.counter += 1

    def is_winner(self):
        return self.user_guess == ANSWER

    def game_over(self):
        if Wordle.counter > 6:
            if self.is_winner():
                print("You've won!")
            else:
                print("You lost!")
            return False

    def check_guess(self):
        for i in range(5):
            if self.guess_chars[i] == ANSWER[i]:
                self.guess_chars[i] = f"{Color.GREEN}{self.guess_chars[i]}{Color.BASE}"
                Wordle.correct_index.add(i)
            else:
                if self.guess_chars[i] in ANSWER:
                    if i not in Wordle.correct_index:
                        self.guess_chars[i] = f"{Color.YELLOW}{self.guess_chars[i]}{Color.BASE}"
                    else:
                        self.guess_chars[i] = self.guess_chars[i]
                else:
                    self.guess_chars[i] = self.guess_chars[i]

        ans = "".join(self.guess_chars)
        print(ans)
