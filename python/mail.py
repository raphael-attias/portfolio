import smtplib
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Déterminer le chemin
        if self.path == '/mail.py':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            name = data['name']
            email = data['email']
            message = data['message']

            # Envoyer l'e-mail
            smtp_server = "mail.infomaniak.com"  # Serveur SMTP de Gmail
            smtp_port = 587                   # Port pour TLS
            smtp_username = "rapatt@littlestorm.eu"  # Votre adresse e-mail
            smtp_password = "Ceyreste1383*@"     # Votre mot de passe

            # Créer le message
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = smtp_username  # Envoyer à votre adresse
            msg['Subject'] = "Nouveau message de contact"

            # Corps du message
            body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            try:
                # Se connecter au serveur SMTP et envoyer l'e-mail
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()  # Activer le cryptage TLS
                    server.login(smtp_username, smtp_password)  # Connexion
                    server.send_message(msg)  # Envoi de l'e-mail

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Message envoyé avec succès.'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': f'Échec de l\'envoi du message: {str(e)}'}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)  # Écouter sur le port 8000
    httpd = server_class(server_address, handler_class)
    print('Démarrage du serveur...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
