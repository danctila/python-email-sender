import smtplib

def Send(adresses, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'myEmail@gmail.com'
    smtp_password = 'myEmailPassword'

    from_email = 'youremail@gmail.com'


    message = f'Subject: {subject}\n\n{body}'

    # initialize smtp server connection
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls() # secure server connection
        smtp.login(smtp_username, smtp_password) # login to gmail account
        for i in range(0, len(adresses)): # parse through email list and send message for each adress
             smtp.sendmail(from_email, adresses[i], message)