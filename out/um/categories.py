#import Person from UI
#import remove_Person from UI
#import interest from UI
#import remove_interest from UI
#import remove_event from UI
#import remove_event_category from UI
#import add_event from UI
#import new_event_category from UI
class Categories: #Create categories class to store info about categories
    def __init__(self, classname, event, person_email):
        self.classname = classname
        self.event = event
        self.person_email = person_email

# Create Categories for events
Categories("Sports", 0, 0)
Categories("Clubs", 0, 0)
Categories("Food", 0, 0)
Categories("Studies", 0, 0)

#Add persons
def Addperson(Person, interest):
    Categories.append(interest, 0, Person.email)
#Add new event
def Create_event(add_event, new_event_category):
    Categories.append(new_event_category, add_event, 0)
#Remove person from event group
def Removeperson(remove_Person, remove_interest):
    Categories.remove(remove_interest, 0, remove_Person.email)
#Remove event
def Remove_event(remove_event, remove_event_category):
    Categories.remove(remove_event_category, remove_event, 0)


