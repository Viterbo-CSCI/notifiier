import uuid
from notifier import Notifier
from person import Person

class Event:
    def __intit__ (self, admin, name, date, advanceNoticeTime, capacity, location, end_time, send_invite):
        self.cancelled = False
        self.admin = admin
        self.name = name
        self.date = date
        self.attendees = []
        self.advanceNoticeTime = advanceNoticeTime
        self.UID = uuid.uuid4()
        self.capacity = capacity
        self.Active = True
        self.location = location
        self.end_time = end_time
        self.send_invite = send_invite
     
     
    def RSVP(self, Person):
        if not self.cancelled and len(self.attendees) < self.capacity:
            self.attendees.append(Person)
            return True
        else:
            return False
        
    def checkAttendance(self):
        return len(self.attendees)

    def sendSmsInvite(self):
        self.send_invite = True
        my_notifier = Notifier()
        for person in self.attendees:
            try:
                my_notifier.send_sms(person, self)
            except:
                print("Error sending SMS to:", person.phone)
        return True 
    
    def sendEmailInvite(self):
        self.send_invite = True
        my_notifier = Notifier()
        for person in self.attendees:
            try:
                my_notifier.send_email(person, self)
            except:
                print("Error sending email to:", person.email)
        
        return True 

    def cancelEvent(self):
        self.cancelled = True
        self.active = False 
        self.send_invite = False
        return True
    