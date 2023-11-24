from model.scene import Dashboard
from data.data import Sample
from data.handler import Timecapsule as tc
from data.handler import Usertime
from data.handler import Database

#db.addDay('2023','November')
#db.addMonth('2023','December')
#db.upActName('2023','November', 1, 0, 'Python Programming')

db = Database('2023', 'November')
db.checkDb()
db.upActName('2023','November', 1, 0, 'Python Programming')
db.upActDur('2023','November', 1, 0, 250)
db.upActState('2023','November', 1, 0, 'Done')
db.upActStart('2023','November', 1, 0, '7:00 AM')
db.upActEnd('2023','November', 1, 0, '8:00 PM')
db.upActType('2023','November', 1, 0, 'Endeavor')
