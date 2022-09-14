
import logging
class thisisatest:
    def check():
        check = 5
        return check

class ROT13Cipher:
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

ROT13Cipher()