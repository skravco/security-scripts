import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_phishing_email(to_email):
    # Set the sender's email address
    from_email = 'fake@mail.com'

    # Create a MIME multipart message object for alternative content (text and HTML)
    msg = MIMEMultipart('alternative')

    # Set email subject, sender, and recipient
    msg['Subject'] = 'Important Security Update'
    msg['From'] = from_email
    msg['To'] = to_email

    # Define the HTML content of the email
    html = '''
    <html>
    <head></head>
    <body>
    <p>
    Click <a href="http://www.___.com">here</a> to update your profile.
    </p>
    </body>
    </html>
    '''

    # Create a MIMEText object with HTML content
    part = MIMEText(html, 'html')

    # Attach the HTML part to the email message
    msg.attach(part)

    # Create an SMTP (Simple Mail Transfer Protocol) connection to localhost
    s = smtplib.SMTP('localhost')

    # Send the email from the sender to the recipient
    s.sendmail(from_email, [to_email], msg.as_string())

    # Close the SMTP connection
    s.quit()

# Target email address to send the phishing email to
target_email = 'victim@example.com'

# Call the send_phishing_email function with the specified target email
send_phishing_email(target_email)
