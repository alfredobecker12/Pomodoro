import smtplib
from sql_operations import get_email
from mail import *


server_smtp = 'smtp.gmail.com'
smtp_port = 587
subject = 'Esqueceu sua senha?\n\n'
body = 'Esse é apenas um email teste. Ninguém mandou esquecer a senhar, bundão.'
message = subject+body


def send_mail(username):
    user_mail = get_email(username)

    with smtplib.SMTP(server_smtp, smtp_port) as smtp:
        smtp.starttls() # Coloca a conexão em modo TLS (o servidor utilizado deve suportar tal criptografia)
        smtp.login(smtp_mail, smtp_app_password) # Realiza o login no server SMTP que, nesse caso, é o gmail
        smtp.sendmail(smtp_mail, user_mail, message)


if __name__ == '__main__':
    pass
    
