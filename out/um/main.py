from flask import Flask, jsonify, request
from person import Person
from events import Event
from categories import Category
from notifier import NotificationService
# Other necessary imports

app = Flask(__name__)

# Account Management
@app.route('/account/create', methods=['POST'])
def create_account():
    data = request.get_json()
    new_person = Person(data['Name'], data['Email'])
    # Add logic to save person to database
    return jsonify(message="Account created successfully", id=new_person.UserID), 201

@app.route('/account/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def account(user_id):
    if request.method == 'GET':
        # Logic to retrieve a person's information
        pass
    elif request.method == 'PUT':
        # Logic to update a person's information
        pass
    elif request.method == 'DELETE':
        # Logic to delete an account
        pass
    return jsonify(success=True), 200

# Category Management
@app.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(data['Name'])
    # Add logic to save category
    return jsonify(message="Category created successfully", id=new_category.Id), 201



@app.route('/create_category/<int:person_email>/<string:cat_name>', methods=['GET'])
def create_category(person_email, cat_name): 
    # Logic to create a category
    pass

@app.route('/add_event_category/<int:category_id>/<id:event_id>', methods=['GET'])
def add_event_category(category_id, event_id):
    # Logic to add an event to a category
    pass


@app.route('/category/<int:category_id>/subscribe', methods=['POST'])
def subscribe_to_category(category_id):
    # Logic for a person to subscribe to a category
    pass

@app.route('/category/<int:category_id>/unsubscribe', methods=['POST'])
def unsubscribe_from_category(category_id):
    # Logic for a person to unsubscribe from a category
    pass


@app.route('/event/create/<string:name>/<string:event_date>', methods=['GET'])
def create_event():
    def create_event(name, event_date):
     new_event = Event(name, event_date)
     return jsonify(message="Event created successfully", id=new_event.UID), 201

# Event Management
@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(data['name'], data['date'])
    # Add logic to save event
    return jsonify(message="Event created successfully", id=new_event.UID), 201

@app.route('/event/<int:event_id>/assign', methods=['POST'])
def assign_event_to_category(event_id):
    # Logic to assign an event to a category
    pass

@app.route('/event/<int:event_id>/notify', methods=['POST'])
def send_event_notifications(event_id):
    # Logic to send notifications for an event
    pass

@app.route('/event/<int:event_id>/rsvp', methods=['POST'])
def rsvp_event(event_id):
    # Logic for RSVP'ing to an event
    pass

# Notification Management
@app.route('/notify/email', methods=['POST'])
def send_email_notification():
    data = request.get_json()
    NotificationService.sendEmail(data['person'], data['event'])
    return jsonify(message="Email notification sent"), 200

@app.route('/notify/sms', methods=['POST'])
def send_sms_notification():
    data = request.get_json()
    NotificationService.sendSMS(data['person'], data['event'])
    return jsonify(message="SMS notification sent"), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
