from cryptography.fernet import Fernet


def createKey():
    return Fernet.generate_key()

class Crypt:

    def __init__(self,key):
        self.cipher = Fernet(key)

    def encrypt(self, string:str):
        crypt = self.cipher.encrypt(string.encode())
        return crypt

    def decrypt(self, crypt):
        ans = self.cipher.decrypt(crypt).decode()
        return ans

key = createKey()
en = Crypt(key)
