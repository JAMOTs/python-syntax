def print_upper_words(words):
    for word in words:
        print(words.upper())
    
def print_words_upper2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_words_upper3(words, must_start_with):
    """Print each word on a seperate line, uppercased, only if it contains the set of letters defined in must_start_with"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
