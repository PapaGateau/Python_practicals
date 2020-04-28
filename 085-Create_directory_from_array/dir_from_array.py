# import string
import os

def artodir(array):
    """Creates local directory for each element in array

    Args:
        array (list): [list of strings]
    """
    cur_dir = os.path.dirname(os.path.realpath(__file__))

    for element in array:
        if not os.path.isdir(element):
            os.makedirs(os.path.join(cur_dir, element))

# array = string.ascii_uppercase
# artodir(array)