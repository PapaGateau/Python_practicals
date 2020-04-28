def recuperer_item(liste, index):
    """function to get and element form a list using its index
    incorrect indexes are protected and will return an error string

    Args:
        liste ([list]): [list searched]
        index ([int]): [index of searched element]

    Returns:
        [str]: [list element or error string]
    """
    if index > len(liste) - 1 or index < -len(liste):
        return "Index {} hors de la liste".format(index)
    else:
        return liste[index]

# liste = ["Julien", "Marie", "Pierre"]

# print(recuperer_item(liste, 0))
# print(recuperer_item(liste, 5))
# print(recuperer_item(liste, -13))