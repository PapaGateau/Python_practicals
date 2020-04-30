class Voiture(object):
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur
        
    @classmethod
    def lamborghini(cls):
        return cls("Lamborghini", 150000, "rouge")
        
    @property
    def prix_euros(self):
        return int(self.prix * 1.5)

lamborghini = Voiture.lamborghini()
print(lamborghini.prix)
print(lamborghini.prix_euros)