import os

class Scenes:
    sc_ID: str
    sc_Date: str

    def __init__(self, sceneID) -> None:
        self.sc_ID = sceneID
        self.sc_Date = self.getDate()        

    def cls(self):
        os.system('clear')

    def getDate(self)->str:
        return "November 21, 2023"


class Dashboard(Scenes):
    act = "Activity"
    dur = "duration"
    state = "State"
    start = "Start"
    end = "End"
    type = "Type"
    total: int = 0
    select: str = ""
    setType: str = ""
    setAct: str = ""

    def nav(self, data):
        print("~"*108)
        print(f"[Q]Add Activity    [F]Edit   [W]Calendar   [E]Graph")
        print("~"*108)
        self.select = input("Select: --> ")
        match self.select:
            case 'Q':                
                return self.addActivity(data)
            case 'q':
                return self.addActivity(data)
            case _:
                return self.scene(data)
            

    def dashb(self, data):
        self.cls()
        print("-"*46, "SELF-TRACK APP", "-"*46)
        print(f"Date: {self.sc_Date}")
        print("_"*108)
        print(f"{self.act:41} | {self.dur:10} | {self.state:10} | {self.start:10} | {self.end:10} | {self.type:5}")
        print("~"*108)
        for items in range(len(data)):
            print(f"{data[items]['name']:41} | {data[items]['dur']:10} | {data[items]['state']:10} | {data[items]['start']:10} | {data[items]['end']:10} | {data[items]['type']:5}")
        print("~"*108)
        print(f"Total: {self.getTotalDur(data)}")

    def scene(self, data):        
        self.dashb(data)
        self.nav(data)
        

    def getTotalDur(self, data)-> int:        
        for items in range(len(data)):
            self.total = self.total + data[items]['dur']

        return self.total
    
    def test(self, data):
        self.cls()
        for items in range(len(data)):
            print(f"Contents: {items}")
            print(f"Contents: {data[items]['name']}")

    def addActivity(self, data):
        self.SetType(data)
        self.SetAct(data)
        
    def SetType(self, data):
        self.cls()
        self.dashb(data)
        print("~"*108)            
        self.setType = input("[Type] ---> ")

    def SetAct(self, data):
        self.cls()
        self.dashb(data)
        print("~"*108)
        self.setAct = input("[Activity] ---> ")
        
    
class Welcome(Scenes):

    year: str
    month: str
    day: int
    wctxt: str
    select: str

    def __init__(self, sceneID) -> None:
        super().__init__(sceneID)
        self.year = "2023"
        self.month = "November"
        self.day = 0
        self.wctxt = """
Welcome User,

I would like to thank you for trying this software.
I hope this software helps you grow.

Regards,
Jeruzael/Developer
"""
        

    def setYear(self, year: str = "2023"):
        self.year = year
    
    def setMonth(self, month: str = "November"):
        self.month = month
    
    def setDay(self, day: int = 0):
        self.day = day
    
    def welcome(self):
        self.cls()
        print("-"*46, "SELF-TRACK APP", "-"*46)
        print(self.wctxt)
        print("-"*108)        
    
    def nav(self):
        self.select = input("Set time & date: [Q] Manual   [W] Auto   ---> ")

    