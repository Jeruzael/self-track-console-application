from model.scene import Dashboard
from data.data import Sample
from data.handler import Timecapsule as tc
from data.handler import Usertime
from data.handler import Database

db = Database('2023', 'November')
#db.checkDb()
db.existentialChecker()
db.checkDb()