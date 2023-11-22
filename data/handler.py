from datetime import date
import datetime
import time

class Center:
    year: str = ""
    month: str = ""
    week: str = ""
    day: str = ""
    date: date
    time: str = ""

    def __init__(self) -> None:
        self.year = self.getYear()
        self.month = self.getMonth()
        self.week = self.getWeek()
        self.day = self.getDay()
        self.date = date.today()
        self.time = self.time

    def getYear(self)->str:
        return '2023'
    
    def getMonth(self)-> str:
        return 'November'
    
    def getWeek(self)-> str:
        return 'week1'
    
    def getDay(self)-> str:
        return '21'
    
    def getDate(self):
        print(f"Date: {self.date}")
        print(f"Test: {datetime.datetime.utcnow()}")