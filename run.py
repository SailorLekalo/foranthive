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
        # HERE I MAKE PARAMS'
        width = hive['map']['width']
        height = hive['map']['height']

        map = [['0']*width]*height

        for i in range (width):
            for j in range (height):
                try:
                    map[i][j] = hive['map']['cells'][i][j]['food']
                except:
                    map[i][j] = 0

        foodx=0
        foody=0

        awayer = False
        for i in range (width):
            for j in range (height):
                if map[i][j] != 0:
                    foodx = i
                    foody = j
                    awayer = True
                    break

            if awayer == True:
                break
        if foodx-hive['ants'][1]['x'] >0:
            orders['1'] = {
                "act": ACTIONS['move'],
                "dir": DIRECTIONS['right']
            }
        elif foodx-hive['ants'][1]['x'] <0:
            orders['1'] = {
                "act": ACTIONS['move'],
                "dir": DIRECTIONS['left']
            }
        elif foody-hive['ants'][1]['y'] >0:
            orders['1'] = {
                "act": ACTIONS['move'],
                "dir": DIRECTIONS['down']
            }
        elif foody-hive['ants'][1]['y'] >0:
            orders['1'] = {
                "act": ACTIONS['move'],
                "dir": DIRECTIONS['up']
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
