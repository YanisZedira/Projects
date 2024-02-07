import random


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
        esquive_chance = random.randint(1, 10)  #chance d'esquiver
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
