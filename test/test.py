import json
import urllib2

data = json.dumps({"userID":"1234test", "facebookFriends":['f1','f2','f3','f4']})
burl = "http://friendzy.herokuapp.com"
#burl = "http://127.0.0.1:8000"
url = burl + '/login'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
response=None
try:
    f = urllib2.urlopen(req)
    response = f.read()
    print 'asdf'
    f.close()
except urllib2.HTTPError, error:
    print error.read()
    k= open('test.html','w')
    k.write(error.read())
    k.close()
print response






url = burl + '/set_status'
data = json.dumps({"userID":"1234test", "status":'this is a status'})
#url = "http://127.0.0.1:8000/set_status"
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
response=None
try:
    f = urllib2.urlopen(req)
    response = f.read()
    print 'asdf'
    f.close()
except urllib2.HTTPError, error:
    k= open('test.html','w')
    k.write(error.read())
    k.close()
print response
