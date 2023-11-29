import random
from model.scene import Dashboard
from data.handler import Database

class Nav:    
    setHead: str = ""
    setBody: str = ""
    setFoot: str = ""

    def __init__(self) -> None:
        self.session = self.setRandomSession()
        self.dashboard = Dashboard(self.session)
        self.db = Database('2023','November')

    # Generate a random id for session
    def setRandomSession(self)->str:
        alp = "abcdefghijklmnop"
        alp_b = "ABCDEFGHIJKLMNOP"
        head = [random.choice(alp),random.choice(alp),random.choice(alp),random.choice(alp)]
        body = [str(random.randrange(9)),str(random.randrange(9)),str(random.randrange(9)),str(random.randrange(9))]        
        foot = [random.choice(alp_b),random.choice(alp_b),random.choice(alp_b),random.choice(alp_b)]
        
        for e in head:
            self.setHead = self.setHead + e
        for b in body:
            self.setBody = self.setBody + b
        for f in foot:
            self.setFoot = self.setFoot + f
        sessionNo = "session-"+self.setHead+self.setBody+self.setFoot
        return sessionNo

    # Return the session id
    def getSession(self)->str:
        return self.session
    
    # Door
    def startTracking(self):
        self.dashboard.scene(self.db.getActivities())
        
