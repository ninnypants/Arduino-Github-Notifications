import web
import json
import serial

urls = (".*", "handler")

SERIAL_PORT = '/dev/tty.usbmodemfa131'
SERIAL_BAUD = 9600


class handler:

    def GET(self):
        print 'hello'

    def POST(self):
        data = web.input()
        payload = json.loads(data.payload)
        s = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)

        commits = payload['commits']
        for commit in commits:
            message = "0,%s,%s" % (commit['added'], commit['removed'])
            s.write(message)
        s.close()


if __name__ == '__main__':

    app = web.application(urls, globals())
    app.run()
