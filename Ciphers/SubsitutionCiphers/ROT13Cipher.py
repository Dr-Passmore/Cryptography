import logging
import string
from main import CipherTool

class ROT13Cipher:
    def __init__(self, text):
        logging.info('ROT13 Cipher has been initialised')
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        output = ROT13Cipher.encrypt(self, text, lowercase, uppercase)
        ROT13Cipher.output(output)
    
    def encrypt (self, text, lowercase, uppercase):
        output = []
        for letter in text:
            if letter in lowercase:
                index = lowercase.index(letter)
                encrypt = (index + 13) %26
                newletter = lowercase[encrypt]
                output.append(newletter)
            elif letter in uppercase:
                index = uppercase.index(letter)
                encrypt = (index + 13) % 26
                newletter = uppercase[encrypt]
                output.append(newletter)
            else:
                output.append(letter)
        
        output = ''.join(map(str, output))
        return output
    
    def output(output):
        CipherTool.returnOutput(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

