from redis import Redis  
from string import ascii_letters
from random import choice

r = Redis(host='localhost', port=6379, db=0)
url = "http://127.0.0.1:5000/"

def setLink(link, time):
    notFoundKey = True

    while notFoundKey:
        code = ''.join({choice(ascii_letters) for x in range(5)})
        if not r.exists(code):
            notFoundKey = False

    time = calculate_time(time)
    r.set(code, link, time)
    return {'encoded_link': url + code}

def getLink(link):
    if r.exists(link):
        return {'decoded_link': str(r.get(link)).strip('b')}  
    else:
        return 'No such key'

def calculate_time(time):
    try: # here we can use arrow or delorean libraries functions instead
        time = list(map(lambda x: int(x), time.split(':')))
        multiplier = 3600
        
        newTime = time[0] * 86400  
        
        for i in time[1:]:
            newTime +=  i * multiplier
            multiplier = int(multiplier / 60)

        return newTime
    except ValueError:
        return 600
    
    

