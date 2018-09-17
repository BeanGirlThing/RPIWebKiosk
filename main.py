#RPIWebKiosk - Written by Joshua Ampstead - merhlim.me
#Please read the licence for further information

import configparser # Importing dependancies to allow the program to work
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
#import socket
#import httplib

class main: # Defining the main object
	config = configparser.ConfigParser() # Create a configuration object 
	config.read("./config.ini") # Assigning the "config.ini" file to the configuration object
	webpage = config.get("config", "webpage") # Getting the webpage address from the config
	kiosk = config.get("config", "kiosk") # Check wether the browser will run in kiosk mode
	chromedriver = config.get("config", "chromedriver")
	options = Options() # Create a chrome options object
	if kiosk == "True": # If the browser is supposed to run in kiosk mode
                options.add_argument("--kiosk") # Set an arguement to make the browser run in kiosk mode

	def __init__(self): # Initialisation
		print("Booting up webbrowser with current config, on page '"+self.webpage+"'!") # Info 
		browser = webdriver.Chrome(executable_path=self.chromedriver, chrome_options=self.options) # Create the browser object using the profile created previously
		browser.get(self.webpage) # Open the browser to the webpage specified in the config
		while True: # Repeat until break
			try: # Try-Catch
				sleep(0.1) # Sleep for .1 of a second
			except KeyboardInterrupt: # Catch KeyboardInterupt
				browser.quit() # Close the browser
				break # Break the loop

if __name__ == "__main__": # If the script is ran
	main() # run the main class
	config = configparser.ConfigParser() # Create a configuration object
	config.read("./config.ini") # Read the config file
	print("Terminating program   "+ str(config.read("config", "reboot_on_close")))
	if config.read("config","reboot_on_close")[0].upper() == "TRUE": # If shutdown on close is true
		os.system("reboot") # Shutdown the system

