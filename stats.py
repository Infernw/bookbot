def get_num_words(text):
    word_list = text.split()
    count = len(word_list)
    return count

def get_characters_counts(text):
    Dict = {}
    text = text.lower()
    for i in text:
        if i in Dict:
            Dict[i] += 1
        else:
            Dict[i] = 1

    return Dict

def sort_on(items):
    return items["num"]

def sorted_char_counts(count_dict):
    char_list = []
    for i in count_dict:
        if i.isalpha():
            char_list.append({"char": i, "num": count_dict[i]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list