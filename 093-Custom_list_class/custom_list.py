class CustomListe():
    """Custom list class with two characteristics:
    - Cannot append numbers
    - Cannot contain doubles
    """
    def __init__(self, *args):
        self.valeurs = [v for v in list(args) if not isinstance(v, int)]
        self.remove_duplicates()
    def append(self, value):
        if isinstance(value, int):
            print("Vous ne pouvez pas ajouter de nombres à la liste")
            return False
        if isinstance(value, str):
            self.valeurs.append(value)
        if isinstance(value, list):
            self.valeurs.extend(value)
        self.remove_duplicates()
    
    def remove_duplicates(self):
        self.valeurs = sorted(list(set(self.valeurs))) 

# ma_liste = CustomListe("Pierre", "Julien", "Marie", "Marie", 10)
# ma_liste.append(5)
# ma_liste.append("Pierre")
# print(ma_liste.valeurs)