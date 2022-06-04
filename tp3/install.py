#!/usr/bin/env python

import os
from stat import *

# Create folders
try:
    os.mkdir("build")
except OSError:
    print ("Creation of the directory %s failed" % "exec")
else:
    print ("Successfully created the directory %s " % "exec")

try:
    os.mkdir("dist")
except OSError:
    print ("Creation of the directory %s failed" % "exec")
else:
    print ("Successfully created the directory %s " % "exec")

try:
    os.mkdir("spec")
except OSError:
    print ("Creation of the directory %s failed" % "exec")
else:
    print ("Successfully created the directory %s " % "exec")

# Set config permissions
os.chmod("src/configs/config.data", S_IRUSR | S_IWUSR | S_IXUSR)
os.chmod("src/configs", S_IRUSR | S_IWUSR | S_IXUSR)

# Install dependecies
os.system('pip3 install pymongo')
os.system('pip3 install configparser')
os.system('pip3 install fusepy')
os.system('pip3 install websockets')

# Build 
os.system('pyinstaller -F --add-data src/configs/config.data:. --distpath dist --workpath build ./src/fuse/acl.py ')
os.system('pyinstaller -F --add-data src/configs/config.data:. --add-data src/fuse/index.html:. --distpath dist --workpath build ./src/fuse/passthrough.py ')
os.system('pyinstaller -F --add-data src/configs/config.data:. --distpath dist --workpath build ./src/server/server.py ')

os.system('mv *.spec spec/')