import Pyro4,pika

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
                payload = name
               # Obj  = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
               # length = 16 - (len(payload)%16)
               # payload +=bytes([length])*length
               # message = Obj.encrypt(payload)
		message = name
                connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
                channel = connection.channel()

                channel.queue_declare(queue='rabbitmessage')

                channel.basic_publish(exchange='',routing_key='rabbitmessage',body=message)
                connection.close()

	        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register("example.greeting", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
