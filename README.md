# FTP-in-connected-mobile-networks
File Transfer Protocol using UDP forintermittent connectivity scenarios powered using Python and Secure shell
# Introduction


For this assignment, in order to create robust File Transfer Protocol, had two main candidates to use: TCP and UDP protocol.
The well-known SSH Protocol, used to log into a remote machine and execute commands is relying on TCP protocol. It uses a TCP port when connecting to it. 
TCP is a much more reliable connection than UDP because it goes through a 3 way handshake known as SYN SYN-ACK ACK which synchronizes and acknowledges the connection, thus guaranteeing delivery. TCP provides error-checking and guarantees delivery of data and that packets will be delivered in the order they were sent.

On the other hand, UDP is a connectionless protocol that assumes that error-checking and recovery services are not required. Instead, UDP continuously sends datagrams to the recipient whether they receive them or not.

Below is a comparison between them and reasons about choosing the UDP.
1. Reliability
TCP is reliable. Data sent using a TCP protocol is guaranteed to be delivered to the receiver. If data is lost in transit it will recover the data and resend it. TCP will also check packets for errors and track packets so that data is not lost or corrupted.

UDP is unreliable, it does not provide guaranteed delivery and a datagram packet may become corrupt or lost in transit.

2. Flow control
TCP uses a flow control mechanism that ensures a sender is not overwhelming a receiver by sending too many packets at once. It stores data in a send buffer and receives data in a receive buffer. When an application is read, it will read the data from the receive buffer. If the receive buffer is full, the receiver would not be able to handle more data and would drop it. TO maintain the amount of data that can be sent to a receiver, it tells the sender how much spare room in the receive buffer there is (receive window). Every time a packet is received, a message is sent to the sender with the value of the current receive window.

UDP does not provide flow control. With UDP, packets arrive in a continuous stream or they are dropped.

1. Ordering
TCP does ordering and sequencing to guarantee that packets sent from a server will be delivered to the client in the same order they were sent.
On the other hand, UDP sends packets in any order.

2. Speed
TCP is slower than UDP because it has a lot more to do. TCP has to establish a connection, error-check, and guarantee that files are received in the order they were sent.

Please read documentation report for further information.

