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
            
        print(key)
        
    def keyProcessing(self, key):
        logging.info("Processing the key")
        key = list(key)
        i = 0
        for letter in key:
            if key[i] not in self.lowercase:
                del key[i]
            i += 1
        return key

    def encrypt(self, key, text):
        logging.info("Encrypting")
        
    def decrypt(self, key, text):
        logging.info("Decrypting")

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

encrypt = True
text = "This is a test"
key = "Test!"
VigenèreCipher(key, text, encrypt)