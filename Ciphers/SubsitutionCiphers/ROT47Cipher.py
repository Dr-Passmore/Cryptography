import string
import logging
import cryptography

class ROT47Cipher:
    def __init__(self, text, encrypt):
        #Encodes all ASCII visible letters (Character 33 '!' to 126 '~') and shifts them by an index change of 47
        #"This is a test!" becomes "%9:D :D 2 E6DEP" 
        logging.info('ROT47 Cipher has been initialised')
        
    def encrypt (text, encrypt):
        logging.info('encrypt')
        
    def decrypt (text, encrypt):
        logging.info('decrypt')
        
    def output(output):
        logging.info('Returning message')
        cryptography.CipherTool.returnOutput(output)
        
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')