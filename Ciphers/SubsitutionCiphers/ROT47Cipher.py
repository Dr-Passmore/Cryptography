from re import ASCII
import string
import logging
import cryptography

class ROT47Cipher:
    def __init__(self, text, encrypt):
        #Encodes all ASCII visible letters (Character 33 '!' to 126 '~') and shifts them by an index change of 47
        #"This is a test!" becomes "%9:D :D 2 E6DEP" 
        logging.info('ROT47 Cipher has been initialised')
        self.ASCII = []
        for character in range(33,127):
            letter = chr(character)
            self.ASCII.append(letter)
        if encrypt == True:
            output = ROT47Cipher.encrypt(self, text)
        else:
            output = ROT47Cipher.decrypt(self, text)
        print
        output = ''.join(map(str, output))
        print(output)
        
    def encrypt (self, text):
        logging.info('encrypt')
        output = []
        for letter in text:
            if letter in self.ASCII:
                index = self.ASCII.index(letter)
                encrypt = (index + 47) % 94
                newletter = self.ASCII[encrypt]
                output.append(newletter)
            else:
                output.append(letter)
        return output
        
    def decrypt (self, text):
        logging.info('decrypt')
        output = []
        for letter in text:
            if letter in  self.ASCII:
                index = self.ASCII.index(letter)
                decrypt = (index - 47) % 94
                newletter= self.ASCII[decrypt]
                output.append(newletter)
            else:
                output.append(letter)
        return output
        
    def output(output):
        logging.info('Returning message')
        cryptography.CipherTool.returnOutput(output)
        
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

text = "Needs to be 20% cooler"
encrypt = True

ROT47Cipher(text, encrypt)

text = "}665D E@ 36 a_T 4@@=6C"
encrypt = False
ROT47Cipher(text, encrypt)