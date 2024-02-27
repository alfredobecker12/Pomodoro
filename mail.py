import smtplib
from sql_operations import get_email


server_smtp = 'smtp.gmail.com'
smtp_mail = 'pomodoroltda@gmail.com'
smtp_app_password = 'zejyzctrrwnyxaig'
smtp_port = 587
subject = 'Esqueceu sua senha?\n\n'
body = 'Verificamos que você esqueceu a senha. Bom, é uma pena, pois não temos a funcionalidade concluída ainda. Passar bem.'
message = {subject}, {body}


def send_mail(username):
    user_mail = get_email(username)

    with smtplib.SMTP(server_smtp, smtp_port) as smtp:
        smtp.starttls() # Coloca a conexão em modo TLS (o servidor utilizado deve suportar tal criptografia)
        smtp.login(smtp_mail, smtp_app_password) # Realiza o login no server SMTP que, nesse caso, é o gmail
        print('Comecei a enviar')
        smtp.sendmail(smtp_mail, user_mail, message)

    return

if __name__ == '__main__':
    send_mail('windowsvista')
    print('enviou')
    