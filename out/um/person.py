import uuid
from categories import Categories
from events import Event
from notifier import EmailInviter, SMSInviter  


class Person:
    def __init__(self, name, email, phone, preferences):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_ID = uuid.uuid4()
        self.preferences = None  #Notifications On(True) off(False)
        self.accounts = {}
        self.subscribe_categories = []
          
    #function to create a new Person
    def create_acct(self):
        user_id = uuid.uuid4()
        self.accounts[user_id] = userName
        #logic for acct function
        #create userID 
        #store accts in dictionary with userID as key and userName as value
        
        
    #function to create events
    def create_event(self, event_name, event_date):
        #logic for event function
        new_event = Event(event_name, event_date):
        
        self.events_created.append(new_event)
        return new_event
        
    #function to pick a category
    def subscribe_to(self,Category):
        self.subscribed_categories.add(Category)
    
    #Function to unsubscribe from category
    def unsubscribe_from(self,Category):
        if Category in self.subscribed_categories:
            self.subscribed_categories.remove(Category)
        else:
            print("You aren't subscribed to that {Category}")
        #logic for unsubscribe function
        pass

person = Person('John', 'jdoe@gmail.com', '578-684-9078', preferences=None)
print("UserID:", person.user_ID) 
 
        