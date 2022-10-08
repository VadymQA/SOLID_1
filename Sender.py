from abc import abstractmethod


class SenderBase:
    @abstractmethod
    def notify(self):
        pass

class SenderSMS(SenderBase):
    def __init__(self, message):
        self.message = message

    def sendSMS(self):
        print("Send SMS")

class SenderEmail(SenderBase):
    def __init__(self, message):
        self.message = message

    def sendEmail(self):
        print("Send EMAIL")

class SenderMessangers(SenderBase):
    def __init__(self, message):
        self.message = message

    def sendMessanger(self):
        print("Send in messanger")

class SenderDefault(SenderBase):
    def __init__(self, message):
        self.message = message

    def informUser(self):
        SenderMessangers.sendMessanger()


