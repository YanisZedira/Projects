import time
import tkinter as tk
import keyboard
#YANIS ZEDIRA DIA1


class Synopsis(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Synopsis")
        self.attributes('-fullscreen', True)

        self.synopsis_label = tk.Label(
            self, text="", font=("Arial", 20), justify="left"
        )
        self.synopsis_label.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)

        synopsis_text = """
        Il était une fois, dans un monde lointain, deux puissants sorciers se livrant une lutte sans 
        merci pour la domination de la terre magique.
        Le premier, le sage et puissant Gandalf, maître des arts mystiques, luttant pour la paix et 
        la justice dans le royaume.Le second, le sombre et maléfique Roi-Sorcier d'Angmar, 
        cherchant  à répandre le chaos et la terreur pour asseoir son règne de terreur.
        Depuis des siècles, ces deux êtres se sont affrontés maintes et maintes fois, mais aucun 
        ne parvenait à prendre le dessus sur l'autre.

        Et aujourd'hui, ils se retrouvent une fois de plus sur le champ de bataille, prêts à s'affronter 
        dans l'ultime bataille où un seul des deux sorciers sortira victorieux, tandis que l'autre 
        sera condamné à la défaite éternelle.
        """

        self.afficher_synopsis(synopsis_text)

    def afficher_synopsis(self, texte):
        for char in texte:
            if char == "\n":
                self.synopsis_label.config(
                    text=self.synopsis_label.cget("text") + "\n"
                )
            else:
                self.synopsis_label.config(
                    text=self.synopsis_label.cget("text") + char
                )
                self.update()
                time.sleep(0.03)
                # Détecter si la touche Espace est pressée pour passer directement au combat
                if keyboard.is_pressed('space'):
                    break
        # Fermer la fenêtre après l'affichage complet du synopsis
        self.after(100, self.destroy)  # Ferme la fenêtre après 3 secondes (3000 millisecondes)
