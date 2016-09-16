import urllib2
import urllib
import time
import datetime

params = {
    "username": "testuser",
    "password": "testpwd",
    "to": "1234567890",
    "content": ""
    }

if __name__ == "__main__":
    (clock0, time0, dt0) = (time.clock(), time.time(), datetime.datetime.now())
    for i in range(0, 3):
        params["content"] = "message.{}".format(i)
        resp = urllib2.urlopen("http://127.0.0.1:1401/send?{}".format(urllib.urlencode(params))).read()
        if resp[:7] != "Success":
            print "{}, {}".format(i, resp)

    (clock1, time1, dt1) = (time.clock(), time.time(), datetime.datetime.now())

    (dc, dt, ddt) = (clock1 - clock0, time1 - time0, dt1 - dt0)
    print "(dc = {}. dt = {}, ddt = {})".format(dc, dt, ddt)

