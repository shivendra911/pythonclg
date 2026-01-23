Server other than http

🌐 Web / Application (Non-HTTP or HTTP-adjacent)

HTTPS – HTTP + TLS (secure web)

WebSocket (WS / WSS) – real-time, full-duplex communication (chat, games)

gRPC – high-performance RPC over HTTP/2 (microservices)

FastCGI / uWSGI – app servers behind web servers (Python, PHP)

📁 File Transfer Servers

FTP – basic file transfer

FTPS – FTP + SSL/TLS

SFTP – file transfer over SSH (very common)

TFTP – lightweight transfer (network devices, PXE boot)

🔐 Remote Access / Control

SSH Server – secure remote shell, tunneling, file copy

Telnet Server – old, insecure remote shell (mostly obsolete)

RDP Server – remote desktop (Windows)

📧 Email Servers

SMTP – sending emails

POP3 – downloading emails

IMAP – syncing emails across devices

🗄️ Database Servers

MySQL Server

PostgreSQL Server

MongoDB Server

Redis Server

Oracle DB Server

(They listen on their own ports, not HTTP)

📡 Messaging / Streaming

MQTT Broker – IoT, sensors, lightweight messaging

AMQP (RabbitMQ) – message queues

Kafka Broker – event streaming

ZeroMQ – high-speed messaging

🕒 Time / Infrastructure

NTP Server – time synchronization

DNS Server – domain → IP resolution

DHCP Server – auto IP assignment

🎮 Media / Gaming

RTSP Server – video streaming

RTP Server – real-time media transport

Game Servers – custom TCP/UDP protocols

🧪 Development / Local Servers

Python TCP/UDP socket server

Node.js net server

Unix domain socket server

Custom protocol servers

🔍 Key idea (important)

HTTP is just one protocol

A server = program listening on a port

Protocol defines how data is exchanged, not whether it’s “web” or not

Example:

SSH  → port 22
FTP  → port 21
SMTP → port 25
DNS  → port 53
HTTP → port 80
