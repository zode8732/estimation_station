print("started game")

game_state = True

while game_state:
    import game
    game.run()
    if input("play again? (y/n) : ") == "n":
        game_state = False

print("gg")

# done