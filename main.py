from model.scene import Dashboard
from data.data import Sample

data = Sample()

sc = Dashboard("09")
sc.scene(data.Act)
#sc.test(data.Act)