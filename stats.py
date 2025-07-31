def get_num_words(text):
    word_list = text.split()
    count = len(word_list)
    return count

def get_characters_counts(text):
    Dict = {}
    text = text.lower()
    for i in text:
        if i in Dict.keys():
            Dict[i] += 1
        else:
            Dict[i] = 1

    return Dict