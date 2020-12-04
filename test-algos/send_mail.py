import smtplib
from email.mime.text import MIMEText


# --------------------------------------

def send_mail(customer, emotion, comments):
    port = 2525
    smtp_server = ''
    login = ''
    password = ''
    message = f"<h3>New feedback Submission</h3><ul><li>Cliente: {customer}</li></ul>" \
              f"<ul><li>emoção: {emotion}</li></ul>" \
              f"<ul><li>frase: {comments}</li></ul>"
    sender_email = ''
    receiver_email = ''
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback Chatbot'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
