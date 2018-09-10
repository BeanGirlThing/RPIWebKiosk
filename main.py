#RPIWebKiosk - Written by Joshua Ampstead - merhlim.me
#Please read the licence for further information

import configparser # Importing dependancies to allow the program to work
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import socket
import httplib

class main: # Defining the main object
	config = configparser.ConfigParser() # Create a configuration object 
	config.read("./config.ini") # Assigning the "config.ini" file to the configuration object
	webpage = config.get("config", "webpage") # Getting the webpage address from the config
	kiosk = config.get("config", "kiosk") # Check wether the browser will run in kiosk mode
	options = Options() # Create a chrome options object
	if kiosk == "True": # If the browser is supposed to run in kiosk mode
                options.add_argument("--kiosk") # Set an arguement to make the browser run in kiosk mode

	def __init__(self): # Initialisation
		print("Booting up webbrowser with current config, on page '"+self.webpage+"'!") # Info 
		browser = webdriver.Chrome(chrome_options=self.options) # Create the browser object using the profile created previously
		browser.get(self.webpage)
		while self.browserstatus(browser):
			print(str(self.browserstatus(browser)))
			sleep(0.1)

	def browserstatus(self,browser):
		try:
			browser.execute(Command.STATUS)
			return True
		except(socket.error, httplib.CannotSendRequest):
			return False
		except:
			raise socket.error
if __name__ == "__main__": # If the script is ran
	main() # run the main class 
	config = configparser.ConfigParser() # Create a configuration object
	config.read("./config.ini") # Read the config file
	print("Terminating program")
	if config.read("config","shutdown_on_close") == "True": # If shutdown on close is true
		os.system("sudo halt") # Shutdown the system

