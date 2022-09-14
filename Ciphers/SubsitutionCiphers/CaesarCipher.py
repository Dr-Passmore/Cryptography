import logging


class caesarCipher:
    def __init__(self):
        logging.info('ROT13 Cipher has been initialised')
        # set up lowercase and upper case alphabets (use self.)
        
    
    def encrypt (self, text, step):
        output = []
        
        #add logging
        
        #loop per letter
        
        # index
        
        #encrypt (index + step)
        
        #newletter
        
        #append letter to output
        
        encryptedText = ''.join(map(str, output))
        return encryptedText
    
    def decrypt (self, text, step):
        output = []
        
        #add logging
        
        #loop per letter
        
        # index
        
        #encrypt (index - step)
        
        #newletter
        
        #append letter to output
        
        decryptedText = ''.join(map(str, output))
        return decryptedText
    
        return output

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

caesarCipher()