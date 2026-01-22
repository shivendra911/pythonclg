python http server
creating web sever 
--> python -m http.server


Know about logs from the server.

Typical log entry contains:

Client IP

Date & time

HTTP method (GET / POST)

Requested path

Status code (200, 404, 500)

Example:

127.0.0.1 - - [22/Jan/2026 10:30:15] "GET /index.html HTTP/1.1" 200 -

Logs in Python http.server (default behavior)

When you run:

python -m http.server 8000


You’ll see logs directly in the terminal:

127.0.0.1 - - [22/Jan/2026 10:30:15] "GET / HTTP/1.1" 200 -


This is called access logging.

Where do these logs come from?

Python uses:

http.server.SimpleHTTPRequestHandler


Inside it, there is a method:

log_message()


That prints logs to stdout (terminal).

Customize logs (important step)
1️⃣ Create your own server with logging
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print("[SERVER LOG]", format % args)

server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on port 8000")
server.serve_forever()


Now logs look like:

[SERVER LOG] "GET / HTTP/1.1" 200 -

Writing logs to a file (real-world skill)
2️⃣ Log to a file instead of terminal
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class MyHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info(format % args)

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()


Now a file server.log is created:

2026-01-22 10:35:20 - "GET / HTTP/1.1" 200 -


This is exactly how real servers work.

Types of logs you should know
Log type	Meaning
Access log	Who accessed what
Error log	What went wrong
Debug log	Internal details
Security log	Suspicious activity
Common HTTP status codes you’ll see in logs
Code	Meaning
200	OK
301	Redirect
403	Forbidden
404	Not Found
500	Server Error
Why logs are VERY important

Debug errors

Track users

Detect attacks

Performance analysis

Required in production servers

No serious server runs without logs.






<<IP>>
public ip
Default ips

port change
<<Mapping of dns to ip>>


mapping name to ip
<<"sudo nano /etc/hosts">>



<<how to access different devices o same network>>


HSTS

privilage escalation