class Character:
    "Defualting was_guessed to False as the character has not been guess before"
    def __init__(self, original, was_guessed=False):
        self.original = original
        self.was_guessed = was_guessed
        if len(original) != 1:
            raise ValueError("Please enter 1 letter at a time.")
        
    def new_guess(self, guess):
        """ An instance method that will take a single string character guess as an argument when its 
        called. The job of this instance method is to update the instance attribute storing the boolean 
        value, if the guess character is an exact match to the instance attribute storing the original 
        char passed in when the Character object was created. """
        if self.guess.upper() == self.original.upper():
            self.was_guessed = True
            
            
    def given_single_character(self):
        character = '{}'
        """ An instance method that when called, will show the original character if the instance 
        attribute was_guessed is True. Otherwise, the instance method should show an _ or underscore 
        character to act as a hidden placeholder character. """
        if self.was_guessed == True:
            return character.format(self.original)
        elif self.original == ' ':
            return character.format(' ')
        else:
            return character.format('_')
