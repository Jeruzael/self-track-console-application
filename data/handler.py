import datetime
from datetime import timedelta as td
from datetime import date
from datetime import datetime as dt
import time

class Timecapsule:
    __leapYearStart: int = 2020
    __year: int = 0
    __month: str = ""
    __week: int = 0
    __day: int = 0
    date: date
    time: time

    def __init__(self) -> None:
        self.__year = self.getYear()
        self.__month = self.getMonth()
        self.__week = self.getWeek()
        self.__day = self.getDay()
        self.date = date.today()
        self.time = time.time()
        self.__getYear()
        self.__getMonth()
        self.__getWeek()
        self.__getDay()
        self.__setYear()
        self.__setMonth()
        self.__setDay()

    def setYear(self, year: int = 2023):
        self.__year = year

    def setMonth(self, month: str = "January"):
        self.__month  = month

    def setDay(self, day: int = 1):
        self.__day = day    

    def getYear(self)->int:
        return self.__year
    
    def getMonth(self)-> str:
        return self.__month
    
    def getWeek(self)-> str:
        return f'week{self.__week}'
    
    def getDay(self)-> int:
        return self.__day
    
    def getDate(self):        
        print(f"Date: {self.date}")
        print(f"Test: {dt.fromtimestamp(self.time)} GetTime: ")

    def getTimeInterval(self, start: td, end: td):
        return end - start
    
    __setYear = setYear
    __setMonth = setMonth
    __setDay = setDay
    __getYear = getYear
    __getMonth = getMonth
    __getWeek = getWeek
    __getDay = getDay
    
class Usertime(Timecapsule):

    def manualTimeSet(self, year, month, day):
        self.setYear(year)
        self.setMonth(month)
        self.setDay(day)

    def getDateInfo(self):
        print(f"Year: {self.getYear()}\nMonth: {self.getMonth()}\nDay: {self.getDay()}")