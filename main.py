import logging
import tkinter as tk
#from Ciphers.test import testing


class CipherTool:
    def __init__(self):
        logging.info('Cipher Tool has been initialised')
        CipherTool.userInterface(self)
        
    def userInterface(self):
        logging.info('User Interface is being initialised')
        root = tk.Tk()
        root.mainloop()
        logging.info('User Interface loaded')

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CipherTool()