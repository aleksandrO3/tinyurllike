import redis
import base64 
r = redis.Redis(host='localhost', port=6379, db=0)
#f = open('index.json')

def setLink(link, time):
    code = hash(link)
    r.set(code, link, int(time))
    return code

def getLink(link):
    return str(r.get(link))