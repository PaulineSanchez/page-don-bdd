from flask import Flask, render_template, request, redirect, url_for, flash
    
import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page-principale-asso.html')

@app.route('/page-reglement-dons')
def reglement():
    return render_template('page-reglement-dons.html')


@app.route('/formulaire', methods=('GET', 'POST'))   
def formulaire():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        tel = request.form['tel']
        montant = request.form['montant']
        typetemps = request.form['typetemps']
        typemateriel = request.form['typemateriel']

        if not nom:
            flash('Le nom est requis!')
        elif not prenom:
            flash('Le prénom est requis!')
        elif not email:
            flash('Le mail est requis!')
        elif not tel:
            flash('Le téléphone est requis!')
        else:
            data.insert_don(nom, prenom, email, tel, montant, typetemps, typemateriel)
            return redirect(url_for('merci'))
    return render_template('formulaire.html')


@app.route('/page-merci')
def merci(): 
    sum = data.get_don()
    donnateurs = data.lire_posts()
    return render_template('page-merci.html', donnateurs=donnateurs, sum=sum)


if __name__ == "__main__":
    app.run(debug=True, port=5001)