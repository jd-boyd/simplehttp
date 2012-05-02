#!/usr/bin/env python

import threading
import SocketServer
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

import sys, os

class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass


server_address = ('', 8080)
httpd = ThreadingHTTPServer(server_address, SimpleHTTPRequestHandler)
print "Running on %s:%s" % server_address
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print "Exiting on Ctrl-C."


