def replace(string, word_out, word_in):
    """Simple implementation of the replace method

    Args:
        string ([str]): [full input string]
        word_out ([str]): [word being replaced]
        word_in ([str]): [word being inserted]

    Returns:
        [str]: [string with replaced words]
    """
    split_string = string.split(word_out)
    return word_in.join(w for w in split_string)

# string = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
# print(string)