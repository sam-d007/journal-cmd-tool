from fileop import FileOp
from encryption import Cryptography
from journal import Journal
import json
# from signup import Signup

def check_num_users():
    print("!!!!!!!!!!!!!!!!!!!!!")
    return len(file_obj.readFile())

class Signup:
    def __init__(self):
        print("@@@@@@@@@@@@@@")
        self.num_users = check_num_users()
            
    def sign_up(self):
        if self.num_users <= 10:
            return 1
            #write_user(1)
        else:
            print("\nMaximum account registration limit reached! Please Login. \n")    
            return 0
            # write_user(2)

    def check_username(self, uname):
        user_details = file_obj.readFile()
        for user in user_details:
                f_uname = user['uname']
                if f_uname==uname:
                    print("User already exists!")
                    return json.loads('{"exists":"1"}')
                else:
                    return json.loads('{"exists":"0"}') 

            

crypto = Cryptography()
file_obj = FileOp()
signup_obj = Signup()


def user_details():
     u_name = str(input("enter user name"))   
     password = str(input("enter password"))

     return u_name, password

def log():
    auth = input("Please enter 1 for login \n")

    try:
        auth = int(auth)
    except:
        print("Invalid input write again")
        log()

    if int(auth)==1:
        u_name = str(input("enter user name\n"))
        password = str(input("enter password\n"))
        e_pass = crypto.encrypt(password)
        login(u_name,e_pass)
    else:
        print("please enter correct input\n")
        log()

def write_user(can_write):
    if int(can_write) == 1:
        u_name, password = user_details()
        user_exists = signup_obj.check_username(u_name)
        if user_exists['exists'] == '0':
            details = {}
            details['uname'] = u_name
            #encrypting the password
            e_pass = crypto.encrypt(password)
            details['password'] = e_pass
            # details = json.dumps(details)
            file_obj.writeFile(details) #write user details to file
            file_obj.readFile()     #read details from file   
            file_obj.create_dir(u_name)
            print("\n User created Please login \n")
            u_name = str(input("enter user name\n"))
            password = str(input("enter password\n"))
            e_pass = crypto.encrypt(password)
            login(u_name,e_pass)
        else:
            print("\n user name already exists \n")
            login_new()        
    else:
        print("Max account registration limit reached. Please login.")
        log()


def login_new():
    auth = input( "Please enter : \n 1 for "+ "\x1b[3;37;42m login \x1b[0m" +"\n 2 for \x1b[3;37;44m Sign-Up \x1b[0m" + "\n 5 for \x1b[3;37;41m Exit \x1b[0m \n" )

    try:
        auth = int(auth)
    except:
        print("Invalid input write again")
        login_new()

    if int(auth)==1:
        print("Write login logic")
        u_name = str(input("enter user name"))
        password = str(input("enter password"))
        e_pass = crypto.encrypt(password)
        login(u_name,e_pass)

    elif int(auth)==2:
        print("Write Sign Up logic") 
        can_write = signup_obj.sign_up()
        write_user(can_write)
        # u_name = str(input("enter user name"))   
        # password = str(input("enter password"))   
        # details = {}
        # details['uname'] = u_name
        # #encrypting the password
        # e_pass = crypto.encrypt(password)
        # details['password'] = e_pass
        # # details = json.dumps(details)
        # file_obj.writeFile(details) #write user details to file
        # file_obj.readFile()     #read details from file   
        # file_obj.create_dir(u_name)
        # print("User created Please login")
        # login_new()         
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
    
    elif int(auth) == 5:
        print("Goodbye!")
        return 1

    elif int(auth) == 4:
        user_details = file_obj.readFile()
        for user in user_details:
            print(user['uname'])
            print(user['password'])
            break
        print(user_details)

    else:
        print("please enter correct input")
        login_new()


def login(u_name, password):
    user_details = file_obj.readFile()
    print("Received Password")
    print(password)
    rec_password = crypto.decrypt(password)
    print("Decrypted Password")
    print(rec_password)
    print(type(password))
    journal_flow = 0
    for user in user_details:
        # if user["uname"] == u_name and user["password"] == password:
            f_uname = user['uname']
            f_pass = user["password"]
            f_pass = crypto.decrypt(f_pass)
            if f_uname==u_name and f_pass==rec_password:
                print("Authentication Successful!")
                journal_flow = 1
                break
    if journal_flow == 0:
        print("login failed")
        login_new()
    else:
        while journal_flow == 1:
            list_or_create = int(input("\n Press 1 for listing previous entries \n Press 2 for creating new entry \n Press 3 to login as new User \n Press 5 to exit application \n"))
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
                
            elif list_or_create == 3:
                journal_flow = 0
                login_new()

            elif list_or_create == 5:
                break

            else:
                journal_flow = 1
                print("invalid input")