import logging
import cryptography

class ROT47Cipher:
    def __init__(self, text, encrypt):
        #Encodes all ASCII visible letters (Character 33 '!' to 126 '~') and shifts them by an index change of 47
        #"This is a test!" becomes "%9:D :D 2 E6DEP" 
        logging.info('ROT47 Cipher has been initialised')
        #Creates list of characters
        self.ASCII = []
        for character in range(33,127):
            letter = chr(character)
            self.ASCII.append(letter)
        #if encrypt is true run encrypt function
        if encrypt == True:
            output = ROT47Cipher.encrypt(self, text)
        #else run decrypt
        else:
            output = ROT47Cipher.decrypt(self, text)
        
        #converts output from list to string
        output = ''.join(map(str, output))
        #sends string to output function
        ROT47Cipher.output(output)
        
        
    def encrypt (self, text):
        logging.info('Encrypting text')
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
        logging.info('Decrypting text')
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
        sample = output[0:30]
        logging.info('Returning message: {}...'.format(sample))
        cryptography.CipherTool.returnOutput(output)
        
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

