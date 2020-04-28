def isdigit(nombre):
    """Simple implementation of isdigit() method

    Args:
        nombre ([str]): [number string]

    Returns:
        [bool]: [True if only digit]
    """
    for i in nombre:
        if i not in [str(n) for n in range(10)]:
            return False
    return True