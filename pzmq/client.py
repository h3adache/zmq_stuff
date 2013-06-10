import zmq
from zmq_strategy import ZMQStrategy
from zmq_strategy import client_strategy

socket = ZMQStrategy(client_strategy).connect('tcp://127.0.0.1:10001')

def echo(msg):
    socket.send(msg, copy=False)
    print "Client sending %s" % msg

    server_response = socket.recv(copy=False)
    print "Client received %s" % server_response
