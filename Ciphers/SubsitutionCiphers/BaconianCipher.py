import logging
import cryptography

class BaconianCipher:
    def __init__(self, text, encrypt, letters):
        logging.info('Baconian Cipher has been initialised')
        
    def encrypt(self, text):
        logging.info('Encrypting text')
        
    def decrypt(self, text):
        logging.info('Decrypting text')
        
    def output(output):
        sample = output[0:30]
        logging.info('Returning message: {}...'.format(sample))
        cryptography.CipherTool.returnOutput(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')