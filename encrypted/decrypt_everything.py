import os
from cryptography.fernet import Fernet as f
from tqdm import tqdm
files=[]
for file in os.listdir():
   if file=="encrypt_everything.py" or file=="thekey.key" or file=="decrypt_everything.py":
      continue
   if os.path.isfile(file):
      files.append(file)

with open("thekey.key",'rb') as thekey:
   secret_key=thekey.read()




for file in files:
   with open(file,'rb') as thefile:
      contents=thefile.read()
   contents_decrypt=f(secret_key).decrypt(contents)
   with tqdm.wrapattr(open(file,'wb'), "write", total=len(contents_decrypt),desc=file,colour="green") as r_raw:
      r_raw.write(contents_decrypt)
   print('\n')
#print(f'[+]{file} is decrypted...')