import logging
import string
import cryptography

class VigenèreCipher:
    def __init__(self, key, text, encrypt):
        logging.info("The Vigenère Cipher has been initialised")
        key = key.lower()
        self.lowercase = list(string.ascii_letters)
        self.uppercase = list(string.ascii_uppercase)
        key = VigenèreCipher.keyProcessing(self, key)
        
        if encrypt == True:
            output = VigenèreCipher.encrypt(self, key, text)
        else:
            output = VigenèreCipher.decrypt(self, key, text)
            
        print(output)
        
    def keyProcessing(self, key):
        logging.info("Processing the key")

    def encrypt(self, key, text):
        logging.info("Encrypting")
        
    def decrypt(self, key, text):
        logging.info("Decrypting")

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')