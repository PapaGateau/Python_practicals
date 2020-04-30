class Voiture():
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur
    def __repr__(self):
        return "Votre voiture est une {} {} et coûte {}$".format(self.marque.capitalize(), self.couleur, self.prix)

# super_voiture = Voiture("lamborghini", 150000, "rouge")
# print(super_voiture)