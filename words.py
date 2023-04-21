def print_upper_words(words, must_start_with):
    '''This function takes a list of words and prints them out one
    line at a time while all uppercase'''
    for word in words:
        word = word.upper()
        for filter in must_start_with:
            if (filter[0].upper() == word[0]):
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
