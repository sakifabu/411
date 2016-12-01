import pysftp as sftp

def sftpexample():
	try:
		s=pysftp.Connection(host='localhost',username='sakif',password='123456')

		remotepath='/home/sakif/stuff'
		localpath='home/sakif/imdb.json'
		s.put(localpath,remotepath)
		s.close
	except Exception, e:
		print str (e)
sftpexample ()
'''

with pysftp.Connection(hostname='10.0.2.15',username='sakif',password='123456') as sftp :
	with sftp.put('/home/sakif/imdb.json','/home/sakif/stuff')

#10.0.2.15'''
