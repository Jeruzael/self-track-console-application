from model.scene import Dashboard
from data.data import Sample
from data.handler import Timecapsule as tc
from data.handler import Usertime
from data.handler import Database

db = Database('2023', 'November')
#db.addDay('2023','November')
#db.addMonth('2023','December')
db.checkDb()