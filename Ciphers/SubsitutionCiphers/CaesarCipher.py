import logging


class caesarCipher:
    def __init__(self):
        logging.info('ROT13 Cipher has been initialised')
    
    def encrypt (self, text):
        output = []
        return output
    
    def decrypt (self, text):
        output = []
        return output

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

caesarCipher()