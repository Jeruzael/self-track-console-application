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

    def scene(self, data):        
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
        print("~"*108)
        print(f"[Q]Add Activity    [F]Edit   [W]Calendar   [E]Graph")
        print("~"*108)
        self.select = input("Select =====> ")

    def getTotalDur(self, data)-> int:        
        for items in range(len(data)):
            self.total = self.total + data[items]['dur']

        return self.total
    
    def test(self, data):
        self.cls()
        for items in range(len(data)):
            print(f"Contents: {items}")
            print(f"Contents: {data[items]['name']}")