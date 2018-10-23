#!/usr/bin/env python

import json
import random

try:  # For python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:  # For python 2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

ACTIONS = ["move", "eat", "load", "unload"]
DIRECTIONS = ["up", "down", "right", "left"]


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        payload = self.rfile.read(int(self.headers['Content-Length']))

        # Hive object from request payload
        hive = json.loads(payload)

        # Loop through ants and give orders
        orders = {}
        # HERE I FIND HIVE'S LIMITS'
        hivexmax = -1
        hiveymax = -1
        hivexmin = -1
        hiveymin = -1

        for i in range (hive['map']['width']):
            for d in range(hive['map']['height']):
                if hive['map']['cells'][i][d]['hive'] == hive['id']:
                    hivexmin = hive['map']['cells'][i]
                    hiveymin = hive['map']['cells'][i][d]
                    break
        for i in reversed(hive['map']['width']):
            for d in reversed(hive['map']['height']):
                if hive['map']['cells'][i][d]['hive'] == hive['id']:
                    hivexmax = hive['map']['cells'][i]
                    hiveymax = hive['map']['cells'][i][d]

        for ant in range (hive['ants']):

            orders[1] = {
                "act": ACTIONS['move'],
                "dir": DIRECTIONS['right']

            }
        response = json.dumps(orders)
        print(response)

        try:  # For python 3
            out = bytes(response, "utf8")
        except TypeError:  # For python 2
            out = bytes(response)

        self.wfile.write(out)

        # json format sample:
        # {"1":{"act":"load","dir":"down"},"17":{"act":"load","dir":"up"}}
        return


def run():
    server_address = ('0.0.0.0', 7070)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()


run()
