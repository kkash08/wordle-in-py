import wordle
import os

os.system("cls")
LOGO = """
 _       ___   ___   ___   _     ____ 
\ \    // / \ | |_) | | \ | |   | |_  
 \_\/\/ \_\_/ |_| \ |_|_/ |_|__ |_|__
"""
if __name__ == "__main__":
    print(LOGO)
    is_game_on = True
    with open("cheat.txt", "w") as file:
        file.write(wordle.ANSWER)
    while is_game_on:
        if is_game_on is True:
            current_game = wordle.Wordle(
                user_guess=str(input(f"{wordle.Wordle.counter + 1}>"))
            )
            if current_game.is_valid():
                current_game.increase_counter()
                current_game.check_perfect_guess()
                current_game.check_game_over()
                current_game.brain_game()
