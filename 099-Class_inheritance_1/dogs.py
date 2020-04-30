"""
For class inheritance its important not to forget calling the parent class __init__ method
we can do this using super(). or the class name itself
"""
class Chien(object):
    def __init__(self, race):
        self.race = race

    @property
    def taille(self):
        return 100

class Chihuahua(Chien):
    def __init__(self, nom):
        super().__init__("Chihuahua")
        # Chien.__init__("Chihuahua")
        self.nom = nom

# chien = Chihuahua("Lily")
# print(chien.race)
	