import logging
import string

class caesarCipher:
    def __init__(self, text, step):
        logging.info('Caesar Cipher has been initialised')
        # set up lowercase and upper case alphabets (use self.)
        self.uppercase = list(string.ascii_uppercase)
        self.lowercase = list(string.ascii_lowercase)
        encryptedtext = caesarCipher.encrypt(self,text,step)
        print(encryptedtext)

        # add check whether encrypt or decrypt
    
    def encrypt (self, text, step):
        output = []
        
        #add logging
        logging.info('Caesar Cipher encryption has commenced using a step of {}'.format(step))
        #loop per letter
        for letter in text:
            if letter in self.uppercase:
                # index
                index = self.uppercase.index(letter)
                #encrypt (index + step)
                encrypt = (index + step)%26
                #newletter
                newletter = self.uppercase[encrypt]
                #append letter to output
                output.append(newletter)
            elif letter in self.lowercase:
                # index
                index = self.lowercase.index(letter)
                #encrypt (index + step)
                encrypt = (index + step)%26
                #newletter
                newletter = self.lowercase[encrypt]
                #append letter to output
                output.append(newletter)
            else:
                #append letter to output
                output.append(letter)      
        
        
        
        
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


text = 'This is a test'
step = 6
caesarCipher(text,step)