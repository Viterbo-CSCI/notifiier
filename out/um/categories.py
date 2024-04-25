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
    Categories.append.person_email(interest, 0, Person.email)
#Add new event
def Create_event(add_event, new_event_category):
    Categories.append.event(new_event_category, add_event, 0)
#Remove person from event group
def Removeperson(remove_Person, remove_interest):
    Categories.remove.person_email(remove_interest, 0, remove_Person.email)
#Remove event
def Remove_event(remove_event, remove_event_category):
    Categories.remove.event(remove_event_category, remove_event, 0)


