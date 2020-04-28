import string

class SuperChaine(object):
    """this class illustrates how to use methods by naming them differently

    Args:
        object ([str])
    """
    def __init__(self, string):
        self.string = string
    def majuscule(self):
        return self.string.upper()
    def minuscule(self):
        return self.string.lower()
    def titre(self):
        return self.string.title()
        

# chaine = SuperChaine("UdeMy")
# print(chaine.majuscule())
# print(chaine.minuscule())
# print(chaine.titre())