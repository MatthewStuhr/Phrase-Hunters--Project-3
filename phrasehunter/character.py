# Create your Character class logic in here.
class Character:
    """Responsible for holding the state of a char (guessed character)"""
    def __init__(self, char, was_guessed = False):
        self.char = char.upper()
        self.was_guessed = was_guessed

    def update_guessed(self, guess):
        if self.was_guessed == False and guess == self.char:
            self.was_guessed = True

    def show_single_character(self):
        tile = '{}'
        if self.was_guessed == True:
            return tile.format(self.char)
        elif self.char == ' ':
            return tile.format(' ')
        else:
            return tile.format('_')
