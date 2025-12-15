def get_num_words(contents):
    words = contents.split()
    return len(words)


def get_chars(contents):
    chars = {}

    for c in contents.lower():
        chars[c] = chars.get(c, 0) + 1

    return chars


def get_chars_list(chars_dict):
    chars = []

    for key, val in chars_dict.items():
        chars.append({"char": key, "num": val})

    chars.sort(key=sort_on, reverse=True)

    return chars


def sort_on(items):
    return items["num"]
