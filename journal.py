import os
from datetime import datetime
import json
import encryption
from encryption import Cryptography

cwd = os.getcwd()
encryption_obj = Cryptography()

def num_entries(path):
        with open(path, 'r') as f:
            num = len(f.readlines())
            return num

class Journal:

    def __init__(self, uname):
        self.dir = cwd + '/' + 'journals/' + uname + '/' + uname + '.txt' 
        self.num = num_entries(self.dir)


    def write_entry(self, text):
        if self.num <= 50:
            timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S%p")
            data = timestamp + '-' + text 
            e_entry = encryption_obj.encrypt(data)
            with open(self.dir, 'a') as f:
                f.write(str(e_entry)+"\n")
        else:
            timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S%p")
            data = timestamp + '-' + text 
            e_entry = encryption_obj.encrypt(data)
            #first append the new entry and then remove the first one
            with open(self.dir, 'a') as f:
                f.write(str(e_entry)+"\n")
            with open(self.dir, 'r+') as f:
                f.readline()
                data = f.read() #read the rest
                f.seek(0) #set the cursor to the top of the file
                f.write(data) #write the data back
                f.truncate() #set the file size to the current size        

    def read_journal(self):
        with open(self.dir, 'r') as f:        
            lines = f.readlines()
            decrp_entries = []
            for line in list(lines):
                decrp_entries.append(encryption_obj.decrypt(line))    

        return decrp_entries     
               
