import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMailtoRecipient(senderMail, receiverMail):
    subject = "Test eMail"
    body = "This is test email"
    sender_email = "meliodastheman106@gmail.com"
    receiver_email = "sthamarai001@gmail.com"
    password = "meliodas1063000"
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email 
    email["Subject"] = subject
    # Add body and attachment to email
    email.attach(MIMEText(body, "plain"))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent')

