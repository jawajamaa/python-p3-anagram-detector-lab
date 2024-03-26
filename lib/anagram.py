x = "listen"
possible = ["enlists", "google", "inlets", "banana"]

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        if isinstance(word, str) and len(word) > 1:
            self._word = word.lower()
        else:
            raise ValueError("'word' must not be an empty string!")
        
    def match(self, match_list):
        confirm_match = list()
        for item in match_list:
            if sorted(self.word) == sorted(item.lower()):
                confirm_match.append(item)
        return confirm_match
