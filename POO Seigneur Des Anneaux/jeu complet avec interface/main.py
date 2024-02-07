from synopsis import *
from magicien import *
from roi_sorcier import *
from combat import *

if __name__ == "__main__":
    synopsis_window = Synopsis()
    synopsis_window.mainloop()

    magicien = Magicien("Gandalf")
    roi_sorcier = RoiSorcier("Le Roi-Sorcier d'Angmar")

    combat = Combat()
    combat.demarrer_combat(magicien, roi_sorcier)
