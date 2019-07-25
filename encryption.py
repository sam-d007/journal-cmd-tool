from cryptography.fernet import Fernet


def read_key():
        file = open('key.key', 'rb')
        key = file.read()
        file.close()
        return key

class Cryptography:
    def __init__(self):
        #Read Key
        # self.text = text
        self.key = read_key()  
        self.f = Fernet(self.key)

    @staticmethod
    def generate_key():
        key = Fernet.generate_key() 
        file = open('key.key', 'wb')
        file.write(key)
        file.close()  
    
    def encrypt(self, msg):
        e_msg = self.f.encrypt(msg.encode())
        return e_msg.decode()

    def decrypt(self, e_msg):
        d_msg = self.f.decrypt(e_msg.encode())
        return d_msg.decode()