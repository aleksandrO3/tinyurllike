from redis import Redis  
from string import ascii_letters
from random import choice
from json import load, dumps

r = Redis(host='localhost', port=6379, db=0)
url = "http://127.0.0.1:5000/"


def setLink(data):  
    if 'link' in data.keys():
        link = data['link']
    else:
        return {'encoded_link': 'empty link was sent'}
    
    if 'time' in data.keys() and not data['time'] == 0:
        time = data['time']
    else:
        time = 1
    
    code = generate_code(link)
    time = calculate_time(time)
    r.set(code, link, time)
    return {'encoded_link': url + code}


def getLink(link):  
    if r.exists(link):
        return {'decoded_link': str(r.get(link)).strip('b')}  
    else:
        return 'No such key'


def calculate_time(time): 
    try: 
        return int(time) * 86400
    except ValueError:
        return 86400

def generate_code(link): 
    notFoundKey = True
    valueExist = isValueInDB(link)

    if not valueExist:
        while notFoundKey:
            code = ''.join({choice(ascii_letters) for x in range(5)})
            if not r.exists(code):
                notFoundKey = False

        addPairToDB(link, code)

        return code 
    else: 
        return valueExist
    

def isValueInDB(value):
    with open('base.json', 'r') as f:
        base = load(f)

    if value in base.keys():
        if not r.exists(base[value]): # saved in json but deleted from db
            del base[value]
            
            with open('base.json', 'w') as f: 
                base = dumps(base)
                f.write(base)
            
            return False  
        else:
            return base[value]
    else:
        return False 


def addPairToDB(key, value):
    with open('base.json', 'r') as f:
        base = load(f)
    
    base[key] = value

    with open('base.json', 'w') as f:
        base = dumps(base)        
        f.write(base)

