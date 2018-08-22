echo "Setting up and installing dependancies (Auto run has to be configured manually"
sudo apt-get install python3-pip
sudo apt-get install firefox-esr
export PATH=$PATH:./files/geckodriver-v0.21.0-linux32.tar.gz
sudo chmod 775 ./files/geckodriver-v0.21.0-linux32.tar.gz
#Firefox is the core browser used for the kiosk
sudo chmod 775 ./*
#Make sure every file has the 775 permission
echo "Verifying PIP modules"
sudo pip3 install selenium
sudo pip3 install configparser
