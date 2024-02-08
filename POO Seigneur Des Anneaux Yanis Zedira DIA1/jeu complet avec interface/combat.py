import random
import time
import tkinter as tk
from PIL import Image, ImageTk
from fin_combat import FinCombat
#YANIS ZEDIRA DIA1

class Combat:
    def demarrer_combat(self, magicien, roi_sorcier):
        print("Le combat commence !")
        time.sleep(1)
        print(
            f"Le Magicien {magicien.get_nom()} se prépare à affronter le redoutable Roi-Sorcier {roi_sorcier.get_nom()} !"
        )
        time.sleep(2)
        
        # Début du combat
        while magicien.get_vie() > 0 and roi_sorcier.get_vie() > 0:
            print("Tour de Gandalf...")
            time.sleep(1)
            magicien.attaque(roi_sorcier)
            print(magicien.commentaire_combat())  # Commentaire aléatoire sur le combat
            print()  # Ligne vide pour séparer les tours
            
            # Vérifie si le Roi-Sorcier est encore en vie après l'attaque du Magicien
            if roi_sorcier.get_vie() <= 0:
                break  # Sort de la boucle si le Roi-Sorcier est vaincu
            
            print("Tour du Roi-Sorcier d'Angmar...")
            time.sleep(1)
            roi_sorcier.attaque(magicien)
            print(magicien.commentaire_combat())  # Commentaire aléatoire sur le combat
            print()  # Ligne vide pour séparer les tours
            
            # Vérifie si le Magicien est encore en vie après l'attaque du Roi-Sorcier
            if magicien.get_vie() <= 0:
                break  # Sort de la boucle si le Magicien est vaincu
        
        # Fin du combat
        if magicien.get_vie() > 0:
            print(f"{magicien.get_nom()} a triomphé du maléfique {roi_sorcier.get_nom()} !")
            vainqueur = "Magicien"
        else:
            print(f"{roi_sorcier.get_nom()} a vaincu le puissant {magicien.get_nom()} !")
            vainqueur = "Roi-Sorcier d'Angmar"

        fenetre_fin_combat = FinCombat(vainqueur)
        fenetre_fin_combat.mainloop()
