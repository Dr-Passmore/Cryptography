from lib2to3.pgen2.token import NEWLINE
import logging
import string
import cryptography

class VigenèreCipher:
    def __init__(self, key, text, encrypt):
        logging.info("The Vigenère Cipher has been initialised")
        key = key.lower()
        self.lowercase = list(string.ascii_lowercase)
        self.uppercase = list(string.ascii_uppercase)
        key = VigenèreCipher.keyProcessing(self, key)
        if key == None:
            output = "Error - No key provided. The Vigenère Cipher requires letters"
            VigenèreCipher.output(output)
        else:
            if encrypt == True:
                output = VigenèreCipher.encrypt(self, key, text)
            else:
                output = VigenèreCipher.decrypt(self, key, text)
            
            output = ''.join(map(str, output))
            print(output)
        
    def keyProcessing(self, key):
        logging.info("Processing the key")
        key = list(key)
        updatedkey = []
        for letter in key:
            if letter in self.lowercase:
                updatedkey.append(letter)
            else:
                continue
        key = updatedkey
        if key == []:
            logging.error("No key provided")
        else:    
            return key

    def encrypt(self, key, text):
        logging.info("Encrypting")
        output = []
        char = 0
        keycount = 0
        while True:
            if (char < len(text)):
                for letter in text:
                    char += 1
                    if letter in self.lowercase:
                        keyLetter = self.lowercase.index(key[keycount])
                        index = self.lowercase.index(letter)
                        keyLetter += 1
                        encrypt = (index + keyLetter) %26
                        newLetter = self.lowercase[encrypt]
                        output.append(newLetter)
                        keycount += 1
                        if keycount == len(key):
                            keycount = 0
                    elif letter in self.uppercase:
                        keyLetter = self.lowercase.index(key[keycount])
                        index = self.uppercase.index(letter)
                        keyLetter += 1
                        encrypt = (index + keyLetter) % 26
                        newLetter = self.uppercase[encrypt]
                        output.append(newLetter)
                        keycount += 1
                        if keycount == len(key):
                            keycount = 0
                    else:
                        output.append(letter)
            else:
                break
        return output
        
    def decrypt(self, key, text):
        logging.info("Decrypting")
        output = []
        char = 0
        keycount = 0
        while True:
            if (char < len(text)):
                for letter in text:
                    char += 1
                    if letter in self.lowercase:
                        keyLetter = self.lowercase.index(key[keycount])
                        index = self.lowercase.index(letter)
                        keyLetter += 1
                        encrypt = (index - keyLetter) %26
                        newLetter = self.lowercase[encrypt]
                        output.append(newLetter)
                        keycount += 1
                        if keycount == len(key):
                            keycount = 0
                    elif letter in self.uppercase:
                        keyLetter = self.lowercase.index(key[keycount])
                        index = self.uppercase.index(letter)
                        keyLetter += 1
                        encrypt = (index - keyLetter) % 26
                        newLetter = self.uppercase[encrypt]
                        output.append(newLetter)
                        keycount += 1
                        if keycount == len(key):
                            keycount = 0
                    else:
                        output.append(letter)
            else:
                break
        return output
                        
    def output(output):
        sample = output[0:30]
        logging.info('Returning message: {}...'.format(sample))
        cryptography.CipherTool.returnOutput(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

encrypt = False
text = "This is a test. Hopefully works!234"
text = "Uvpk hu f uwiu. Ehqsmmknd xghlp!234"
key = "angry!! bear!!!!12345 paws"

VigenèreCipher(key, text, encrypt)