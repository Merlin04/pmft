## What is pmft?

pmft is a tool to flash Pro Micros with a hex file. It works much better than other solutions such as dfu-programmer and avrdude. It was created with the [mechanical keyboard community](https://reddit.com/r/mechanicalkeyboards) in mind, but works for any application. 

## How does it work?

It uses a python script from paranoid.rat on the [Adafruit Forums](https://forums.adafruit.com/viewtopic.php?f=22&t=35335) and avrdude as its base. I built a wrapper around this script that allows for installation and ease of use. All code/binaries I did not create belongs to the respective owners and is licensed under the license the owner chose. 

## How do I install it?

Download the zip file containing the files. Run the installer script for your platform:

#### Note for Linux and MacOS:

Be sure to keep all of the files together, the python script copies the files into their folders. Once you install pmft, you can delete the files from the zip file. 

### Linux:

`sudo python linux-install.py`

### MacOS (WIP):

`sudo python macos-install.py`

### Windows:

Double-click on the installer executable in the `pmft-win folder`. You don't need any other files. Do not change the place where pmft installs from the default, which should be `C:\Program Files (x86)\pmft`. 

## Usage

Type `pmft help` for help:
```
pmft v0.1
Usage: pmft [hex file path] [port]
```
To flash a pro micro, you must run pmft as an administrator/using sudo. 

