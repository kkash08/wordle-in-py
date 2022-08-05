import wordle


if __name__ == "__main__":
    is_game_on = True
    with open("cheat.txt", "w") as file:
        file.write(wordle.ANSWER)
    while is_game_on:
        if is_game_on is True:
            current_game = wordle.Wordle(
                user_guess=str(input(">"))
            )
            if current_game.is_valid():
                current_game.increase_counter()
                print(current_game.counter)
                x = current_game.brain_game()
                print(x)
                if x is False:
                    is_game_on = False


