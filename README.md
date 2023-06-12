<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .container{
            align-items: center;
        }
        .image{
            max-height:200px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img class="image" src="assets/logo-full.png">
    </div>
    
</body>
</html>


## Introduction
Menous DB is a simple and elegant key value database. It uses a structured file system to store key values. The database is written in python and can be used directly in python using the menousdb library that you can install from pip using the pypi repositories. 

## Installation
### 1) Mac
To install menousdb on Mac OS, you need to install the installer from the official repository releases. You can download it [here](https://github.com/MenousTech/Menous-DB/releases/tag/1.0.2) To use the menousdb just use the following command:

```
$ sudo menousdb --start
```

### 2) Linux
To install menousdb on any linux distro, you need to install the installer from the official repository of your linux distribution. Use the following commands as per distributions

```
For Debian based distributions use:

$ sudo apt-get install menousdb
$ sudo apt install menousdb
$ sudo snap install menousdb

For Arch based distributions use:

$ sudo pacman -S menousdb
$ sudo pamac -S menousdb
```

### 3) Windows
To install menousdb for Windows, you can use curl to download the latest exe from the github releases page. You can do this by running the following command

```
curl -o menousdb.exe http:/github.com/snehashish090
```

After doing this, add the folder you have curled the file in to your environment path variables

