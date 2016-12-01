import pysftp ,hashlib, Pyro4
#pyro4 stuff

#pysftp
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
