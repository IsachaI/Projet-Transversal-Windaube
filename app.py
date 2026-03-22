from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

# liste des choix
choixMaster = []
choixPlayer = []

# couleurs choisit
@app.route('/')
def menuGame():
   return render_template('menuGame.html')

@app.route('/master', methods=['GET','POST'])
def master():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        dictio = {
            'led1': request.form.get('led1'),
            'led2': request.form.get('led2'),
            'led3': request.form.get('led3'),
            'led4': request.form.get('led4')
        }

        print("Données reçus:", dictio)

        return redirect('player')

    return render_template('master.html')

@app.route('/player')
def player():
    return render_template('player.html')

# pour le mode debug automatique
if(__name__ == "__main__"):
    app.run(debug=True)