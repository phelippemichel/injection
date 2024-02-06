from core.Load import Load
from core.Database import Database
from core.Movement import Movement

def start(Client):
    Pid = Load.get_pid(Client)
    Movement.createRouter(Client,Pid)

    # Database.setRoutes("test",1,(5143,5134,6),(5133,5134,6))
    # Database.checkFile()
    # print(Pid)