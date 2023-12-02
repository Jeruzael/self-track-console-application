import datetime
from datetime import timedelta as td
from datetime import date
from datetime import datetime as dt
import time
import os
import sys
from data.data import Sample
import json

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

class Database:
    __f: os
    structure: {}
    years: []
    months: []    
    year: str = ""
    month: str = ""
    newbie: bool = False

    # Initialize the database of the application.
    def __init__(self) -> None:   
        self.structure = {}
        self.years = []
        self.months = []              
        try:
            print(f"File exist: Getting the data")                
            self.__f = open('data/database.json', 'r+', encoding="utf-8")
            self.structure = json.load(self.__f)
            self.__f.close()
            self.getAllYear()
            self.getAllMonths()
            self.year = self.years[len(self.years) - 1]
            self.month = self.months[len(self.months)-1]
            print(self.structure['2023'])
            print(f"Current Year: {self.year}, Current month: {self.month}")
        except FileNotFoundError as err:            
            self.newbie = True
            print("Newbie is True", err)
        finally:                        
            print("Initialized!")

    # Check the file if exist.
    # If the file exist, it will read the file and extract the data.
    # If the file doesn't exist, it will create a file in designated directory.
    def existentialChecker(self, year: str = "", month: str = ""):    
        try:            
            self.__f = open('data/database.json', 'w+', encoding="utf-8")
            self.buildStructure(year, month)
            json.dump(self.structure, self.__f)
            self.__f.close()
        except FileExistsError as err:
            self.__f.close()
            print(f"File exist: Getting the data")
        finally:
            self.__f = open('data/database.json', 'r+', encoding="utf-8")
            self.structure = json.load(self.__f)
            self.__f.close()

    def getAllYear(self):
        for k,v in self.structure.items():
            self.years.append(k)
            print(self.years)

    def getAllMonths(self):
        for k, v in self.structure[self.years[len(self.years)-1]].items():
            self.months.append(k)
            print(self.months)

    def getCurrentYear(self)-> str:
        return self.years[len(self.years)-1]
    
    def getCurrentMonth(self)->str:
        return self.months[len(self.months)-1]
    
    def getCurrentDay(self)-> int:
        m = self.structure[self.getCurrentYear()][self.getCurrentMonth()]
        return self.structure[self.getCurrentYear()][self.getCurrentMonth()][len(m)-1]['day']

    # Check the contents of database
    def checkDb(self):
        self.__f = open('data/database.json', 'r+', encoding="utf-8")
        juice = json.load(self.__f)
        print(juice)
        self.__f.close()

    # Create the JSON structure of the JSON file.
    def buildStructure(self, year: str = '2023', month: str = 'January', day: int = 1):
        self.structure[year] = {
            'year': year,
            month: [
                {
                   "month": month,
                   "day": day, 
                   "activities": [{
                       "name": "Self-track setup",
                        "dur": 5,
                        "state": "Done",
                        "start": "",
                        "end": "",
                        "type": "Endeavor"
                   }]
                }
            ]
        }

    def createFile(self, year: str = "2023", month: str = "November", day: int = 1):        
        self.year = year
        self.month = month
        self.__f = open('data/database.json', 'x+', encoding="utf-8")
        self.buildStructure(self.year, self.month, day)
        json.dump(self.structure, self.__f)
        self.__f.close()
        self.getAllYear()
        self.getAllMonths()
        print("Created a file: Database.json")    
        
    # Get all the information in the database and return the extracted data.
    def getAll(self)-> object:
        self.__f = open('data/database.json', "r+", encoding="utf-8")
        juice = json.load(self.__f)
        self.__f.close()
        return juice
    
    # Get all activities and return the extracted data
    def getActivities(self)->object:
        self.structure = self.getAll()                
        return self.structure[self.year][self.month][0]['activities']

    # Add year to the JSON file.
    def addYear(self, year: str = "none"):
         data = self.getAll()
         self.structure = data
         self.structure[year] = {
             'year': year,
            'January': [
                {
                   "month": "January",
                   "day": 1, 
                   "activities": [{
                       "name": "Self-track setup",
                        "dur": 5,
                        "state": "Done",
                        "start": "",
                        "end": "",
                        "type": "Endeavor"
                   }]
                }
            ]
        }
         self.__f = open('data/database.json', 'w+', encoding="utf-8")
         json.dump(self.structure, self.__f)
         self.__f.close()
    
    # Add month to the JSON file.
    def addMonth(self,year: str = "none", month: str = "none"):
         data = self.getAll()
         self.structure = data
         self.structure[year][month] = [
                {
                   "month": month,
                   "day": 1, 
                   "activities": [{
                       "name": "Self-track setup",
                        "dur": 5,
                        "state": "Done",
                        "start": "",
                        "end": "",
                        "type": "Endeavor"
                   }]
                } 
         ]
         self.__f = open('data/database.json', 'w+', encoding="utf-8")
         json.dump(self.structure, self.__f)
         self.__f.close()

    # Add day to the JSON file.
    def addDay(self,year: str = "none", month: str = "none"):
         data = self.getAll()
         self.structure = data
         self.structure[year][month].append({
                   "month": month,
                   "day": self.structure[year][month][len(self.structure[year][month]-1)]['day'], 
                   "activities": [{
                       "name": "Self-track setup",
                        "dur": 5,
                        "state": "Done",
                        "start": "",
                        "end": "",
                        "type": "Endeavor"
                   }]
                }) 
         self.__f = open('data/database.json', 'w+', encoding="utf-8")
         json.dump(self.structure, self.__f)
         self.__f.close()

    # Add activity
    def addAct(self, year: str = "2023", month: str = "November", day: int = 0):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'].append({
                       "name": "Self-track setup",
                        "dur": 5,
                        "state": "Done",
                        "start": "",
                        "end": "",
                        "type": "Endeavor"
                   })

    # Del an specific year in the database.
    def delYear(self, year: str = ""):
        data = self.getAll()
        self.structure = data
        del self.structure[year]
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    # Del an specific month in the database.
    def delMonth(self, year: str = "", month: str = ""):
        data = self.getAll()
        self.structure = data
        del self.structure[year][month]
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    # Del an specific day in the database.
    def delDay(self, year: str = "", month: str = "", day: int = 0):    
        data = self.getAll()
        self.structure = data
        del self.structure[year][month][day]
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def delAct(self, year: str = "", month: str = "", day: int = 0, act: int = 0):    
        data = self.getAll()
        self.structure = data
        del self.structure[year][month][day]['activities'][act]
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActName(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['name'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActDur(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: int = 0):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['dur'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActState(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['state'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActStart(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['start'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActEnd(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['end'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upActType(self, year: str = "", month: str = "", day: int = 0, act: int = 0, value: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['type'] = value
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()

    def upAct(self, year: str = "", month: str = "", day: int = 0, act: int = 0, name: str = "", dur: int = 0, state: str = "", start: str = "", end: str = "", type: str = ""):
        data = self.getAll()
        self.structure = data
        self.structure[year][month][day]['activities'][act]['name'] = name
        self.structure[year][month][day]['activities'][act]['dur'] = dur
        self.structure[year][month][day]['activities'][act]['state'] = state
        self.structure[year][month][day]['activities'][act]['start'] = start
        self.structure[year][month][day]['activities'][act]['end'] = end
        self.structure[year][month][day]['activities'][act]['type'] = type
        self.__f = open('data/database.json', 'w+', encoding="utf-8")
        json.dump(self.structure, self.__f)
        self.__f.close()