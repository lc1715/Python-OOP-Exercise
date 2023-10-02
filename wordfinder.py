"""Word Finder: finds random words from a dictionary."""
# file = open('words.txst', 'r')


def turn_to_lst():
    file = open('words.txt', 'r')

    return [line.strip() for line in file]

    
class WordFinder:
    """
    WordFinder: finds random words from a file.

    >>> wf = WordFinder('words.txt')
    11 words read

    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    >>> wf.random() in ['cat', 'dog', 'rat', '', '# Veggies', 'kale', 'parsnips', '', '# Fruits', 'apple', 'mango']
    True
    """

    def __init__(self, file_name):
        """
        Counts the total words in a file
        """
        self.file_name = file_name
        
        file = open(file_name, 'r')

        total_words= 0

        for line in file:
            total_words += 1
        
        print(f'{total_words} words read')

        file.close()


    def __repr__(self):
        """
        WordFinder will execute on this file name
        """
        return f'<WordFinder filename:{self.file_name}>'


    def random(self):
        """
        Returns a random word
        """
        from random import choice

        file = open(self.file_name, 'r')

        word_lst = [line for line in file]

        word = choice(word_lst).strip()
 
        return word



class SpecialWordFinder(WordFinder):
    """
    Returns a random word without hashtags (#), spaces or empty strings
    """

    def __init__(self, file_name):
        """
        Counts the total number of lines in the file
        """
        super().__init__(file_name)


    def random(self):
        """
        Returns a random word without hashtag(#) or spaces
        """
        rand_word = super().random().strip()

        while '#' in rand_word or len(rand_word) == 0:
            rand_word = super().random().strip()

        return rand_word

     



















