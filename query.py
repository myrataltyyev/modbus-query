from scapy.all import *
import time

# Modbus ADU
class ModbusTCP(Packet):
    name = "Modbus/TCP"
    fields_desc = [ ShortField("Transaction Identifier", 1),
                    ShortField("Protocol Identifier", 0),
                    ShortField("Length", 6),
                    XByteField("Unit Identifier", 247),
                    ]
# Modbus PDU
class Modbus(Packet):
    name = "Modbus"

    fields_desc = [ XByteField("Function Code", 4),
                    ShortField("Reference Number", 1),
                    ShortField("Word Count", 2),
                    ]

# Create a socket and connect
#---Feed 1---#
s10 = socket.socket()
s10.connect(("192.168.95.10", 502))
ss10 = StreamSocket(s10, Raw)

#---Feed 2---#
s11 = socket.socket()
s11.connect(("192.168.95.11", 502))
ss11 = StreamSocket(s11, Raw)

#---Purge---#
s12 = socket.socket()
s12.connect(("192.168.95.12", 502))
ss12 = StreamSocket(s12, Raw)

#---Product---#
s13 = socket.socket()
s13.connect(("192.168.95.13", 502))
ss13 = StreamSocket(s13, Raw)

#---Tank---#
s14 = socket.socket()
s14.connect(("192.168.95.14", 502))
ss14 = StreamSocket(s14, Raw)

# pkt.show()
while True:
    try:
        # Encapsulate modbus inside the raw data, then send and receive
        resp = ss10.sr1(Raw(ModbusTCP()/Modbus()), verbose=0)
        resp = ss11.sr1(Raw(ModbusTCP()/Modbus()), verbose=0)
        resp = ss12.sr1(Raw(ModbusTCP()/Modbus()), verbose=0)
        resp = ss13.sr1(Raw(ModbusTCP()/Modbus()), verbose=0)
        resp = ss14.sr1(Raw(ModbusTCP()/Modbus()), verbose=0)

        time.sleep(1)
    except KeyboardInterrupt:
        break
