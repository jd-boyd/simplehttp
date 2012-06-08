
simplehttp
==========

A very simple web server.  It serves only static content and is configured by CLI options.

About:
======

Sometimes I want a simple http server that doesn't require a lot of
configuration and just serves files out of the current directory.

I used to use Python's SimpleHTTPServer directly:

    python -m SimpleHTTPServer 8080

However, I found that I was out growing that.  Some pages I work on
need to request so many elements that this method was very slow (since
it only serves one element at a time), and starting to be unreliable
(requests being lost).

This is a threaded server.  One thread per request, so it isn't the
most efficient of threaded servers, but it is certainly adequate for
development.

This server doesn't implement CGI, WSGI, SSL, or other such features.  It
just serves plain content.

Usage:
======

    usage: simplehttp [-h] [-i INTERFACE] [-p PORT] [-r ROOT]

    optional arguments:
      -h, --help            show this help message and exit
      -i INTERFACE, --interface INTERFACE
                            Interface to listen on, defaults to all.
      -p PORT, --port PORT  Port to run on.
      --pidfile PIDFILE     Write the PID to a file.
      -r ROOT, --root ROOT  Document root. Defaults to current directory.
