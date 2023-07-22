import hashlib
from cryptography.fernet import Fernet
import os as operating_system

class Hash256:

    def hash_single (self, singleInput):
        hashedSingle256 = hashlib.sha256(singleInput.encode(), usedforsecurity=True).hexdigest()
        return hashedSingle256

    def default_hash (self, defaultInput, numberOfIter=10):
        pass

    def custom_hash (self, customInput, numberOfIter=20):
        pass

#TODO: Continue the hasher. Continue default hash

class Hash512:

    def hash_single (self):
        pass

    def hash_default (self):
        pass

    def hash_custom (self):
        pass

class Encrypt:

    def encrypt_single (self):
        pass

    def encrypt_multiple (self):
        pass

class Decrypt:

    def decrypt_single (self):
        pass

    def decrypt_multiple (self):
        pass

def main_function ():

    SHA256 = Hash256()
    SHA512 = Hash512()
    ENCRYPT = Encrypt()
    DECRYPT = Decrypt()

    while True:
        print("========== HASHING CLI ==========")
        print("========== INPUT OPTION ==========\n")
        print("Hashing:\n [H1] Single hash\n [H2] Default hash\n [H3] Custom hash\n")
        print("Encrypting:\n [E1] Encrypt single file\n [E2] Encrypt multiple files\n")
        option = input(">> ")

        try:
            if option.upper() == "H1":
                hashInput = input(">> ")
                hashValue = SHA256.hash_single(hashInput)
                print("Hash value: {}".format(hashValue))
        except:
            pass

main_function()

#TODO: Continue
