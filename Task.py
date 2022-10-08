import SenderSMS

from Sender import SenderBase, SenderDefault

message = "Status of you task was changed"

class Task:
    def __init__(self, project, name, user, status):
        self.name = name
        self.project = project
        self.user = user
        self.status = status


    def doTask(self):
        print("Task is done")

    def sd(self)
        if self.status == "DONE":
            SenderSMS().sendSMS(message)
        if self.status == "NEW":
            SenderDefault().informUser()

