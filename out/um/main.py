from flask import Flask, jsonify, request
from notifier import EmailInviter, SMSInviter
from events import Event
from person import Person
# Other necessary imports

app = Flask(__name__)


# Notification Management
@app.route('/notify/email', methods=['POST', 'GET'])
def send_email_notification():
    # Extract email address from URL query parameter
    email = request.args.get('email', None)
    if not email:
        return jsonify(message="No email provided"), 400
    
    # Assuming Event.sendEmailInvite() now takes an email parameter
    response = Event.sendEmailInvite(email)
    return jsonify(message="Email notification sent to {}".format(email)), 200
@app.route('/notify/sms', methods=['POST'])
def send_sms_notification():
   # Extract phone number from URL query parameter
    phone = request.args.get('phone', None)
    if not phone:
        return jsonify(message="No phone number provided"), 400
    
    # Assuming Event.sendSmsInvite() now takes a phone number parameter
    response = Event.sendSmsInvite(phone)
    return jsonify(message="SMS notification sent to {}".format(phone)), 200
# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
