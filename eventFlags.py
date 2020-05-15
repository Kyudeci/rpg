class SucreNoir:
    def __init__(self):
        self.loop = 0
        self.options = False
    challengers = []

class GeardegCrest:
    def __init__(self):
        self.wins = 0
        self.battles = 0
        self.dagger = False
        self.training = False
        self.SRE = False

class GeardegRath:
    def __init__(self):
        self.options = False
        self.intro = False
    challengers = []

class Events(SucreNoir, GeardegCrest, GeardegRath):
    Flags = []
    def locAdd(self, location):
        Events.Flags.append(location)


town1 = SucreNoir()
path1 = GeardegCrest()
town2 = GeardegRath()
location = [town1, path1, town2]

def onStartFlagSet():
    for x in location:
        Events().locAdd(x)
# onStartFlagSet()
# print(Events.Flags[1].battles)
