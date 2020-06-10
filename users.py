
import random
import json

users = [{'admin' : False, 'active' : True, 'name' : 'James'},
        {'admin' : False, 'active' : False, 'name' : 'Johnas'},
        {'admin' : True, 'active' : True, 'name' : 'Jason'},
        {'admin' : True, 'active' : False, 'name' : 'Theodore'},
        {'admin' : True, 'active' : True, 'name' : 'Daniel'},
        ]
line = 1

for user in users:
    prefix =f"{line} "
    if user['admin'] == True and  user['active']== True:
        prefix+= 'ACTIVE - (ADMIN)'
    elif user['admin'] == True and user['active']== False:
        prefix += '(ADMIN)'
    elif user['active'] == True and user['admin'] == False:
        prefix += 'ACTIVE -'

    print(f"{prefix} {user['name']}")
    line += 1
