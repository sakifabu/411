import pika
from Crypto.Cipher import AES




#receive message from node3 via pyro




#decompress CRC file




#encrypt payload with AES
obj = AES.new('key', AES.MODE_CBC, 'This is an IV456')
ciphertext = obj.encrypt(message)


#send the encrypted message to node1 via rabbitmq
ciphertext = "blahblahblah"


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='rabbitmessage')


channel.basic_publish(exchange='',
                      routing_key='rabbitmessage',
                      body=ciphertext)
print(" Sent message ")
connection.close()

