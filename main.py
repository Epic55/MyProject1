from sql import *
from tk import *

def f(agrument):
    match agrument:
        case "1": return select()
        case "2": return insert()
        case "3": return delete()
        case "4": return update()
        case "5": return sendmsg()
        case "6": return gui()
        case "7": exit()
for i in iter(int,1):
    print("\n","Choose number what u want to do: ")
    print(" 1 - show all shares, 2 - insert data about new share, 3 - delete data about share,","\n",
          "4 - update data about share, 5 - send msg via rabbitmq, 6 - launch GUI, 7 - exit")
    f(input("Enter number: "))