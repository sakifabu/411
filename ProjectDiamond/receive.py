import socket, ssl


bindsocket = socket.socket()
bindsocket.bind(('', 10025))
bindsocket.listen(5)


run=True


def do_something(connstream, data):
        print "do something: ", data


        #creates new file with payload
        file = open('message.json', 'w')
        file.write(data)
        file.close()
        run=False
        return False


def deal_with_client(connstream):
        data = connstream.read()
        while data:
                if not do_something(connstream, data):
                        break
                data = connstream.read()


while run:
        newsocket, fromaddr = bindsocket.accept()
        connstream = ssl.wrap_socket(newsocket, server_side=True, certfile="server.crt", keyfile="server.key")
        try:
                deal_with_client(connstream)
        finally:
                connstream.shutdown(socket.SHUT_RDWR)
                connstream.close()

