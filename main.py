from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets
from flask_login import login_user, login_required
from flask_login import current_user, UserMixin
from flask_login import LoginManager

import os

port = int(os.environ.get("PORT", 5000))


app = Flask(__name__)
app.secret_key = 'jhbviug75765drtxzbiu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.Integer, default=False, nullable=False)
    is_confirmed = db.Column(db.Boolean, default=False)

    def is_active(self):
        """Return True if the user is active, else False."""
        return self.is_active
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

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
    if user is not None and check_password_hash(user.password_hash, password):
        login_user(user)
        return redirect(url_for('dashboard'))
    flash('Invalid username or password.')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
     user = current_user
     return render_template('dashboard.html',user=current_user)

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
    # Adresse e-mail de l'expéditeur et mot de passe
    EMAIL_ADDRESS = "loicstrauch123@gmail.com"
    EMAIL_PASSWORD = "vouelukgzkutyvji"
    # Adresse e-mail du destinataire
    to_email = email
    user = User.query.filter_by(email=email).first()
    # Sujet et corps du message
    subject = 'Confirmation d\'inscription'
    body = f'Cliquez sur ce lien pour activer votre compte : http://127.0.0.1:5000/confirmation/{user.username}/{user.token}'
    # Créer un message multipart et ajouter le sujet et le corps du message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
# Se connecter au serveur SMTP et envoyer le message
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    return render_template('verifiermail.html')

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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=port)
