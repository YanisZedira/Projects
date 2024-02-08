import tkinter as tk
from PIL import Image, ImageTk
import time
#YANIS ZEDIRA DIA1


class FinCombat(tk.Toplevel):
    def __init__(self, vainqueur):
        super().__init__()
        self.title("Fin du combat")
        self.attributes('-fullscreen', True)

        if vainqueur == "Magicien":
            image_path = r"jeu complet avec interface/magicien.jpg"
            texte = "Le Magicien a triomphé du maléfique Roi-Sorcier d'Angmar !"
        else:
            image_path = r"jeu complet avec interface/sorcier.webp"
            texte = "Le Roi-Sorcier d'Angmar a vaincu le puissant Magicien Gandalf !"

        image = Image.open(image_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.pack()

        self.label_texte = tk.Label(self, text="", font=("Arial", 20))
        self.label_texte.pack()

        self.afficher_texte(texte)

    def afficher_texte(self, texte):
        for char in texte:
            self.label_texte.config(
                text=self.label_texte.cget("text") + char
            )
            self.update()
            time.sleep(0.1)
