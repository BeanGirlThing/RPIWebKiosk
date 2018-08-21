#RPIWebKiosk - Written by Joshua Ampstead
#Please read the licence for further information

import configparser
from selenium import webdriver
import os

class main:
	config = configparser.ConfigParser()
	config.read("./config.ini")
	plugins = config.get("config","firefox_addons")
	plugins = plugins.split(";")
	webpage = config.get("config", "webpage")
	ffprofile = webdriver.FirefoxProfile()
	for i in range(0,len(plugins)):
		ffprofile.add_extension(extension="./files/"+plugins[i])
	browser = webdriver.Firefox(firefox_profile=ffprofile)
	def __init__(self):
		print("Booting up webbrowser with current config!")
		self.browser.get(self.webpage)


if __name__ == "__main__":
	main()
	config = configparser.ConfigParser()
	config.read("./config.ini")
	if config.read("config","shutdown_on_close") == "true":
		os.system("sudo halt")
