import logging
import tkinter as tk
from tkinter import messagebox, Button
from turtle import back
from Ciphers.SubsitutionCiphers.CaesarCipher import caesarCipher
from Ciphers.SubsitutionCiphers.ROT13Cipher import ROT13Cipher
#from Ciphers.test import testing


class CipherTool:
    def __init__(self):
        logging.info('Cipher Tool has been initialised')
    
    def initialTesting():
        text = "This is a quick test"
        step = 4
        caesarCipher(text, step)
        text = "This is a quick test"
        encrypt = True
        ROT13Cipher(text, encrypt)
        text = "Guvf vf n dhvpx grfg"
        encrypt = False
        ROT13Cipher(text, encrypt)
        
    def userInterface():
        logging.info('User Interface is being initialised')
        root = tk.Tk()
        root.title('Cryptography')
        root.geometry("800x560")
        exit_button = Button(
            root,
            text = 'Exit',
            width = 11,
            height = 2,
            background='red',
            command= lambda : CipherTool.exit(root)
        )
        exit_button.pack()
        root.mainloop()
        logging.info('User Interface loaded')
        CipherTool.initialTesting()
        
    def returnOutput(output):
        print(output)
        
    def exit (root):
        logging.info('Exit button clicked')
        confirmbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
        if confirmbox == 'yes':
            logging.info('Exiting the program')
            root.destroy()
        else:
            logging.info('exit has been aborted')

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CipherTool()