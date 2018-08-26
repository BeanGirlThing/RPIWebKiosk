echo "Setting up and installing dependancies (Auto run has to be configured manually"
sudo apt-get install python3-pip
sudo apt-get install firefox-esr
sudo cp files/geckodriver /usr/local/bin/
sudo chmod 775 ./files/geckodriver
#Firefox is the core browser used for the kiosk
sudo chmod 775 ./*
#Make sure every file has the 775 permission
echo "Verifying PIP modules"
sudo pip3 install selenium
sudo pip3 install configparser
