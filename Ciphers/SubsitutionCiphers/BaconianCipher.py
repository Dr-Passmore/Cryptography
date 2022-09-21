import logging
import cryptography

class BaconianCipher:
    def __init__(self, text, encrypt, letters):
        logging.info('Baconian Cipher has been initialised')
        self.letterCipher = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 
                             'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 
                             'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 
                             'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 
                             'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 
                             'Z': 'bbaab'}
        self.binaryCipher = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 
                             'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001', 
                             'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110', 
                             'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 
                             'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 
                             'Z': '11001'}
        text = text.upper()
        
        if encrypt == True:
            output = BaconianCipher.encrypt(self, text, letters)
        else:
            output = BaconianCipher.decrypt(self, text, letters)
        
        BaconianCipher.output(output)
        
    def encrypt(self, text, letter):
        logging.info('Encrypting text')
        
    def decrypt(self, text, letter):
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