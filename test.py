import json
import threading

data = {}
data['test'] = []
data['test'].append({
    'name': 'name1',
    'website': 'awebsite.com',
    'from': 'Oklahoma'
})

def printData():
    t = threading.Timer(5.0, printData)
    t.start()
    data['test'].append({
    'name': 'name2',
    'website': 'google.com',
    'from': 'Michigan'
})
    with open('api.json', 'w') as api:
        json.dump(data, api)
    
printData()