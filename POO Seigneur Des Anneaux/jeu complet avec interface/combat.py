import random
import time
import tkinter as tk
from PIL import Image, ImageTk
from fin_combat import FinCombat

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

        fenetre_fin_combat = FinCombat(vainqueur)
        fenetre_fin_combat.mainloop()

