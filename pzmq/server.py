import zmq
from zmq_strategy import ZMQStrategy
from zmq_strategy import server_strategy

socket = ZMQStrategy(server_strategy).connect('tcp://127.0.0.1:10001')

def start():
    while True:
        msg = socket.recv(copy=False)
        print "Server received %s" % msg
        socket.send(msg)
        print "Server sent %s" % msg
