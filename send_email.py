import smtplib, ssl


def send_email(massage):
    # Personal information need to secure:
    host = "smtp.gmail.com"
    port = 465
    mail = "appmailtester642@gmail.com"
    password = "rbai ysha quan rbfg"
    receiver = "appmailtester642@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(mail, password)
        server.sendmail(mail, receiver, massage)