import pika
import logging
f=open("imdb.json","rb")
i=f.read()

logging.basicConfig()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',routing_key='hello',body=i)
print " [x] Sent 'jsonpayload'"
connection.close()
