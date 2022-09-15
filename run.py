import cryptography
import logging

logging.info('Starting the Cryptography Program')

logging.basicConfig(filename='Cryptography.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
cryptography.CipherTool()
cryptography.CipherTool.userInterface()