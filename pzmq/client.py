import zmq
from zmq_strategy import ZMQStrategy
from zmq_strategy import client_strategy

# pgm can only be used as pub/sub
socket = ZMQStrategy(client_strategy).connect('epgm://239.255.0.1:10001', zmq.SUB)
#socket = ZMQStrategy(client_strategy).connect('tcp://127.0.0.1:10001')

def echo(msg):
    socket.send(msg, copy=False)
    print "Client sending %s" % msg

    server_response = socket.recv(copy=False)
    print "Client received %s" % server_response

def listen():
    # for this example listen to all topics
    socket.setsockopt(zmq.SUBSCRIBE, '')

    while True:
        topic, msg = socket.recv_multipart()
        print 'Client received topic: %s, msg:%s' % (topic, msg)
