import json
import os

class FileOp:
    @staticmethod
    def readFile():
        arr_file = []
        with open('text.txt', 'r') as f:        
            lines = f.readlines()
            for line in lines:
                arr_file.append(json.loads(line))
        return arr_file        

    @staticmethod
    def writeFile(text):
        text = json.dumps(text)
        with open('text.txt', 'a') as f:
            f.write(str(text)+"\n")

    @staticmethod
    def create_dir(u_name):
        path = 'journals/'+u_name
        if not os.path.exists(path):
            os.makedirs(path)
            filename = path + '/' + u_name + '.txt'
            open(filename, 'w').close()
            print("Directory/File " , path ,  " Created ")
        else:    
            print("Directory " , path ,  " already exists")   