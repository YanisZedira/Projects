from magicien import *
from roi_sorcier import *
from combat import *


if __name__ == "__main__":
    magicien = Magicien("Gandalf")
    roi_sorcier = RoiSorcier("Le Roi-Sorcier d'Angmar")

    combat = Combat()
    combat.demarrer_combat(magicien, roi_sorcier)
