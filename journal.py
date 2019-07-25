import os
from datetime import datetime
import json

cwd = os.getcwd()

class Journal:
    def __init__(self, uname):
        self.dir = cwd + '/' + 'journals/' + uname + '/' + uname + '.txt' 

    def write_entry(self, text):
        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S%p")
        data = timestamp + '-' + text 
        with open(self.dir, 'a') as f:
            f.write(str(data)+"\n")

    def read_journal(self):
        with open(self.dir, 'r') as f:        
            lines = f.readlines()
        return list(lines)            
               
