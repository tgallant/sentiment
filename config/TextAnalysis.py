from enchant.checker import SpellChecker
from SyllableCounter import CountSyllables as cs
from sentiment2 import sentiment as sa

class Analysis:
    
    def __init__(self, text):
        self.text = text
    
    def spellcheck(self):
        errs = 0
        words = []
        chkr = SpellChecker("en_US")
        chkr.set_text(self.text)
        for err in chkr:
            errs += 1
            words.append(err.word)
        return [errs, words]

    def syllablecount(self):
        syllables = 0
        words = 0
        for x in self.text.split():
            syllables += cs(x)
            words += 1
        return [syllables, words, float(syllables)/words]

    def sentiment(self):
        return sa(self.text)
