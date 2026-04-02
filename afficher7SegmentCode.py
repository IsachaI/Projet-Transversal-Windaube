import time
import tm1637

# Initialisation de la CONNEXIONNN
display = tm1637.TM1637(clk=16, dio=26)


def startJeu():
    """
    Fonction de bienvenue
    """
    display.scroll("MasterDaube", delay=0.3)
    time.sleep(1)
    # Message de la fin YOUPIII
    display.scroll("Fait par Mehdi Sacha Val et Louis", delay=0.3)
    time.sleep(1)
    display.scroll("Le jeu va commencer dans")
    display.show("3")
    time.sleep(0.5)
    display.show("2")
    time.sleep(0.5)
    display.show("1")
    time.sleep(0.5)
    display.show("0")
    time.sleep(0.5)

def affichageScore(bien_places,mal_places):
    display.show(str(bien_places)+'-'+str(mal_places))