#!/usr/bin/env

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt -y install python3-llfuse
    sudo apt -y install curl
    curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
    sudo apt update
    sudo apt -y install mongodb-org
    sudo systemctl start mongod.service
    sudo apt -y install python3-pip
    pip3 install pymongo
    pip3 install pyinstaller
    sudo apt -y install python3-pyqt5
    pyinstaller --onefile passthroughfs.py
    pyinstaller --onefile access_control.py
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install mongodb-community
    python3 -m pip3 install
    pip3 install pymongo
    pip3 install pyinstaller
    brew install pyqt@5
    pyinstaller --onefile passthroughfs.py
    pyinstaller --onefile access_control.py
fi


