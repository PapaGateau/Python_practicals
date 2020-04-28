class SuperStr(str):
    """
    This class recursively adds each string to itself
    using the __add__ attribute // "+" operator
    """
    def __init__(self, string):
        self.string = string
    def __add__(self, word):
        return SuperStr(f"{self.string} {word}")

s = SuperStr("Bonjour")
print(s + "tout" + "le" + "monde")