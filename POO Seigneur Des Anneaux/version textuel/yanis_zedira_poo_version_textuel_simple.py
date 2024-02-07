#Voici la version textuel simple du projet POO Seigneur des Anneaux.
#La version avec interface graphique est aussi présente dans le dossier du jeu.

import random
import time

class Personnage:
    def __init__(self, nom):
        self.__nom = nom
        self.__vie = 100
        self.__force = 0
        self.__experience = 0
        self.__degats = 0
        self.__tour = 'joueur1'
        self.__phrases_combat = [
            "L'attaque est imminente !",
            "La bataille fait rage !",
            "Un coup critique !",
            "Une attaque dévastatrice !",
            "Les sorciers s'affrontent !",
            "La magie est déchaînée !",
            "Les sorts fusent de toutes parts !",
            "Une contre-attaque fulgurante !",
            "Le duel continue !",
        ]

    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        self.__vie = vie

    def get_force(self):
        return self.__force

    def set_force(self, force):
        self.__force = force

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_degats(self):
        return self.__degats

    def set_degats(self, degats):
        self.__degats = degats

    def get_tour(self):
        return self.__tour

    def frappe(self, cible, force_frappe, nom_attaque):
        cible.recoit_degat(self, force_frappe, nom_attaque)

    def esquive(self):
        esquive_chance = random.randint(1, 10)  # 10% de chance d'esquiver
        return esquive_chance == 7

    def recoit_degat(self, adversaire, force_frappe, nom_attaque):
        if not self.esquive():
            self.set_degats(self.get_degats() + force_frappe)
            self.set_vie(self.get_vie() - force_frappe)
            self.set_experience(self.get_experience() + 1)
            print(
                f"{self.__nom} subit {force_frappe} dégâts de {adversaire.get_nom()} à cause de l'attaque '{nom_attaque}'. "
                f"Il lui reste {self.get_vie()} points de vie."
            )
        else:
            print(f"{self.__nom} esquive l'attaque de {adversaire.get_nom()} !")

    def commentaire_combat(self):
        return random.choice(self.__phrases_combat)


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


class Combat:
    def demarrer_combat(self, magicien, roi_sorcier):
        print("Le combat commence !")
        time.sleep(1)
        print(
            f"Le Magicien {magicien.get_nom()} se prépare à affronter le redoutable Roi-Sorcier {roi_sorcier.get_nom()} !"
        )
        time.sleep(2)
        while magicien.get_vie() > 0 and roi_sorcier.get_vie() > 0:
            if magicien.get_tour() == 'joueur1':
                print("Tour de Gandalf...")
                time.sleep(1)
                magicien.attaque(roi_sorcier)
                magicien._Personnage__tour = 'joueur2'
            else:
                print("Tour du Roi-Sorcier d'Angmar...")
                time.sleep(1)
                roi_sorcier.attaque(magicien)
                magicien._Personnage__tour = 'joueur1'

            print(magicien.commentaire_combat())  # Commentaire aléatoire sur le combat
            print()  # Ligne vide pour séparer les tours

        if magicien.get_vie() > 0:
            print(
                f"{magicien.get_nom()} a triomphé du maléfique {roi_sorcier.get_nom()} !"
            )
            vainqueur = "Magicien"
        else:
            print(
                f"{roi_sorcier.get_nom()} a vaincu le puissant {magicien.get_nom()} !"
            )
            vainqueur = "Roi-Sorcier d'Angmar"

        print(f"Le vainqueur est : {vainqueur}")


if __name__ == "__main__":
    magicien = Magicien("Gandalf")
    roi_sorcier = RoiSorcier("Le Roi-Sorcier d'Angmar")

    combat = Combat()
    combat.demarrer_combat(magicien, roi_sorcier)
