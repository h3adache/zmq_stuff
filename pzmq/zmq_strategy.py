import zmq

def client_strategy(self, socket, url) :
    socket.connect(url)

def server_strategy(self, socket, url) :
    socket.bind(url)

class ZMQStrategy :
    connect_strategy = client_strategy

    def __init__(self, connect_strategy=None) :
        self.context = zmq.Context()
        if connect_strategy :
             self.connect_strategy = connect_strategy

    def connect(self, url, socket_type=zmq.REQ) :
        socket = self.context.socket(socket_type)
        self.connect_strategy(self, socket, url)
        return socket
