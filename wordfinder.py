import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, path):
        self.path = path
        file = open(path, 'r')
        self.word_list = []
        self.word_count = 0
        for line in file:
            self.word_list.append(line)
            self.word_count += 1
        print(f"{self.word_count} words read")

    def random(self):
        """Returns a random word from list of words in file."""
        return self.word_list[random.randrange(len(self.word_list))]

