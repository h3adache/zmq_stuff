import zmq
from zmq_strategy import ZMQStrategy
from zmq_strategy import server_strategy
from datetime import datetime
from time import sleep

# pgm can only be used as pub/sub
socket = ZMQStrategy(server_strategy).connect(socket_type=zmq.PUB)
# socket = ZMQStrategy(server_strategy).connect('tcp://127.0.0.1:10001', zmq.REP)

def start():
    while True:
        msg = socket.recv(copy=False)
        print "Server received %s" % msg
        socket.send(msg)
        print "Server sent %s" % msg

def multicast_start():
    while True:
	time = datetime.now()
        msg = "The time is now %s" % time
        socket.send_multipart(["time", msg])
        print "Server sent %s" % msg
        sleep(1)
