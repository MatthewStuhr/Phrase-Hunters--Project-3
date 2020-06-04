# Create your Game class logic in here.
import random
import os

from .phrase import Phrase

class Game:
    def __init__(self, phrases):
        self.start_game = True
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.guessed_phrases = []
        
    def fetch_guess(self, user_input):
        correct_guess = False