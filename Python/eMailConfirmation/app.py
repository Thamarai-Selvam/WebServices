import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
password = "meliodas1063000"

def sendMailtoRecipient(senderMail = "meliodastheman106@gmail.com", receiverMail = "sthamarai001@gmail.com"):
    subject = "Test eMail"
    body = "This is test email"
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = senderMail
    email["To"] = receiverMail 
    email["Subject"] = subject
    # Add body and attachment to email
    email.attach(MIMEText(body, "plain"))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(senderMail, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(senderMail, receiverMail, text)
    session.quit()
    print('Mail Sent')

