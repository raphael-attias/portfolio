from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les informations SMTP depuis les variables d'environnement
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

app = Flask(__name__)

@app.route('/envoyer-mail', methods=['POST'])
def envoyer_mail():
    try:
        # Récupérer les données du formulaire en JSON
        data = request.get_json()
        nom = data['nom']
        email = data['email']
        sujet = data['sujet']
        message = data['message']

        # Configuration de l'email
        destinataire = SMTP_USER  # Adresse e-mail du destinataire, ici votre adresse

        # Créer le message email
        msg = MIMEMultipart()
        msg['From'] = f"{nom} <{SMTP_USER}>"  # L'expéditeur est vous-même, mais avec le nom de l'utilisateur
        msg['To'] = destinataire
        msg['Subject'] = sujet
        msg['Reply-To'] = email  # Ajouter l'adresse de l'utilisateur dans le champ "Reply-To"

        # Contenu du message
        body = f"Nom: {nom}\nEmail: {email}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Connexion au serveur SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SMTP_USER, destinataire, text)
        server.quit()

        return jsonify({"message": "Merci, votre message a été envoyé avec succès !"})

    except Exception as e:
        print(e)
        return jsonify({"message": "Erreur lors de l'envoi du message."}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
