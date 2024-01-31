
import tkinter as tk  #interface graphique
from tkinter import messagebox  
from tkinter import simpledialog  
import random  #valeurs aléatoires
import sys  
import time  #pause
import pickle 


def save_game(player, game_map):
    data = {
        'player': player,
        'game_map': game_map
    }

    with open('saved_game.pickle', 'wb') as file:
        pickle.dump(data, file)
    print("Partie sauvegardée avec succès.")




    
# Fonction pour simuler un effet de tappage au clavier
def typing_print(text):
    for char in text:  # Parcourir chaque caractère dans le texte , pour taper chaque cara l'un apres l'autre
        sys.stdout.write(char)  
        sys.stdout.flush()  
        time.sleep(0.01)  # pause entre chaque lettre , comme si on tappait le texte en temps reel au clavier
    print()  

# Fonction pour simuler une saisie avec effet de frappe
def typing_input(prompt):
    typing_print(prompt)  # Utiliser la fonction typing_print pour afficher l'invite
    return input()  #saisie de l'utilisateur

# Classe joueur 
class Player:
    def __init__(self, name):
        # Initialisation des attributs du joueur lors de la création d'une instance
        self.name = name  # Nom du joueur
        self.level = 1  # Niveau initial
        self.hp = 100  # Points de vie initiaux
        self.max_hp = 100  # Points de vie maximum
        self.base_attack = 10  # Attaque de base
        self.attack_bonus = 0  # Bonus d'attaque additionnel
        self.defense = 5  # Valeur de défense
        self.xp = 0  # Points d'expérience
        # Inventaire initial du joueur, avec des quantités pour chaque objet
        self.inventory = {"knife": 1, "healing potion": 5, "crossbow arm": 0}
        self.enemies_defeated = 0  # Nombre d'ennemis vaincus
        self.weapons = ["knife"]  # Liste des armes disponibles
        self.crossbow_equipped = False  # Indique si l'arbalète est équipée

    # Méthode pour afficher le statut du joueur
    def display_status(self):
        # Calcul de l'attaque totale
        total_attack = self.base_attack + self.attack_bonus
        # Affichage des informations du joueur
        typing_print(f"Nom: {self.name}, HP: {self.hp}/{self.max_hp}, Attaque: {total_attack}, Défense: {self.defense}")
        # Affichage de l'inventaire du joueur
        typing_print("Inventaire: " + ", ".join([f"{item}: {quantity}" for item, quantity in self.inventory.items()]))
        # Affichage des armes disponibles
        typing_print("Armes: " + ", ".join(self.weapons))

    # Méthode pour utiliser un objet de l'inventaire
    def use_item(self, item):
        # Vérification de la présence de l'objet dans l'inventaire
        if item in self.inventory and self.inventory[item] > 0:
            # Utilisation d'une potion de force
            if item == "strength potion":
                self.attack_bonus += 5  # Augmentation du bonus d'attaque
                self.inventory[item] -= 1  # Réduction de la quantité de l'objet
                typing_print(f"Vous avez utilisé une potion de force. Votre attaque augmente temporairement.")
            # Utilisation d'une potion de défense
            elif item == "defense potion":
                self.defense += 5  # Augmentation de la défense
                self.inventory[item] -= 1  # Réduction de la quantité de l'objet
                typing_print(f"Vous avez utilisé une potion de défense. Votre défense augmente temporairement.")
        else:
            # Message si l'objet n'est pas disponible
            typing_print(f"Pas de {item} disponible.")

    
    def heal(self): #systeme de soin du joueur 
        
        if self.inventory["healing potion"] > 0: # vérification de la disponibilité des potions de guérison
            
            self.hp = min(self.hp + 30, self.max_hp) #Soigner le joueur, sans dépasser le maximum de HP (max_hp)
            self.inventory["healing potion"] -= 1  # réduction de la quantité de potions
            typing_print(f"Vous avez utilisé une potion de guérison. HP actuel: {self.hp}/{self.max_hp}")
        else:
            
            typing_print("Pas de potions de guérison disponibles.")# message si aucune potion de guérison dispo , toute utiliser ou autre 

    # Méthode pour améliorer l'arme du joueur
    def upgrade_weapon(self, new_weapon):
       
        typing_print(f"Vous avez trouvé une arme: {new_weapon}. Voulez-vous l'équiper? (oui/non)") #demande au joueur s'il souhaite équiper la nouvelle arme
        choice = input().lower()  #saisie du choix du joueur
        if choice == "oui":
            self.weapons.append(new_weapon)  #ajout de la nouvelle arme à la liste
            self.attack_bonus += 5  #augmentation du bonus d'attaque car oui
            typing_print(f"Vous avez équipé {new_weapon}. Attaque totale: {self.base_attack + self.attack_bonus}")



class Enemy:
    def __init__(self, name, level, hp, attack, defense):
        self.name = name  #nom de l'ennemi
        self.level = level  #niveau de l'ennemi
        self.hp = hp  #points de vie de l'ennemi
        self.attack = attack  #attaque de l'ennemi
        self.defense = defense  #défense de l'ennemi

        

class GameMap:
    def __init__(self):
        self.locations = {
            (0, 0): "Départ",   #Point de spawn
            (1, 0): "Forêt dense",          # Guts ici (interaction arabalete)
            (0, 1): "Clairière", #ours
            (1, 1): "Rivière", #sorcier
            (2, 1): "Montagne", #geant 
            (2, 0): "Enderland",            # Boss ici (pour finir le jeu il faut le tuer)
            (3, 0): "Midland", #griffith
            (3, 1): "Pirate Bay", #Skull Knight
            (3, 2): "Royaume du Berserk", #Zodd Nosferatus
            (3, 3): "Fôret Noir",
            (0, 3): "Village Maudit",
            (1, 3): "Château des Ombres",
            (2, 3): "Cimetière",
            (3, 3): "Midgard",
            (1, 2): "Village mystérieux"    # PNJ ici (donne une information importante rien de plus)
        }
        self.enemies = {
            (1, 0): Enemy("Loup sauvage", 1, 30, 5, 2),
            (0, 1): Enemy("Ours furieux", 2, 40, 8, 3),
            (1, 1): Enemy("Sorcier mystérieux", 3, 50, 10, 4),
            (2, 1): Enemy("Géant de pierre", 4, 60, 12, 5),
            (3, 0): Enemy("Griffith", 4, 82, 15, 3),
            (3, 2) : Enemy("Zodd Nosferatus", 5, 54, 20, 4),
            (3, 1) : Enemy("Skull Knight", 5, 77, 25, 7),
            (2, 0): Enemy("Dragon ancestral", 5, 100, 25, 8)  # Boss
        }
        self.player_position = (0, 0)
        self.items_dropped = ["healing potion", "strength potion", "defense potion"] #heal que les ennemi peuvent lacher
        self.weapons_dropped = ["épée en fer", "hache de guerre", "lance", "arc enchanté", "Dragonslayer"] #loot que les ennemi peuvent faire récupérer aux joueurs a la suite de chaque combat
        self.guts_defeated = False   #tant que le joueur ne rencontre pas guts et ne decide pas de le tuer 
        self.defeated_enemies_locations = set()
    def move_player(self, player, direction):
        x, y = self.player_position

        # Position en focntion de la direction (points cardininaux est ouest nord sud)
        if direction == "east" and (x + 1, y) in self.locations:
            x += 1 #+1 pas vers l'est
        elif direction == "west" and (x - 1, y) in self.locations:
            x -= 1 #+1 pas vers l'ouest
        elif direction == "north" and (x, y - 1) in self.locations:
            y -= 1 #+1 pas vers le nord
        elif direction == "south" and (x, y + 1) in self.locations:
            y += 1 #+1 pas vers le sud
        else:
            typing_print("Vous ne pouvez pas aller dans cette direction.") #lorsque le joueur tente de se deplacer dans une position qui n'existe pas dans la map 
            return

        self.player_position = (x, y)
        typing_print(f"Vous êtes arrivé à {self.locations[(x, y)]}.") #pour qu'a chaque deplacement le joueur sache dans quel village ou royaume il se treouve ( en gros le lieu )

        # Interaction avec les PNJ ou Guts
        if (x, y) == (1, 2): #position du second pnj du jeu beaucoup moins important 
            interact_with_pnj(player)
        elif (x, y) == (1, 0) and not self.guts_defeated:#lorsque le joueur se retrouve sur cette position (il tombe dessus en allant une fois vers l'est des le debut du jeu au depart)
            interact_with_guts(player, self)

        # Gestion des combats contre les ennemis
        elif (x, y) in self.enemies and (x, y) not in self.defeated_enemies_locations:
            enemy = self.enemies[(x, y)]

            # Vérification pour combattre le boss et finir le jeu 
            if enemy.name == "Dragon ancestral" and player.enemies_defeated < 3: #il faut avoir battu minimum 3 ennemis sinon le combat ne sera pas possible
                typing_print("Vous n'êtes pas encore prêt à affronter le Dragon ancestral. Combattez plus d'ennemis pour gagner en force.") #message explicatif , suspens
            else:
                combat(player, enemy)
                if enemy.hp <= 0: #lorsque l'ennemi meurt
                    player.enemies_defeated += 1 #le nombre d'ennemi vaincu est incrementer de 1 grace au compteur
                    self.defeated_enemies_locations.add(self.player_position)

                    self.reward_player_after_battle(player, enemy) #loot
 
                    if enemy.name == "Dragon ancestral": #on s'assure que l'ennemi est bien le boss et non un ennemi lambda apres l'avoir vaincu
                        typing_print("Félicitations ! Vous avez vaincu le Dragon ancestral et sauvé le royaume !") #fin du jeu
                        typing_print("Appuyez sur fermez pour quitter...")
                        input()  # Attendre que l'utilisateur appuie sur une touche
                        sys.exit(0)  # Quitter le programme


        # Afficher le message si la position correspond à un ennemi vaincu
        elif (x, y) in self.defeated_enemies_locations: #si le joueur reviens sur la position d'un ennemi deja vaincu 
            self.display_defeated_enemy_message((x, y))


    def display_defeated_enemy_message(self, location): #un message personallisé appairaitra pour chaque ennemi vaincu pour rajouter de l'immersion 
        messages = {
            (1, 0): "Jadis, le Loup sauvage régnait sur cette forêt dense, jusqu'à ce qu'un héros le vainque.",
            (0, 1): "Cette clairière était autrefois le territoire d'un Ours furieux, maintenant terrassé par votre bravoure.",
            (1, 1): "Les murmures du Sorcier mystérieux résonnent encore près de la rivière, souvenir de votre affrontement.",
            (2, 1): "La Montagne se tient silencieuse, libérée de la présence menaçante du Géant de pierre.",
            (2, 0): "Enderland, où le Dragon ancestral a été défait, est désormais un lieu de paix.",
            (3,0): "Ici séjournais Griffith illustre chef de la brigade des Faucons..."
        }
        typing_print(messages.get(location, "Ce lieu semble calme. Il n'y a plus rien à y faire."))

    def reward_player_after_battle(self, player, enemy): #lorsque le joueur tue un ennemi
            if len(self.weapons_dropped) > 0:
                new_weapon = self.weapons_dropped.pop(0)
                player.upgrade_weapon(new_weapon) #systeme d'amelioration des armes , plus puissante apres chaque victoire



def equip_crossbow(player): #arbalete de guts 
    if player.inventory["crossbow arm"] > 0: #lorsque le joueur accepte de recuperer l'arbalete apres avoir tuer guts
        typing_print("Vous équipez l'arbalète. Voulez-vous l'utiliser en combat ? (oui/non)")
        choice = input().lower()
        if choice == "oui":
            player.crossbow_equipped = True #arbalete equipée 
            player.attack_bonus += 10  # l'attaque augmente 
            typing_print("Arbalète équipée. Votre attaque est maintenant plus puissante.")

def combat(player, enemy):
    typing_print(f"Un {enemy.name} apparaît ! Niveau: {enemy.level}") #pour chaque combat le nom de l'ennemi ainsi que son niveau 

    while player.hp > 0 and enemy.hp > 0: #tant que les deux entité sont vivantes , le joueur et son ennemi  , une replique apparait 
        enemy_dialogues = [
            f"{enemy.name} rugit de rage !",
            f"{enemy.name} : 'Tu ne peux pas me vaincre !'",
            f"{enemy.name} : 'Je vais te détruire !'",
            f"{enemy.name} : 'Tu vas regretter de m'avoir défié !'"
        ]
        typing_print(random.choice(enemy_dialogues)) #ces repliques sont aleatoire 
        player_choice = typing_input("Voulez-vous attaquer (a), guérir (g) ou fuir (f) ? ") #choix du joueur tout au long des combats de la partie

        if player_choice.lower() == 'a': #attaquer
            damage_to_enemy = max(player.base_attack + player.attack_bonus - enemy.defense, 0) #on prend l'attaque du joueur qu'on retire a la vie et defesne de l'ennemi
            enemy.hp -= damage_to_enemy #degat infliger
            typing_print(f"Vous infligez {damage_to_enemy} points de dégâts à {enemy.name}.")

            if enemy.hp <= 20 and player.crossbow_equipped: #lorsque l'ennemi est faible il est possible de l'achever a l'arbalete 
                typing_print("L'ennemi est faible. Voulez-vous faire un finish à l'arbalete (oui/non) ?")
                finish_choice = input().lower()
                if finish_choice == "oui":
                    enemy.hp = 0 #l'ennemi meurt directement dans le cas ou un finish a lieu 
                    typing_print("Vous utilisez votre arbalète pour un finish brutal !")
            if enemy.hp <= 0:
                typing_print(f"Vous avez vaincu {enemy.name}!") #lorsque l'ennemi meurt , petit message 
                break

        elif player_choice.lower() == 'g': #guerrir 
            player.heal()
        elif player_choice.lower() == 'f': #fuir 
            typing_print("Vous fuyez le combat.")
            break

        if enemy.hp > 0:
            damage_to_player = max(enemy.attack - player.defense, 0)
            player.hp -= damage_to_player
            typing_print(f"{enemy.name} inflige {damage_to_player} points de dégâts.")

            if player.hp <= 0: 
                typing_print("Vous avez été vaincu.") #mort du joueur 
                break



def interact_with_pnj(player): #le joueur rencontre le pnj et doit faire un choix , comme avec guts , cette interaction n'est pas crucial
    typing_print("Vous rencontrez Casca , une jeune femme...")
    choice = typing_input("1. Demander des conseils\n2. Demander ce qu'elle fait ici\n3. Ignorer et continuer votre chemin\nQue voulez-vous faire ? ")
    if choice == "1":
        typing_print("Le sage vous dit : 'Si vous êtes prêts pour affronter votre cauchemar, retournez au nord vers l'Enderland...Guts y est aller me laissant ici mais il n'est jamais revenu...'")
    elif choice == "2":
        typing_print("Je me battais au côté de Guts mais je me suis blesser , il m'as dit de l'attendre ici le temps qu'il revienne de sa bataille contre le Dragon de l'Enderland. Je sais qu'il va revenir tant qu'il ne sera pas de retour je ne bougerai pas d'ici , même si je dois mourrir ici je lui serai toujours  fidèle. ")
    elif choice == "3":
        typing_print("Vous continuez votre chemin, laissant Casca derrière vous.")

def interact_with_guts(player, game_map): #interaction cruciale , qui change le cours de jeu si le joueur fais le bon choix 
    print("Si tu ne marches qu'en regardant où tu mets les pieds, tu ne pourras jamais atteindre le but que tu t'es fixé")
    print("1. Demander qui il est")
    print("2. Le tuer")
    print("3. Ignorer et continuer votre chemin")
    choice = input("Que voulez-vous faire ? ")
    if choice == "1":
        print("Je suis Guts, un guerrier solitaire. Ma quête est guidée par la vengeance et le combat contre les ténèbres.")
    elif choice == "2":
        typing_print("Vous avez vaincu Guts et récupéré son bras arbalète !")
        player.inventory["crossbow arm"] = 1 #le joueur possede maintenant l'arbalete 
        equip_crossbow(player)
        game_map.guts_defeated = True #guts n'est plus la car mort 
    elif choice == "3":
        print("Vous continuez votre chemin, laissant Guts derrière vous.")




class GameApp:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("Menu")
        self.windows.geometry('1600x1600')
        self.windows.configure(bg="black")

        self.player_name = "Name"

        self.label = tk.Label(self.windows, text="Main Menu :", bg="orange", fg="black", width=50, height=10)
        self.label.pack()

        self.bouton1 = tk.Button(self.windows, text="1- Create a game", fg="black", width=35, height=7, command=self.create_game)
        self.bouton1.pack()
        self.bouton2 = tk.Button(self.windows, text="2- Load a game ", fg="black", width=30, height=7, command=self.load_game)
        self.bouton2.pack()
        self.bouton3 = tk.Button(self.windows, text="3- About", fg="black", width=23, height=7, command=self.windows_about)
        self.bouton3.pack()
        self.bouton4 = tk.Button(self.windows, text="4- Quit", fg="black", bg="red", width=20, height=7, command=self.exit_game)
        self.bouton4.pack()

    def exit_game(self):
        response = messagebox.askyesno("Quitter", "Êtes-vous sûr ?")
        if response is True:
            self.windows.destroy()

    def create_game(self):
        windows2 = tk.Toplevel(self.windows)
        windows2.title("Connexion")
        windows2.geometry('1000x800')
        windows2.configure(bg="black")
        
        name_var = tk.StringVar()
        name_label = tk.Label(windows2, text="Quel est votre nom?", font=(16), bg="black", fg="white")
        name_label.pack(pady=20)

        name_entry = tk.Entry(windows2, textvariable=name_var, font=(14))
        name_entry.pack(pady=20)

        submit_button = tk.Button(windows2, text="Commencer le jeu", command=lambda: self.on_close(name_var, windows2), font=(14), bg="orange")
        submit_button.pack()

        self.windows.withdraw()
        windows2.mainloop()

    def on_close(self, name_var, windows2):
        self.player_name = name_var.get()
        if self.player_name :
            windows2.destroy()
            self.start_game()

    def start_game(self):
        player = Player(self.player_name)
        game_map = GameMap()

        while player.hp > 0:

            player.display_status()
            direction = input("Où voulez-vous aller ? (east, west, north, south) ").lower()
            game_map.move_player(player, direction)
            if player.hp <= 0:
                print("Game Over")
                break
    
    def windows_game(self):
        if create_game :
            windows3 =tk.Toplevel()
            windows3.title("Game")
            windows3.geometry("1000x800")
            windows3.configure(bg="black")

    def load_game(self):
        file_path = simpledialog.askstring("Charger une partie", "Entrez le chemin du fichier de sauvegarde :")
        if file_path:
            try:
                with open(file_path, 'rb') as file:
                    saved_data = pickle.load(file)
                    self.start_loaded_game(saved_data)
            except FileNotFoundError:
                messagebox.showinfo("Erreur", "Fichier de sauvegarde non trouvé.")
            except Exception as e:
                messagebox.showinfo("Erreur", f"Erreur lors du chargement de la partie : {e}")
    
    def windows_about(self):
        windows_about = tk.Toplevel(self.windows)
        text = tk.Label(windows_about, text="Auteur : Yanis et Aymen")
        text.pack()

if __name__ == "__main__":
    windows = tk.Tk()
    app = GameApp(windows)
    windows.mainloop()
