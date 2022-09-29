import string
import logging
import cryptography

class ROT18Cipher:
    def __init__(self, text):
        logging.info('ROT18 Cipher Selected')
        #ROT5 shifts numbers by 5 - 1 becomes 6, 9 becomes 4 and shifts letters by 13
        
    def encrypt(self, text):
        logging.info('Encrypting')
    
    def decrypt(self, text):
        logging.info('Decrypting')
        
    def output(output):
        sample = output[0:30]
        logging.info('Returning message: {}...'.format(sample))
        cryptography.CipherTool.returnOutput(output)
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
text = "The answer to life, the universe, and everything is 42"
ROT18Cipher(text)