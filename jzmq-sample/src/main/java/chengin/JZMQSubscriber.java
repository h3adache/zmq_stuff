package chengin;

import org.zeromq.ZMQ;

public class JZMQSubscriber {
    public static void main(String[] args) {
        final String topic = "time";
        final String address = "epgm://239.255.0.1:10001";
        final ZMQ.Context context = ZMQ.context(1);
        final ZMQ.Socket socket = context.socket(ZMQ.SUB);

        socket.setMulticastLoop(true);

        socket.subscribe(topic.getBytes());
        socket.bind(address);

        while(true) {
            final String message = socket.recvStr();
            System.out.printf("received %s%n", message);
        }
    }
}
