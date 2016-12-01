import pika,Pyro4 ,urllib, urllib2
from Crypto.Cipher import AES

#pyro4



#rabbitmq
title='frozen'
url = 'http://omdbapi.com/?'
param = {'t':title,'y':'','plot':'short','r':'json'}
value = urllib.urlencode(param)
response = urllib2.urlopen(url+value)
payload = response.read()

aesObj  = AES.new('public key', AES.MODE_CBC, 'This is an IV456')
message = aesObj.decrypt(payload)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rabbitmessage')

channel.basic_publish(exchange='',routing_key='rabbitmessage',body=message)
connection.close()
