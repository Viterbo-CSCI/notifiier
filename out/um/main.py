from flask import Flask, jsonify, request
from person import Person
#from events import Event
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


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
