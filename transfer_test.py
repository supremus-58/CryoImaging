"""
import os
import paramiko

ssh = paramiko.SSHClient() 
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect('192.168.1.37', username='sshd', password='Toshiba12')
sftp = ssh.open_sftp()
sftp.put('/home/pi/Desktop/full_size.jpg', '/mnt/HD/HD_a2/testRuns')
sftp.close()
ssh.close()



"""

import os
import paramiko
import scp
import datetime

a = datetime.datetime.now()
print a

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


ssh = createSSHClient('192.168.1.37', 22, 'sshd', 'Toshiba12')
putter = scp.SCPClient(ssh.get_transport())

putter.put('/home/pi/Desktop/som_code', '/mnt/HD/HD_a2/testRuns')

b = datetime.datetime.now()
print b
c = b-a
print c
