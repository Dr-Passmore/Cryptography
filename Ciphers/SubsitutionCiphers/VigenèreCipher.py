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
        if key == None:
            output = "Error - No key provided. The Vigenère Cipher requires letters"
            VigenèreCipher.output(output)
        else:
            if encrypt == True:
                output = VigenèreCipher.encrypt(self, key, text)
            else:
                output = VigenèreCipher.decrypt(self, key, text)
            
            print(key)
        
    def keyProcessing(self, key):
        logging.info("Processing the key")
        key = list(key)
        updatedkey = []
        for letter in key:
            if letter in self.lowercase:
                updatedkey.append(letter)
            else:
                continue
        key = updatedkey
        if key == []:
            logging.error("No key provided")
        else:    
            return key

    def encrypt(self, key, text):
        logging.info("Encrypting")
        
    def decrypt(self, key, text):
        logging.info("Decrypting")
        
    def output(output):
        sample = output[0:30]
        logging.info('Returning message: {}...'.format(sample))
        cryptography.CipherTool.returnOutput(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

encrypt = True
text = "This is a test"
key = "angry!! bear!!!!12345 paws"

VigenèreCipher(key, text, encrypt)