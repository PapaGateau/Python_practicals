def split(string, separator):
    """Simple implementation of the split method

    Args:
        string ([str]): [input string to be split]
        separator ([char]): [string will be divided around this character]

    Returns:
        [list]: [list of split words]
    """
    ret = []
    current = ""
    for letter in string:
        if letter != separator:
            current += letter
        elif letter == separator:
            ret.append(current)
            current = ""
    ret.append(current)
    return ret

# phrase = "bonjour-tout-le-monde"
# print(split(phrase, "-"))