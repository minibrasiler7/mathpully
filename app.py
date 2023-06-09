import copy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import login_user, login_required
from flask_login import current_user, UserMixin
from flask_login import LoginManager
from flask_mail import Mail, Message
import os
import sujet
import points
import calcullittéralbrain
from datetime import datetime
import method

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
app.secret_key = 'jhbviug75765drtxzbiu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER']='smtp-relay.sendinblue.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'loic_strauch_19@msn.com'
app.config['MAIL_PASSWORD'] = 'aPN85AhBSbWzxmY0'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.Integer, default=False, nullable=False)
    is_confirmed = db.Column(db.Boolean, default=False)
    personnalisation = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(50), nullable = True)
    points = db.Column(db.Integer, default=0)
    exercises = db.relationship('Exercise', backref='user', lazy='dynamic')
class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(128), nullable=True)
    exercise_name = db.Column(db.String(128))
    exercise_nom = db.Column(db.String(128), nullable=True)
    is_completed = db.Column(db.Boolean)
    completed_at = db.Column(db.DateTime, nullable=True)
    # Clé étrangère vers l'utilisateur
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def is_active(self):
        """Return True if the user is active, else False."""
        return self.is_active
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User,(int(user_id)))

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user is not None and check_password_hash(user.password_hash, password) :
        login_user(user)
        if user.personnalisation:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('personnalisation', user=current_user))
    flash('Invalid username or password.')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
     badge_user = Exercise.query.filter_by(user_id=current_user.id, is_completed=1).order_by(Exercise.completed_at.desc()).limit(5).all()
     return render_template('dashboard.html',user=current_user, badges= badge_user)

@app.route('/personnalisation', methods=["GET","POST"])
@login_required
def personnalisation():
    if request.method == 'POST':
        selected_avatar = request.form['avatar']
        user = User.query.get(current_user.id)
        user.avatar = selected_avatar
        user.personnalisation = True
        db.session.commit()
        try:

            for i in range(len(charger_nom_badge())):
                new_exercise = Exercise(exercise_name=charger_nom_badge()[i], is_completed=False, user=current_user)
                db.session.add(new_exercise)
            db.session.commit()
        except Exception as e:
            print("An error occurred while adding exercises:", e)
        return render_template('dashboard.html', user=user)

    images =['avatar1.png', 'avatar2.png', 'avatar3.png']
    return render_template('personnaliser-utilisateur.html', user=current_user, images = images)


@login_required
@app.route('/chapitre')
def chapitre():
    nom_chapitre = request.args.get('nom_chapitre')
    sujet_selectionne = getattr(sujet, f"_{nom_chapitre}")

    dic_point=[]

    for souschapitre in sujet_selectionne['points']:
        souschapitre = souschapitre.replace(" ", "_")
        souschapitre = souschapitre.replace("'", "_")
        copie_souschapitre = copy.deepcopy(getattr(points, souschapitre))
        dic_point.append(copie_souschapitre)


    for i in range(len(dic_point)):
        nom_fonction = dic_point[i]["questions"]
        if hasattr(calcullittéralbrain, nom_fonction):
            questions = [getattr(calcullittéralbrain, nom_fonction)(), getattr(calcullittéralbrain, nom_fonction)(), getattr(calcullittéralbrain, nom_fonction)(), getattr(calcullittéralbrain, nom_fonction)()]
            dic_point[i]["questions"] = questions
        else:
            print("no function")
    badge_user = Exercise.query.filter_by(user_id=current_user.id).all()
    # Code pour récupérer les données du chapitre correspondant à nom_chapitre depuis la base de données
    return render_template(f"{nom_chapitre}.html", chapitre=sujet_selectionne, souschapitre=dic_point, user=current_user, badge_user = badge_user)

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        password_hash = generate_password_hash(method="pbkdf2:sha256", salt_length=8, password=password)
        token =  secrets.token_hex(32)
        user = User(username=username, password_hash=password_hash, email=email, token = token)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('verifier_mail', email=email))
    else:
        return render_template('inscription.html')

@app.route('/verifier_mail/<email>')
def verifier_mail(email):

    user = User.query.filter_by(email=email).first()
    # Sujet et corps du message
    mail = Mail(app)
    subject = 'Confirmation d\'inscription'
    body = f'Cliquez sur ce lien pour activer votre compte : http://127.0.0.1:5000/confirmation/{user.username}/{user.token}'
    # Créer un message multipart et ajouter le sujet et le corps du message

    msg = Message('Votre confirmation', sender = 'loic_strauch_19@msn.com', recipients=[email])
    msg.body=body
    mail.send(msg)
    return render_template('verifiermail.html')


@app.route('/update_score', methods=['POST'])
def update_score():
    user = current_user
    user.points += 10
    db.session.commit()
    response = {
        'message': 'Score updated successfully',
        'new_score': user.points  # Remplacez cette valeur par le nouveau score de l'utilisateur.
    }

    # Utilisez jsonify pour renvoyer la réponse JSON.
    return jsonify(response)

@app.route('/confirmation/<username>/<token>')
def confirmation(username, token):
    # Vérifier si l'utilisateur existe dans la base de données et que le token est valide
    user = User.query.filter_by(username=username, token=token, is_confirmed=0).first()

    if user:
        # Mettre à jour le champ confirmed de l'utilisateur à True
        user.is_confirmed= True
        db.session.commit()

        # Afficher un message de confirmation
        flash('Votre inscription a été confirmée avec succès!', 'success')
        return redirect(url_for('index'))

    # Si l'utilisateur n'existe pas ou que le token est invalide, afficher un message d'erreur
    flash('Le lien de confirmation est invalide ou a expiré.', 'error')
    return redirect(url_for('index'))

@app.route('/update_exercise', methods=['POST'])
def update_exercise():
    data = request.get_json()
    exercise_name = data.get('exercise_name')
    user_id = current_user.id

    # Trouver l'exercice pour l'utilisateur actuel
    exercise = Exercise.query.filter_by(exercise_name=exercise_name, user_id=user_id).first()
    all_dicts = [attr for attr in dir(points) if isinstance(getattr(points, attr), dict)]

# Recherchez parmi ces dictionnaires celui qui a la valeur exercise_name pour la clé "name"
    for d in all_dicts:
        dict_obj = getattr(points, d)
        if dict_obj.get("name") == exercise_name:
            dic_exercice = dict_obj
            break


    if exercise:
        exercise.is_completed = 1
        exercise.exercise_nom = dic_exercice['nom']
        exercise.image_name = dic_exercice['badge']
        exercise.completed_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Exercise updated successfully"}), 200

    else:
        return jsonify({"message": "Exercise not found"}), 404



def charger_nom_badge():
    liste_name_sous_chapitre =[]
    for nom_variable in dir(points):
    # Obtenez l'objet associé au nom de variable
        variable = getattr(points, nom_variable)
    # Vérifiez si la variable est un dictionnaire
        if isinstance(variable, dict):
            # Vérifiez si la clé "name" existe dans le dictionnaire
            if "name" in variable:
                # Ajoutez la valeur de la clé "name" à la liste des noms
                liste_name_sous_chapitre.append(variable["name"])
    return liste_name_sous_chapitre

@app.route('/methodpython', methods=['POST'])
def methodpython():
    methode = request.form.get('method')
    userAnswer = request.form.get('userAnswer')
    fonction = method.METHOD.get(methode)
    reponse = fonction(userAnswer)
    # Vous pouvez écrire ici votre logique basée sur 'method' et 'userAnswer'
    # Pour cet exemple, nous renvoyons simplement la valeur 2
    return jsonify({'value': reponse})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=port)
