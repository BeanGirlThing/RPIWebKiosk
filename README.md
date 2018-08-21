# RPIWebKiosk
Initially for RAAS but can be used on any raspberry pi you wish to turn into a web kiosk

# Installation

To install it is recommended that you are using the latest version of raspbian, but be aware that this software was
programmed on: 

```
Raspbian Stretch with desktop
Version: June 2018.
Release date: 2018-06-27.
Kernel version: 4.14.
```

Installation is simple and should not cause any problems as long as all raspberry pi systems are working

The code should work straight off of git (Please assure you have python3 installed to your Raspberry Pi)

To download, CD into the directory you wish to save the binary files in and run the command

```
git clone https://github.com/merhlim/RPIWebKiosk
```

Which will clone the repository to the host folder

Once downloaded, it is recommended that you run 

```
sudo chmod 775 setup.sh
sudo .\setup.sh
```

To verify dependencies and make sure everythings where it should be

(You do not need to run this file if you are installing manually, if so then please see the manual install section)
 
Once that is done you should be able to run the program by typing 

```
./startup.sh
```

Or you can configure the raspberry pi to run the software on startup

## Take note

Raspberry pi systems contain various methods of access that could cause sudden system fault or access to the main system
being forcefully accessed

Some methods can include:

SSH

TTY 1-6

Ctrl + Alt + T 

Unplugging the raspberry pi

