import smtplib, ssl

def send_mail(sender_email, content):

    port = 465  # For SSL
    receiver_email = "19131a1231@gvpce.ac.in"#Change to ur credentials.
    password = "9948072982Aa@"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(receiver_email, password)
        server.sendmail(sender_email, receiver_email, content)