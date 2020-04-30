def get_value(*args):
    """simple function to get a value from a list of keys

    Args:
        args[0] is the dictionary
        args[1:-1] are the keys
        args[-1] is the message to be returned if value isn't found

    Returns:
        [str]: [value or provided string]
    """
    d = args[0]
    for value in args[1:-1]:
        d = d.get(value)
        if not d:
            return(args[-1])
    return (d)
    

# dictionnaire = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# a = get_value(dictionnaire, "01", "identite", "prenom", "valeur inconnue")
# print(a)