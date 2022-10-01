from re import S
import string
import logging
import cryptography

class RailFenceCipher:
    def __init__(self, text, key):
        logging.info('Rail-Fence Cipher Selected')
        #In the rail fence cipher, the plaintext is written downwards diagonally on successive "rails" of an imaginary fence, 
        #then moving up when the bottom rail is reached, down again when the top rail is reached, and so on until the whole plaintext is written out. 
        #The ciphertext is then read off in rows. 
        #tests becomes 'tsets' 
        #t   s
        # e t
        #  s
        RailFenceCipher.encrypt(self, text, key)
        
    def encrypt(self, text, key):
        logging.info('Encrypting')
        rail = [["//" for character in range(len(text))] 
                for rows in range (key)]
        
        row = 0 
        flag = 0 
        
        for character in range (len(text)):
            rail[row][character] = text[character]
            if row == 0:
                flag = 0
            elif row==key-1:
                flag = 1
            if flag == 0:
                row += 1
            else:
                row-=1
        
        for line in range(key):
            print("".join(rail[line]))
            
        output = []
        for line in range(key):
            for character in range(len(text)):
                if rail[line][character]!='//':
                    output.append(rail[line][character])
        
        output = ''.join(map(str, output))
        print (output)
        
       
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
text = "Home is where the heart is, but the stars are made of latinum."
key = 9
RailFenceCipher(text, key)