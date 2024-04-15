import uuid


class Person:
    def __init__(self, name, email, phone, preferences):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_ID = uuid.uuid4()
        self.preferences = None  #Notifications On(True) off(False)
          
    #function to create a new Person
    def create_acct(self):
        #logic for acct function
        #create userID 
        #store accts in dictionary with userID as key and userName as value
        pass
        
    #function to create events
    def create_event(self):
        #logic for event function
        """
        
        """
        pass
    
    
    
    #function to pick a category
    def subscribe_to(self,Category):
        #logic for subscribe function
        #store categories in list, dictionary?
        pass
    
    #Function to unsubscribe from category
    def unsubscribe_from(self,Category):
        #logic for unsubscribe function
        pass

person = Person('John', 'jdoe@gmail.com', '578-684-9078', preferences=None)
print("UserID:", person.user_ID) 
 
        
    