import logging
import string
import cryptography

class ROT13Cipher:
    def __init__(self, text, encrypt):
        logging.info('ROT13 Cipher has been initialised')
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        output = ROT13Cipher.encrypt(self, text, lowercase, uppercase, encrypt)
        ROT13Cipher.output(output)
    
    def encrypt (self, text, lowercase, uppercase, encrypt):
        if encrypt == True:
            logging.info('Encrypting message')
        else:
            logging.info('Decrypting message')
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
        logging.info('Returning message')
        cryptography.CipherTool.returnOutput(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

