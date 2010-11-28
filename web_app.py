import os
import socket
try:
    import json
except ImportError:
    import simplejson as json

import web

import convert_4lw


urls = (
    r'/', 'Index',
    r'/convert/(.*)', 'Convert',
)

render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))

class Index(object):
    def GET(self):
        return render.index()

class Convert(object):
    def GET(self, address):
        ip = socket.gethostbyname(address)
        base_address = web.ctx.host.replace('www', '').split(':')[0]
        four_lw_address = convert_4lw.to_4lw(ip) + '.' + base_address
        result = {
            'address' : address,
            'ip' : ip,
            '4lw' : four_lw_address,
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(result)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
