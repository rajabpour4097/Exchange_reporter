import smtplib, ssl

from send_config import port, smtp_server, sender_email, receiver_email

from email.mime.text import MIMEText



password = 'mohammad4097'


def send_smtp_email(subject, body):
    context = ssl.create_default_context()
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "finance@inprobes.com"
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as mail_server:
        mail_server.login(sender_email, password)
        mail_server.sendmail(sender_email, receiver_email, msg.as_string())
        # mail_server.quit()




