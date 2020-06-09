# Import your Game class
from phrasehunter.game import Game
from phrasehunter.constants import stored_phrases
# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
if __name__ == '__main__':
    game = Game(stored_phrases)
    try:
            game.run_game()
    except KeyboardInterrupt:
            print("\nThanks for playing!")
