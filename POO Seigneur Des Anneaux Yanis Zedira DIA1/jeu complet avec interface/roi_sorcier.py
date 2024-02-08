from personnage import *
import random
#YANIS ZEDIRA DIA1

class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20
    FORCE_FRAPPE_3 = 25

    def __init__(self, nom):
        super().__init__(nom)

    def frappe_avec_son_epee(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_1 + self.get_experience(), "Frappe avec son épée"
        )

    def attaque_avec_son_nazgul(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_2 + self.get_experience(), "Attaque avec son Nazgûl"
        )

    def invoque_un_troll(self, adversaire):
        self.frappe(
            adversaire, self.FORCE_FRAPPE_3 + self.get_experience(), "Invocation de Troll"
        )

    def attaque(self, adversaire):
        attaque_type = random.randint(1, 3)
        if attaque_type == 1:
            self.frappe_avec_son_epee(adversaire)
        elif attaque_type == 2:
            self.attaque_avec_son_nazgul(adversaire)
        else:
            self.invoque_un_troll(adversaire)