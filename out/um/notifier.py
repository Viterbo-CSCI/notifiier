import smtplib
import twilio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Notifier:
    def __init__(self):
        self.email = EmailInviter()
        self.sms = SMSInviter()
    def send_sms(self, Person, event):
        self.sms.send_sms(Person, event)
    def send_email(self, Person, event):
        self.email.send_invitation(Person, event)

#region EmailNotifier
class EmailInviter:
    def __init__(self, host, port, username, password):
        """
        Initializes the EmailInviter with the required server and login details.
        Args:
            host (str): SMTP host address.
            port (int): SMTP port number.
            username (str): Login username.
            password (str): Login password.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        # Establish a connection to the email server
        self.server = smtplib.SMTP(host, port)
        self.server.starttls()  # Start TLS encryption
        self.server.login(username, password)
    
    def send_invitation(self, person, event):
        """
        Sends an email invitation to a list of recipients.
        Args:
            subject (str): The subject line of the email.
            message (str): The body of the email.
            from_addr (str): The sender's email address.
            to_addrs (list): A list of recipient email addresses.
        Returns:
            None
        """
        # Create the email message
        email_message = MIMEMultipart()
        email_message['From'] = person.email
        email_message['To'] = ", ".join(person.to_addresses)
        email_message['Subject'] = "You are invited to " + event.name
        email_message.attach(MIMEText("message", 'plain'))
        
        # Send the email
        self.server.send_message(email_message)
        print("Email sent to:", email_message['To'])
    
    def close(self):
        """
        Closes the connection to the SMTP server.
        Returns:
            None
        """
        # Close the server connection
        self.server.quit()
#endregion

#region SmsNotifier

class SMSInviter:
    def __init__(self, account_sid, auth_token):
        """
        Initializes the SMSInviter with Twilio account details.
        Args:
            account_sid (str): Twilio Account SID.
            auth_token (str): Twilio Auth Token.
        """
        self.client = Client(account_sid, auth_token)
        self.from_number = None

    def send_sms(self, Person, event):
        
        self.send_invite(Person.phone, f"You're invited to {event.name} on {event.date} at {event.location}")

    def set_from_number(self, from_number):
        """
        Sets the Twilio phone number that will appear as the sender.
        Args:
            from_number (str): The phone number assigned by Twilio.
        Returns:
            None
        """
        self.from_number = from_number

    def send_invite(self, Person, message):
        """
        Sends an SMS invitation to a specified phone number.
        Args:
            to_number (str): The recipient's phone number.
            message (str): The message text of the SMS.
        Raises:
            ValueError: If the from number is not set.
        Returns:
            None
        """
        if not self.from_number:
            raise ValueError("From number is not set.")
        message = self.client.messages.create(
            to=to_number,
            from_=self.from_number,
            body=message
        )
        print(f"Sent message to {to_number}; SID: {message.sid}")

#endregion

if __name__ == "__main__":
    # Email Inviter
    email_host = 'smtp.office365.com'
    email_port = 587
    email_username = '' #TODO
    email_password = '' #TODO
    inviter = EmailInviter(email_host, email_port, email_username, email_password)
    
    subject = "You're Invited!"
    message = "Hi there! Please join us at our event."
    from_address = '' #TODO
    to_addresses = [''] #TODO 
    
    inviter.send_invitation(subject, message, from_address, to_addresses)
    inviter.close()

    #SMS Inviter
    # account_sid = '' #TODO
    # auth_token = '' #TODO
    # from_number = '' #TODO
    # to_number = '' #TODO

    # inviter = SMSInviter(account_sid, auth_token)
    # inviter.set_from_number(from_number)
    # message = "You're invited to our special event!"
    # inviter.send_invite(to_number, message)
