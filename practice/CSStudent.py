class CSStudent:
    stream = 'cse'
    def __init__(self,roll):
        self.roll = roll
    def getRoll(self):
        return self.roll
    def setName(self, name):
        self.name =  name
    def getName(self):
        return self.name
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address
p = CSStudent(234)
p.setName("Vanshika")
p.setAddress("Greater Noida")
print(p.getRoll())
print(p.getName())
print(p.getAddress())
