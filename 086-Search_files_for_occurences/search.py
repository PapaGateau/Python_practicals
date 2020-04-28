import os
from glob import glob

def search_dir(needle):
    """Search current directory recursively for files containing needle

    Args:
        needle ([str]): [target of search]

    Returns:
        [list]: [list of filepaths containing needle]
    """
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    result = []
    files = glob(cur_dir + "/**/*.txt", recursive=True)
    for filename in files:
        with open(filename, "r") as f:
            if needle in f.read():
                result.append(filename)
    return result

print(search_dir("Python"))