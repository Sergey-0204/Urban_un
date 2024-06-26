#import random
import random


#def say_hello(name):
#print('hello', name)
#say_hello('max')
#say_hello('Den')

#def lottery():
#   tickets = [1, 2, 3, 4, 5, 6,]
#   win = random.choice(tickets)
#   return win
#win = lottery()
#print(win)


def lottery(mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2
