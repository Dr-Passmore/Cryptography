import logging
import tkinter as tk
from tkinter import messagebox, Button
from turtle import back
from Ciphers.SubsitutionCiphers.AtbashCipher import atbashCipher
from Ciphers.SubsitutionCiphers.CaesarCipher import caesarCipher
from Ciphers.SubsitutionCiphers.ROT13Cipher import ROT13Cipher
from Ciphers.SubsitutionCiphers.ROT47Cipher import ROT47Cipher
from Ciphers.SubsitutionCiphers.BaconianCipher import BaconianCipher
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
        text = "Needs to be 20% cooler"
        encrypt = True
        ROT47Cipher(text, encrypt)
        text = "}665D E@ 36 a_T 4@@=6C"
        encrypt = False
        ROT47Cipher(text, encrypt)
        text = "When there’s no cops around, anything’s legal!"
        letters = True
        encrypt = True
        BaconianCipher(text, encrypt, letters)
        letters = False
        BaconianCipher(text, encrypt, letters)
        text = "babbaaabbbaabaaabbab baabbaabbbaabaabaaabaabaa’baaba abbababbba aaabaabbbaabbbbbaaba aaaaabaaababbbababaaabbabaaabb, aaaaaabbabbbaaabaabbaabbbabaaaabbabaabba’baaba ababbaabaaaabbaaaaaaababb!"
        letters = True
        encrypt = False
        BaconianCipher(text, encrypt, letters)
        text = "10110001110010001101 1001100111001001000100100’10010 0110101110 00010011100111110010 000001000101110101000110100011, 0000001101110001001100111010000110100110’10010 0101100100001100000001011!"
        encrypt = False
        letters = False
        BaconianCipher(text, encrypt, letters)
                
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