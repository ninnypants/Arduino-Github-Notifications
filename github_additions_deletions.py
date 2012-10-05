import web
import json
import serial

urls = (".*", "handler")


class handler:

    def GET(self):
        print 'hello'

    def POST(self):
        data = web.input()
        payload = json.loads(data.payload)

        commits = payload['commits']
        for commit in commits:
            print commit


if __name__ == '__main__':

    app = web.application(urls, globals())
    app.run()
