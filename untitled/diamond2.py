import socket, ssl, pysftp


bindsocket = socket.socket()
bindsocket.bind(('', 10022))
bindsocket.listen(5)


run=True

#ssl receive and create file
def do_something(connstream, data):
        print "do something: ", data
        file = open('payload.json', 'w')
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

#sftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None    # disable host key checking.


cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux.abington.psu.edu', 'username':'AbuSakif', 'password':'sakifabu', 'port':109}
try:
  with pysftp.Connection(**cinfo) as sftp:
    try:
        sftp.cd('/home/AbuSakif')               # temporarily chdir to public
        sftp.put('payload.json','/home/AbuSakif/ProjectDiamond/payload.json')  # upload file to public/ on remote
        #sftp.get('remote_file')         # get a remote file
    except:
        print "File transfer issue"
except Exception, err:
 print err
