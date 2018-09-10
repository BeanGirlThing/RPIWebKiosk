#RPIWebKiosk - Written by Joshua Ampstead - merhlim.me
#Please read the licence for further information

import configparser # Importing dependancies to allow the program to work
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class main: # Defining the main object
	config = configparser.ConfigParser() # Create a configuration object 
	config.read("./config.ini") # Assigning the "config.ini" file to the configuration object
	webpage = config.get("config", "webpage") # Getting the webpage address from the config
	kiosk = config.get("config", "kiosk") # Check wether the browser will run in kiosk mode
	options = Options() # Create a chrome options object
	if kiosk == "True": # If the browser is supposed to run in kiosk mode
	options.add_arguement("--kiosk") # Set an arguement to make the browser run in kiosk mode

	def __init__(self): # Initialisation
		print("Booting up webbrowser with current config!") # Info 
		browser = webdriver.Chrome(executable_path=r"./chromedriver",chrome_options=self.options()) # Create the browser object using the profile created previously
		self.browser.get(self.webpage) # Setting the browser to the website set in config
																

if __name__ == "__main__": # If the script is ran
	main() # run the main class 
	config = configparser.ConfigParser() # Create a configuration object
	config.read("./config.ini") # Read the config file
	if config.read("config","shutdown_on_close") == "True": # If shutdown on close is true
		os.system("sudo halt") # Shutdown the system
