#RPIWebKiosk - Written by Joshua Ampstead
#Please read the licence for further information

import configparser # Importing dependancies to allow the program to work
from selenium import webdriver
import os

class main: # Defining the main object
	config = configparser.ConfigParser() # Create a configuration object 
	config.read("./config.ini") # Assigning the "config.ini" file to the configuration object
	plugins = config.get("config","firefox_addons") # Getting information from the config file to find the name of the firefox extentions
	plugins = plugins.split(";") # Spliting up the list of XPI files (Firefox extentions)
	webpage = config.get("config", "webpage") # Getting the webpage address from the config
	ffprofile = webdriver.FirefoxProfile() # Creating a firefox profile object


	def __init__(self): # Initialisation
		print("Booting up webbrowser with current config!") # Info 
		self.add_ext() # Function that adds extentions onto the firefox profile
		browser = webdriver.Firefox(firefox_profile=self.ffprofile) # Create the browser object using the profile created previously
		self.browser.get(self.webpage) # Setting the browser to the website set in config


	def add_ext(self): # Function to add extentions onto the firefox profile
		for i in range(0, len(self.plugins)): # Repeat for the number of firefox addons written in the config
			self.ffprofile.add_extension(extension="./files/firefox_addons/" + self.plugins[i]) # Add an extention to the firefox profilee 
																

if __name__ == "__main__": # If the script is ran
	main() # run the main class 
	config = configparser.ConfigParser() # Create a configuration object
	config.read("./config.ini") # Read the config file
	if config.read("config","shutdown_on_close") == "true": # If shutdown on close is true
		os.system("sudo halt") # Shutdown the system
