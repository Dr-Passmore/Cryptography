import string
import logging
#import cryptography

class atbashCipher:
    def __init__(self, text):
        #Mirrored alphabet A = Z, Y = B. Dictionary approach would work well
        lowercase = list(string.ascii_lowercase)
        lowercaseReverse = list(string.ascii_lowercase)
        lowercaseReverse.reverse()
        lowercaseDictionary = dict(zip(lowercase, lowercaseReverse))
        #print(lowercaseDictionary)
        uppercase = list(string.ascii_uppercase)
        uppercaseReverse = list(string.ascii_uppercase)
        uppercaseReverse.reverse()
        uppercaseDictionary = dict(zip(uppercase, uppercaseReverse))

        self.combinedDictionary = lowercaseDictionary.copy()
        self.combinedDictionary.update(uppercaseDictionary)
        
        #print(combinedDictionary)
        
        logging.info('Atbash Cipher has been initialised')
        output = atbashCipher.encrypt(self, text)
        output = ''.join(map(str, output))
        print(output)
        
    def encrypt (self, text):
        output = []
        logging.info('encrypt')
        #only requires one. A IF statement using encyrpt True or False can be used to update logging info
        for letter in text:
            if letter in self.combinedDictionary:
                newletter = self.combinedDictionary[letter]
                output.append(newletter)
            else:
                output.append(letter)
        return output
        
    def output(output):
        logging.info('Returning message')
        #cryptography.CipherTool.returnOutput(output)
        
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

text = 'supercalifragilistic'
encrypt = True
atbashCipher(text)