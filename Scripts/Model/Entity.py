

fictionName=["Tony Stark","Scrooge McDuck","Carlisle Cullen","Bruce Wayne","Smaug","Richie Rich","Mr Burns","Lara Croft","Mr Monopoly"]
clientName=list(range(0,100))


from enum import Enum

CompanyNameList=["Wayne Industries", "Stark Industries","Umbrella Corp","Acme Corp","Beacon Street Pizza","Monster Corp","Oceanic Airlines","Roxxon"]
CompanyTypeList=["tech","tech","tech","tech","restaurant","energy","airline","energy"]

GovNameList = ["Gotham","Tatooine","Coruscant","Naboo","First Order","New Republic"]

SecurityNameDict={
    1:["Wayne Enterprises", "Stark Industries","Umbrella Corp","Acme Corp","Beacon Street Pizza","Monster Corp","Oceanic Airlines"],
    2:["Wayne Enterprises", "Stark Industries","Umbrella Corp","Acme Corp","Beacon Street Pizza","Monster Corp","Oceanic Airlines"],
    3:["Gotham","Tatooine","Coruscant","Naboo","First Order","New Republic"]
}

class SecType(Enum):
    equity = 1
    corpBond = 2
    GovBond = 3

class Security():
    def __init__(self):
        self.id=""
        self.name=""
        self.type=""
        self.secType=""
        pass

class Customer():
    def __init__(self):
        self.id=""
        self.name=""
        pass


class Trade():
    def __init__(self):
        self.tradeId=""
        self.cust=""

        self.secid=None
        self.quantity=0
        self.price=0
        self.orgType=None
        self.day=0
        pass

