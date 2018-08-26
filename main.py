#RPIWebKiosk - Written by Joshua Ampstead
#Please read the licence for further information

import configparser
from selenium import webdriver
import os
from pyvirtualdisplay import Display

class main:
	display = Display(visible=0,size=(800,600))

	config = configparser.ConfigParser()
	config.read("./config.ini")
	plugins = config.get("config","firefox_addons")
	plugins = plugins.split(";")
	webpage = config.get("config", "webpage")
	ffprofile = webdriver.FirefoxProfile()


	def __init__(self):
		print("Booting up webbrowser with current config!")
		self.start_display()
		self.add_ext()
		browser = webdriver.Firefox(firefox_profile=self.ffprofile)
		self.browser.get(self.webpage)

	def start_display(self):
		print("Starting virtual display")
		self.display.start()
		print("Virtual display started successfully")

	def add_ext(self):
		for i in range(0, len(self.plugins)):
			self.ffprofile.add_extension(extension="./files/firefox_addons/" + self.plugins[i])


if __name__ == "__main__":
	main()
	config = configparser.ConfigParser()
	config.read("./config.ini")
	if config.read("config","shutdown_on_close") == "true":
		os.system("sudo halt")
