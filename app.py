from flask import Flask,render_template,request,redirect,url_for
from rpi_ws281x import PixelStrip,Color

app = Flask(__name__)

# choix master COPIE
choixMaster = {}


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
    global choixMaster # pour que par la suite on puissent faire des comparaison avec le choix du player
    if request.method == 'POST':
        # Récupération des données du formulaire

        dico = {
            'led1': dicoRGB[request.form.get('led1')], # conversion nom de la couleur en valeur RGB :)
            'led2': dicoRGB[request.form.get('led2')],
            'led3': dicoRGB[request.form.get('led3')],
            'led4': dicoRGB[request.form.get('led4')]
        }
        # copie du choix master

        choixMaster = dico.copy()
        # ------------------------------------------------------
        # EN COURS DE DEVELOPPEMENT !
        # partie LEDS -> allumage des LEDS côtés MASTER

        # from rpi_ws281x import PixelStrip,Color
        LED_COUNT = 4
        LED_PIN = 18
        strip = PixelStrip(LED_COUNT,LED_PIN)
        strip.begin()
        numLed = 0 # numéro de la led -> ex. led1->0,led2->1 etc....
        for clef in dico:
        #       #décomposition de la led RGB (tuple)
             R,G,B = dico[clef]
             strip.setPixelColor(numLed,Color(R,G,B))
             strip.show()
             numLed+=1 # incrémentation pour passer à la led suivante
        # ------------------------------------------------------

        print("Données reçus:", dico) # print de debug

        #return redirect('reponse')
        return redirect('player')

    return render_template('master.html')

@app.route('/player')
def player():
    return render_template('player.html')

# route pour nos futur session
#@app.route('/reponse')
#def reponse():
#    return render_template('reponse.html')

# pour le mode debug automatique
if(__name__ == "__main__"):
    app.run(debug=True)
