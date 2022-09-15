import logging
import tkinter as tk
from Ciphers.SubsitutionCiphers.CaesarCipher import caesarCipher
from Ciphers.SubsitutionCiphers.ROT13Cipher import ROT13Cipher
#from Ciphers.test import testing


class CipherTool:
    def __init__(self):
        logging.info('Cipher Tool has been initialised')
        
        
    def userInterface():
        logging.info('User Interface is being initialised')
        root = tk.Tk()
        root.mainloop()
        logging.info('User Interface loaded')
        text = "This is a quick test"
        step = 4
        caesarCipher(text, step)
        #text = "This is a quick test"
        #ROT13Cipher(text)
        
    def returnOutput(output):
        print(output)

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CipherTool()