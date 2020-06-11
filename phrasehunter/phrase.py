# Create your Phrase class logic here.
from .character import Character


class Phrase:
    """Phrase class responible for knowing if/when the entire phrase has been guessed"""
    current_letter_index = []
    
    def __init__(self, phrase):
        self.phrase = [Character(letter) for letter in phrase]
        self.phrase_ = phrase
    
    def entire_guessed(self):
        for letter in self.phrase:
            if letter.was_guessed == False:
                return False
        return True
    
    def show_guessed_phrase(self):
        for letter in self.phrase:
            print(letter.show_single_character(), end=' ')
        print(' ')
        
    def phrase_again(self):
        for character in self.phrase:
            character.was_guessed = False
            
    def exists(self, user_input):
        for letter in self.phrase:
            if letter.char == user_input:
                return True
        return False
    
    def check_guess(self, guess):
        for char in self.phrase:
            char.update_guessed(guess)
