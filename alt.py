import hashlib
from cryptography.fernet import Fernet
import os as operating_system

class Hash256:

    def hash_single (self, singleInput):
        hashedSingle256 = hashlib.sha256(singleInput.encode(), usedforsecurity=True).hexdigest()
        return hashedSingle256

    def default_hash (self, defaultInput, numberOfIterations=10):
        for _ in range(numberOfIterations):
            hashedDefault256 = hashlib.sha256(defaultInput.encode(), usedforsecurity=True).hexdigest()

            return hashedDefault256

    def custom_hash (self, customInput, numberOfIterations=None):
        if numberOfIterations == None:
            numberOfIterations = 20
            for _ in range(numberOfIterations):
                hashedCustom256 = hashlib.sha256(customInput.encode(), usedforsecurity=True).hexdigest()
                return hashedCustom256
        else:
            convertedNumberIterations = int(numberOfIterations)
            for _ in range(convertedNumberIterations):
                hashedCustom256 = hashlib.sha256(customInput.encode(), usedforsecurity=True).hexdigest()
            return hashedCustom256

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
            elif option.upper() == "H2":
                hashTwoInput = input(">> ")
                hashTwoValue = SHA256.default_hash(hashTwoInput)
                print("Hash value: {}".format(hashTwoValue))
            elif option.upper() == "H3":
                hashThreeInput = input(">> ")
                hashThreeIterations = input(">> ")
                hashThreeValue = SHA256.custom_hash(hashThreeInput, hashThreeIterations)
                print("Hash value: {}".format(hashThreeValue))
        except ValueError as valError:
            print("Error: {}".format(valError))
            main_function()

main_function()

#TODO: Continue
