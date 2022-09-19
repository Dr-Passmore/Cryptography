import string
import logging
import cryptography

class AffineCipher:
    def __init__(self, text, encrypt):
        #Possible values of A - 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25
        #http://practicalcryptography.com/ciphers/
        #https://www.dcode.fr
        #B can be arbitrary as long as a does not equal 1 since this is the shift of the cipher
        logging.info('Affine Cipher has been initialised')
        uppercase = list(string.ascii_uppercase)
        lowercase = list(string.ascii_lowercase)
        key = [5, 8]
        
        output = AffineCipher.encrypt(key, text, uppercase, lowercase)
        output = ''.join(map(str, output))
        print (output)
        text = output
        output = AffineCipher.decrypt(key, text, uppercase, lowercase)
        output = ''.join(map(str, output))
        print (output)
        
    def encrypt (key, text, uppercase, lowercase):
        #only requires one. A IF statement using encyrpt True or False can be used to update logging info
        
        #encrypt calulation A x Letter index (if A is 5 and letter is C then (5 X 2)) Then plus B, if B was 8, (5 X 2)+8. Finally % by 26. The letter C would become S 
        logging.info('encrypting with the Affine Cipher using a key of {} and {}'.format(key[0], key[1]))
        output = []
        for letter in text:
            if letter in lowercase:
                index = lowercase.index(letter)
                encrypt = ((key[0] * index) + key[1]) % 26
                newletter = lowercase[encrypt]
                output.append(newletter)
            
            elif letter in uppercase:
                index = uppercase.index(letter)
                encrypt = ((key[0] * index) + key[1]) % 26
                newletter = uppercase[encrypt]
                output.append(newletter)
            else:
                output.append(letter)
        return output
        
    def decrypt (key, text, uppercase, lowercase):
        output = []
        decryptkey = 26 - key[0] 
        for letter in text:
            if letter in lowercase:
                index = lowercase.index(letter)
                decrypt = (decryptkey *(index - key[1])) % 26
                #
                newletter = lowercase[decrypt]
                output.append(newletter)
            elif letter in uppercase:
                index = uppercase.index(letter)
                decrypt = (decryptkey *(index - key[1])) % 26
                newletter = uppercase[decrypt]
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
encrypt = True
text = 'A secret military team, SG-1, is formed to explore other planets through the recently discovered Stargates.'

AffineCipher(text, encrypt)