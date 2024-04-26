from flask import Flask, jsonify, request
from notifier import EmailInviter, SMSInviter
from events import Event
from person import Person
# Other necessary imports

app = Flask(__name__)


# Notification Management
@app.route('/notify/email', methods=['POST', 'GET'])
def send_email_notification():
    # Example
    # Event.sendEmailInvite()
    return jsonify(message="Email notification sent"), 200

@app.route('/notify/sms', methods=['POST'])
def send_sms_notification():
    # Example
    # Event.sendSmsInvite()
    return jsonify(message="SMS notification sent"), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
