#!/usr/bin/env python

import SocketServer
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

import argparse, sys, os

class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

def run():

    parser = argparse.ArgumentParser(prog="simplehttp")
    parser.add_argument('-i', '--interface', type=str, default="",
        help='Interface to listen on, defaults to all.')
    parser.add_argument('-p', '--port', type=int, default = 8080,
        help='Port to run on.')
    parser.add_argument('--pidfile', type=str, default="/dev/null",
        help='Write the PID to a file.')
    parser.add_argument('-r', '--root', type=str, default="./",
        help='Document root.  Defaults to current directory.')

    args = parser.parse_args(sys.argv[1:])

    if args.pidfile != "/dev/null":
        with open(args.pidfile, "w") as fh:
            fh.write(str(os.getpid()))

    os.chdir(args.root)
    server_address = (args.interface, args.port)
    httpd = ThreadingHTTPServer(server_address, SimpleHTTPRequestHandler)
    print "Running on %s:%s" % server_address
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Exiting on Ctrl-C."
        if args.pidfile != "/dev/null" and os.path.exists(args.pidfile):
            os.remove(args.pidfile)

if __name__=="__main__":
    run()
