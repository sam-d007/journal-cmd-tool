from fileop import FileOp
from login import  login
from encryption import Cryptography

crypto = Cryptography()
file_obj = FileOp()


class Signup:
    def __int__(self):
        self.num_users = check_num_users()
            
    def sign_up(self):
        if self.num_users <= 10:
            return 1
            #write_user(1)
        else:
            print("\nMaximum account registration limit reached! Please Login. \n")    
            return 0
            # write_user(2)

            
def check_num_users():
    return len(file_obj.readFile())











          

