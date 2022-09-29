import string
import logging
import cryptography

class RailFenceCipher:
    def __init__(self, text):
        logging.info('Rail-Fence Cipher Selected')
        #In the rail fence cipher, the plaintext is written downwards diagonally on successive "rails" of an imaginary fence, 
        #then moving up when the bottom rail is reached, down again when the top rail is reached, and so on until the whole plaintext is written out. 
        #The ciphertext is then read off in rows. 
        #test becomes 'tets' 
        #t
        # e t
        #  s
        
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
text = "test"
RailFenceCipher(text)