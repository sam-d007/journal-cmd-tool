import pickle
import json
from encryption import Cryptography
from journal import Journal

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


global auth
auth = int(input("Please enter 1 for login and 2 for Sign-Up"))
crypto = Cryptography()
file_obj = FileOp()

def login(u_name, password):
    user_details = file_obj.readFile()
    print("Received Password")
    print(password)
    rec_password = crypto.decrypt(password)
    print("Decrypted Password")
    print(rec_password)
    print(type(password))
    for user in user_details:
        # if user["uname"] == u_name and user["password"] == password:
            f_uname = user['uname']
            f_pass = user["password"]
            f_pass = crypto.decrypt(f_pass)
            if f_uname==u_name and f_pass==rec_password:
                print("Authentication Successful!")
                list_or_create = int(input("\n Press 1 for listing previous entries \n Press 2 for creating new entry \n"))
                if list_or_create == 1:
                    print("list codde")
                    journal_obj = Journal(u_name)
                    entries = journal_obj.read_journal()  
                    print("entries are ", entries)
                    
                elif list_or_create == 2:
                    print("create code")
                    j_entry = str(input("\n Write an entry for the journal"))
                    journal_obj = Journal(u_name)
                    journal_obj.write_entry(j_entry)        
                    print("entry written")
                else:
                    print("invalid input")                
                break

            # if d_pass == rec_password:
            #     print("Password Correct")
            # else:
            #     # print("rec",u_name,password)
            #     # print("file",user["uname"],user["password"])
            #     print("wrong password") 

if int(auth)==1:
    print("Write login logic")
    u_name = str(input("enter user name"))
    password = str(input("enter password"))
    e_pass = crypto.encrypt(password)
    login(u_name,e_pass)

elif int(auth)==2:
    print("Write Sign Up logic") 
    u_name = str(input("enter user name"))   
    password = str(input("enter password"))   
    details = {}
    details['uname'] = u_name
    #encrypting the password
    e_pass = crypto.encrypt(password)
    details['password'] = e_pass
    # details = json.dumps(details)
    file_obj.writeFile(details) #write user details to file
    file_obj.readFile()     #read details from file   
             
    # pickle_in = open("text.txt","rb")
    # example_dict = pickle.load(pickle_in)    
    # print(example_dict)    
    # print(type(example_dict))    

elif int(auth) == 123:
    try:
        crypto.generate_key()
        print("key written")
    except:
        print("error in generating key")    

elif int(auth) == 3:
    # try:
    e_msg = crypto.encrypt("123")    
    print(e_msg)
    # except:
    #     print("could not be encrypted")    

elif int(auth) == 4:
    user_details = file_obj.readFile()
    for user in user_details:
        print(user['uname'])
        print(user['password'])
        break
    print(user_details)

else:
    print("please enter correct input")
    while True:
        auth = input("Please enter 1 for login and 2 for Sign-Up")
        
   

# lines = f.readlines()
# for line in lines:
#     print(line.rstrip())        