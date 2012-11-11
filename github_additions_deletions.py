import web
import json
import time
import serial
import httplib

urls = (".*", "handler")

SERIAL_PORT = '/dev/tty.usbmodemfd121'
SERIAL_BAUD = 9600


class handler:

    def GET(self):
        print 'hello'

    def POST(self):
        data = web.input()
        payload = json.loads(data.payload)
        s = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
        time.sleep(1)
        repository = payload['repository']

        commits = payload['commits']
        for commit in commits:
            request = httplib.HTTPSConnection('api.github.com')
            request.request("GET", "/repos/%s/%s/commits/%s" % (repository['owner']['name'], repository['name'], commit['id']))
            response = request.getresponse()
            c = json.loads(response.read())
            message = "0,%s,%s" % (c['stats']['additions'], c['stats']['deletions'])
            s.write(message)
        s.close()


if __name__ == '__main__':

    app = web.application(urls, globals())
    app.run()
