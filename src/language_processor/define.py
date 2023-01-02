from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()

def define_word(input_language : str = None, word : str = None) -> tuple:
    if input_language and word:
        return dictionary.meaning(input_language, word)