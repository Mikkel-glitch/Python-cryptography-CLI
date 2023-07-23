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

    def hash_single (self, singleInput):
        hashedSingle = hashlib.sha512(singleInput.encode(), usedforsecurity=True).hexdigest()
        return hashedSingle

    def hash_default (self, defaultInput, numberOfIterations=10):
        for _ in range(numberOfIterations):
            hashedDefault = hashlib.sha512(defaultInput.encode(), usedforsecurity=True).hexdigest()
        return hashedDefault

    def hash_custom (self, customInput, numberOfIterations=None):
        if numberOfIterations == None:
            numberOfIterations = 20
            for _ in range(numberOfIterations):
                hashedCustom = hashlib.sha512(customInput.encode(), usedforsecurity=True).hexdigest()
            return hashedCustom
        else:
            convertedNumberIteration = int(numberOfIterations)
            for _ in range(convertedNumberIteration):
                hashedCustom = hashlib.sha512(customInput.encode(), usedforsecurity=True).hexdigest()
            return hashedCustom

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
        print("Decrypting:\n [D1] Decrypt single file\n [D2] Decrypt multiple files\n ")
        option = input(">> ")

        try:
            if option.upper() == "H1":
                print("\n[S1] SHA-256 OR [S2] SHA-512\n")
                hashOption = input(">> ")
                try:
                    if hashOption.upper() == "S1":
                        hash256Input = input(">> ")
                        hash256Value = SHA256.hash_single(hash256Input)
                        print("Hash value: {}".format(hash256Value))
                    elif hashOption.upper() == "S2":
                        hash512Input = input(">> ")
                        hash512Value = SHA512.hash_single(hash512Input)
                        print("Hash value: {}".format(hash512Value))
                    else:
                        raise ValueError("Unrecognized command")
                except ValueError as valErrorOne:
                    print("Error: {}".format(valErrorOne))
                    hashOption = input(">> ")
            elif option.upper() == "H2":
                print("\n[S1] SHA-256 OR [S2] SHA-512\n")
                hashOptionTwo = input(">> ")
                try:
                    if hashOptionTwo.upper() == "S1":
                        hash256InputTwo = input(">> ")
                        hash256ValueTwo = SHA256.default_hash(hash256InputTwo)
                        print("Hash value: {}".format(hash256ValueTwo))
                    elif hashOptionTwo.upper() == "S2":
                        hash512InputTwo = input(">> ")
                        hash512ValueTwo = SHA512.hash_default(hash512InputTwo)
                        print("Hash value: {}".format(hash512ValueTwo))
                    else:
                        raise ValueError("Unrecognized option")
                except ValueError as valErrorTwo:
                    print("Error: {}".format(valErrorTwo))
                    hashOptionTwo = input(">> ")
            elif option.upper() == "H3":
                print("\n[S1] SHA-256 OR [S2] SHA-512\n")
                hashOptionThree = input(">> ")
                try:
                    if hashOptionThree.upper() == "S1":
                        hash256InputThree = input(">> ")
                        hashThreeIteration = input(">> ")
                        hash256ValueThree = SHA256.custom_hash(hash256InputThree, hashThreeIteration)
                        print("Hash value: {}".format(hash256ValueThree))
                    elif hashOptionThree.upper() == "S2":
                        hash512InputThree = input(">> ")
                        hashThreeIteration = input(">> ")
                        hash512ValueThree = SHA512.hash_custom(hash512InputThree, hashThreeIteration)
                        print("Hash value: {}".format(hash512ValueThree))
                except ValueError as valErrorThree:
                    print("Error: {}".format(valErrorThree))
                    hashOptionThree = input(">> ")
            else:
                raise ValueError("Unrecognized command")
        except ValueError as valError:
            print("Error: {}".format(valError))
            main_function()

main_function()

#TODO: Continue the md file
#TODO: Code the Encrypt and Decrypt class
