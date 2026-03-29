from flask import Flask,render_template,request,redirect,url_for
import utils
import afficher7SegmentCode as segment
from rpi_ws281x import PixelStrip,Color
import time
app = Flask(__name__)

# choix master COPIE
dicoMaster = {}

# variable globale

LED_PIN_MASTER = 18
LED_PIN_PLAYER = 21
LED_COUNT = 4
strip_master = PixelStrip(LED_COUNT, LED_PIN_MASTER)
strip_master.begin()
strip_player = PixelStrip(LED_COUNT, LED_PIN_PLAYER)
strip_player.begin()

for i in range(LED_COUNT):
    wait = 50

    strip_master.setPixelColor(i, Color(255,255,255))
    strip_player.setPixelColor(i, Color(255,255,255))
    strip_master.show()
    strip_player.show()
    time.sleep(wait / 100.0)

# liste to RGB
# site utiliser pour la conversion colorNAME TO RGB  --> https://products.aspose.app/svg/color-converter/name-to-rgb
dicoRGB = {
    'rouge':(255, 0, 0),
    'bleu':(0, 0, 255),
    'orange':(255, 165, 0),
    'rose':(255, 138, 221),
    'bleu-clair':(100, 185, 249),
    'vert':(0, 128, 0),
    'jaune':(255, 255, 0),
    'blanc':(255, 255, 255)

}
# décomposition TUPLE TO VALEUR R,G,B que la méthode Color attend

# couleurs choisit
@app.route('/')
def menuGame():
   return render_template('menuGame.html')

@app.route('/master', methods=['GET','POST'])
def master():
    global dicoMaster # pour que par la suite on puissent faire des comparaison avec le choix du player
    
    if request.method == 'POST':
        # Récupération des données du formulaire

        dico = {
            'led1': dicoRGB[request.form.get('led1')], # conversion nom de la couleur en valeur RGB :)
            'led2': dicoRGB[request.form.get('led2')],
            'led3': dicoRGB[request.form.get('led3')],
            'led4': dicoRGB[request.form.get('led4')]
        }
        # copie du choix master

        dicoMaster = dico.copy()
        # ------------------------------------------------------
        # EN COURS DE DEVELOPPEMENT !
        # partie LEDS -> allumage des LEDS côtés MASTER

        
        numLed = 0 # numéro de la led -> ex. led1->0,led2->1 etc....
        for clef in dicoMaster:
        #       #décomposition de la led RGB (tuple)
             R,G,B = dicoMaster[clef]
             strip_master.setPixelColor(numLed,Color(R,G,B))
             strip_master.show()
             numLed+=1 # incrémentation pour passer à la led suivante
        # ------------------------------------------------------

        print("Données reçus:", dico) # print de debug

        #return redirect('reponse')
        return redirect('player')

    return render_template('master.html')

@app.route('/player', methods=['GET', 'POST'])
def player():
    bien_places = 0
    mal_places = 0
    if request.method == 'POST':
        # Récupération des données du formulaire et conversion des couleurs en RGB
        dicoPlayer = {
            'led1': dicoRGB[request.form.get('led1')],
            'led2': dicoRGB[request.form.get('led2')],
            'led3': dicoRGB[request.form.get('led3')],
            'led4': dicoRGB[request.form.get('led4')]
        }

        print("Données reçues:", dicoPlayer)  # Debug
        print("Choix maître:", dicoMaster)

        # Comparaison des leds du joueur avec celles du MASTER MON GARS
        bien_places, mal_places = utils.comparer(dicoMaster, dicoPlayer)

        print("LEDs bien placées:", bien_places)
        print("LEDs mal placées:", mal_places)

        segment.affichageScore(bien_places, mal_places)
        numLed = 0 # numéro de la led -> ex. led1->0,led2->1 etc....
        for clef in dicoPlayer:
        #       #décomposition de la led RGB (tuple)
             R,G,B = dicoPlayer[clef]
             strip_player.setPixelColor(numLed,Color(R,G,B))
             strip_player.show()
             numLed+=1 # incrémentation pour passer à la led suivante
        # Si toutes les leds sont bien placer on redirige vers la page 'reponse'

        if bien_places == 4:
            return redirect('reponse')

    return render_template('player.html')

@app.route('/reponse')
def reponse():
    # page manipuler via du js pour afficher les data
    return render_template('reponse.html')

# pour le mode debug automatique
if(__name__ == "__main__"):
    app.run(debug=True)