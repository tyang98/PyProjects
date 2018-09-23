# hangman.py
# Anne Bracy (awb93)
# March 28, 2018

"""Module with one class: a SecretWord"""

class SecretWord():
    """A word to be guessed by a user in a game of hangman.
    
    Instance attributes:
       secret_word: the word being guessed [str of lower case letters]
       display_word: word as the user sees it: the letters of secret_word show
           correctly guessed letters [str of lower case letters and '_']
    secret_word and display_word agree on all letters and have same length
    """
    
    def __init__(self, word):
        """Initializer: creates both secret_word and display_word
        from word [a str of lower case letters]
        """
        self.secret_word = word
        self.display_word = len(word)*'_'

    def word_so_far(self):
        """Prints the word being guessed"""
        print("So far you have: "+self.display_word)

    def reveal(self):
        """Prints the word being guessed"""
        print("The word was "+self.secret_word)

    def apply_guess(self, letter):
        """Updates the display_word to reveal all instances of letter as they 
        appear in the secret_word. (‘_’ is replaced with letter)
        letter: the user's guess [1 character string A..Z]
        """
        lower_letter = letter.lower()
        for i in list(range(len(self.secret_word))):
            if self.secret_word[i] == lower_letter:
                self.display_word = self.display_word[:i] + lower_letter + self.display_word[i+1:]

    def is_solved(self):
        """Returns True if the entire word has been guessed"""
        return self.secret_word == self.display_word

