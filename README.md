![test](assets/logo-full.png)


## Introduction
Menous DB is a simple and elegant key value database. It uses a structured file system to store key values. The database is written in python and can be used directly in python using the menousdb library that you can install from pip using the pypi repositories. 

## Installation
### 1) Mac
To install menousdb on Mac OS, you need to install the installer from the official repository releases. You can download it [here](https://github.com/MenousTech/Menous-DB/releases/tag/1.0.2) To use the menousdb just use the following command:

```
$ sudo menousdb --start
```

### 2) Linux
To install menousdb on any linux distro, you need to manually build the project

```
$ sudo apt-get install git
$ git clone https://github.com/MenousTech/Menous-DB
$ cd Menous-DB 
$ sudo apt-get install python3-pip
$ sudo python3 -m  pip install -r requirements.txt
$ sudo python3 -m pip install pyinstaller
$ cd src
$ sudo python3 -m PyInstaller --onefile api.py
$ sudo mv dist/api /usr/bin/menousdb
$ sudo menousdb --newuser
```

### 3) Windows
To install menousdb for Windows, you can use curl to download the latest exe from the github releases page. You can do this by running the following command

```
curl -o menousdb.exe https://github.com/MenousTech/Menous-DB/releases/download/1.0.2/menousdb.exe
```

After doing this, add the folder you have curled the file in to your environment path variables

