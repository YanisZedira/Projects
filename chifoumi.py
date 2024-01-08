
import random
def chifoumi():
  recommencer = "oui"


  while recommencer == "oui" :
    X = input("pierre, papier ou ciseau ?")
    C = ["pierre", "papier", "ciseau"]
    resultat_final = random.choice(C)
    print("J'ai choisit" ,resultat_final)

    if (X == "pierre" and resultat_final == "papier") or \
       (X == "papier" and resultat_final == "ciseau") or \
       (X == "ciseau" and resultat_final == "pierre") :
        print("perdu")
    if (X == "ciseau" and resultat_final == "papier") or \
       (X == "papier" and resultat_final == "pierre") or \
       (X == "pierre" and resultat_final == "ciseau") :
        print("gagné")
    if X == resultat_final :
      print("Match nul")
          
    recommencer = input("Voulez vous recommencer ?" )
    
chifoumi()