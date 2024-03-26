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
        
    def match(word, match_list):
        confirm_match = list()
        for item in match_list:
            if sorted(word) == sorted(item):
                confirm_match.append(item)
        return confirm_match

        
    # def match(word, match_list):
    #     confirm_match = list()
    #     for item in match_list:
    #         # breakpoint()
    #         if word == item:
    #             confirm_match.append(item)
    #             breakpoint()
    #             return confirm_match
    #         elif word != item:
    #             return confirm_match
