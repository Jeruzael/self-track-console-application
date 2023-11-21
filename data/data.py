from dataclasses import dataclass

@dataclass
class Sample:

    Act = [
        {
        "name": "Python programming",
        "dur": 200,
        "state": "Done",
        "start": "8:00 am",
        "end": "12:00 pm",
        "type": "Endeavor"
    },
    {
        "name": "Lunch",
        "dur": 20,
        "state": "Done",
        "start": "12:00 pm",
        "end": "12:20 pm",
        "type": "Self-time"
    },
    {
        "name": "wash Dishes",
        "dur": 10,
        "state": "Done",
        "start": "12:20 pm",
        "end": "12:40 pm",
        "type": "House Chores"
    },
    {
        "name": "Woke up late because of emergency meeting",
        "dur": 10,
        "state": "Done",
        "start": "12:20 pm",
        "end": "12:40 pm",
        "type": "House Chores"
    }

]