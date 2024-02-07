import random
from personnage import Personnage

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15
    FORCE_FRAPPE_3 = 20

    def __init__(self, nom):
        super().__init__(nom)

    def lance_un_sort(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_1 + self.get_experience(), "Sort de Feu"
        )

    def lance_un_rayon_de_lumiere_sombre(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_2 + self.get_experience(), "Rayon de Lumière Sombre"
        )

    def invoque_un_dragon(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_3 + self.get_experience(), "Invocation de Dragon"
        )

    def attaque(self, adversaire):
        attaque_type = random.randint(1, 3)
        if attaque_type == 1:
            self.lance_un_sort(adversaire)
        elif attaque_type == 2:
            self.lance_un_rayon_de_lumiere_sombre(adversaire)
        else:
            self.invoque_un_dragon(adversaire)
