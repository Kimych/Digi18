# Digi18

This project is intended to emulate host PC requests via Digi18 protocol

# Install
## Windows
1. Check/install latest python3 vesrion from here https://www.python.org/downloads/
2. Check/install 'google' module: 
```
pip install --upgrade google-api-python-client
```
3. Check/install 'serial' module:
```
pip install pyserial
```

# Run
1. Download and ukpack (or clone) project from here https://github.com/Kimych/Digi18
2. Open comman console with administartive rights and navigate into the project folder.
3. Check COM/UART port and boud rate in the COMHost.py. Example for Linux the port should be like '/dev/ttyUSB0', for Windows - 'COM6'.
4. run command:
### Windows
```
python COMHost.py
```

1. Download and ukpack (or clone) project from here https://github.com/Kimych/Digi18
2. Check COM/UART port and bound rate in the COMHost.py. Example: Linux - "/dev/ttyUSB0", Windows - COM6.
3. Run the script: python COMHost.py


# Compile
If you changed proto/Digi18Com.proto file then new bin/Digi18Com_pb2.py should be compiled. How to do it (and also some additional information) can be found here https://developers.google.com/protocol-buffers/docs/pythontutorial
## Unbuntu
run build/compile_proto.sh to compile it in Linux
## Windows
python COMHost.py
