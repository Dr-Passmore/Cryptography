import string
import logging
import cryptography
#http://practicalcryptography.com/ciphers/
#https://www.dcode.fr
class AffineCipher:
    def __init__(self, text, encrypt, key):
        #Possible values of A - 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25
        
        #B can be arbitrary as long as a does not equal 1 since this is the shift of the cipher
        #logging.info('Affine Cipher has been initialised')
        uppercase = list(string.ascii_uppercase)
        lowercase = list(string.ascii_lowercase)
        #21, 5 both work 
        #key = [11, 24]
        output = AffineCipher.encrypt(key, text, uppercase, lowercase)
        output = ''.join(map(str, output))
        #print (output)
        text = output
        output = AffineCipher.decrypt(key, text, uppercase, lowercase)
        output = ''.join(map(str, output))
        #print (output)
        
    def encrypt (key, text, uppercase, lowercase):
        #only requires one. A IF statement using encyrpt True or False can be used to update logging info
        
        #encrypt calulation A x Letter index (if A is 5 and letter is C then (5 X 2)) Then plus B, if B was 8, (5 X 2)+8. Finally % by 26. The letter C would become S 
        #logging.info('encrypting with the Affine Cipher using a key of {} and {}'.format(key[0], key[1]))
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
        output = ''.join(map(str, output))
        logging.info('Output using key {} and shift {} = {}'.format(key[0], key[1], output))
        return output
    
    def modularMultiplicationInverse (key, alphabet):
        alphabet = len(alphabet)
        for inversekey in range(key[0], alphabet):
            if (((key[0] % alphabet) * (inversekey % alphabet)) % alphabet == 1):
                decryptkey = alphabet + inversekey
                #logging.info('The decrypt key from a key of {} is {}'.format(key[0], decryptkey))
                return decryptkey
                
        #print(inversekey)
        decryptkey = alphabet - inversekey
        print(decryptkey)
        return decryptkey
     
    
    def decrypt (key, text, uppercase, lowercase):
        output = []
        for letter in text:
            if letter in lowercase:
                index = lowercase.index(letter)
                decryptkey = AffineCipher.modularMultiplicationInverse(key, lowercase)
                decrypt = (decryptkey *(index - key[1])) % 26
                newletter = lowercase[decrypt]
                output.append(newletter)
            elif letter in uppercase:
                index = uppercase.index(letter)
                decryptkey = AffineCipher.modularMultiplicationInverse(key, uppercase)
                decrypt = (decryptkey *(index - key[1])) % 26
                newletter = uppercase[decrypt]
                output.append(newletter)
            else:
                output.append(letter)
        output = ''.join(map(str, output))
        logging.info('Output using key {} and shift {} = {}'.format(key[0], key[1], output))
        return output
        
                
    def output(output):
        logging.info('Returning message')
        cryptography.CipherTool.returnOutput(output)
        
logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

key1 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
workingKeys = [1, 3, 5, 7, 11, 17, 25 ]
brokenkeys = [9, 15, 19, 21, 23]
for keyNumber in workingKeys:
    for shiftkey in range(26):
        
        key = [keyNumber, shiftkey]
        encrypt = True
        text = 'A secret military team, SG-1, is formed to explore other planets through the recently discovered Stargates.'
        #text = 'cat'
        AffineCipher(text, encrypt, key)