# Create your Character class logic in here.
class Character:
    def __init__(self, char, was_guessed=False):
        self.char = char.upper()
        self.was_guessed = was_guessed
        
    
    def guessed(self, guess):
        if self.was_guessed == Flase and guess == self.char:
            self.was_guessed = True
            
    def single_character(self):
        title = '{}'
        if self.was_guessed == True:
            return title.format(self.char)
        elif self.char == ' ':
            return title.format(' ')
        else:
            return title.fomat('_')