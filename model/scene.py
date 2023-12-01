import os
import time

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
        self.year = ""
        self.month = ""
        self.day = 0
        self.wctxt = """
Welcome User,

I would like to thank you for trying this software.
I hope this software helps you grow.

Regards,
Jeruzael/Developer
"""
        
    def scene(self):
        self.welcome()
        self.nav()

    def setYear(self):
        self.welcome()
        self.year = input("Year: ---> ")
    
    def setMonth(self):
        self.welcome()
        self.month = input("Month: ---> ")
    
    def setDay(self):
        self.welcome()
        self.day = input("Day: ---> ")
    
    def welcome(self):
        self.cls()
        print("-"*46, "SELF-TRACK APP", "-"*46)
        if (self.year == ""):
            print("Date: ") 
        else:
            print(f"{self.month} {self.day}, {self.year}")
        print(self.wctxt)
        print("-"*108)        
    
    def nav(self):
        self.select = input("Set time & date: [Q] Manual   [W] Auto   ---> ")
        match (self.select):
            case 'Q':
                return self.setDateManual()
            case 'q':
                return self.setDateManual()
            case 'W':
                print("Auto")
            case 'w':
                print("Auto")
            case _:
                print('Exit')

    def setDateManual(self):        
        self.setMonth()
        self.setDay()
        self.setYear()
        self.loadingScr()

    def showDate(self):
        print(f"Date: {self.month} {self.day},{self.year}")

    def loadingScr(self):                
        for i in range(50):
            self.welcome()
            print("Configuring: pls wait :) " + f"#"*i + f" {(i+1)*2}%")
            time.sleep(0.02)
        for i in range(4):
            self.welcome()
            print(f"Starting: {3-i}")
            time.sleep(1)
