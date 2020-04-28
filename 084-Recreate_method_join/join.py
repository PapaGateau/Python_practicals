def join(*args):
    """Simple implementation of join() method
        
    Args:
        arg1 ([str]): [separator]
        arg2 ([str]): [first element]
        ...
    Returns:
        str: ret // joined_string
    """
    i = 2
    if args[1]:
        ret = args[1]
        while i < len(args):
            ret = ret + args[0] + args[i]
            i += 1
    return ret