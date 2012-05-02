simplehttp
==========

A very simple web server.  It serves only static content and is configured by CLI options.

Usage:
======

    usage: simplehttp [-h] [-i INTERFACE] [-p PORT] [-r ROOT]
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INTERFACE, --interface INTERFACE
                            Interface to listen on, defaults to all.
      -p PORT, --port PORT  Port to run on.
      -r ROOT, --root ROOT  Document root. Defaults to current directory.
