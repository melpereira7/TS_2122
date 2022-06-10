#!/usr/bin/env

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update
    sudo apt -y install python3-llfuse
    sudo apt -y install mongodb-org
    sudo systemctl start mongod.service
    sudo apt -y install python3-pip
    pip3 install pymongo
    pip3 install pyinstaller
    sudo apt -y install python3-pyqt5
    pyinstaller --onefile passthroughfs.py
    pyinstaller --onefile access_control.py
    python3 -c '''
import os
from stat import *
os.chmod("config.ini",S_IRUSR | S_IWUSR | S_IXUSR)'''
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    python3 -m pip3 install
    pip3 install pymongo
    pip3 install pyinstaller
    brew install pyqt@5
    pyinstaller --onefile passthroughfs.py
    pyinstaller --onefile access_control.py
    python3 -c '''
import os
from stat import *
os.chmod("config.ini",S_IRUSR | S_IWUSR | S_IXUSR)'''
fi


