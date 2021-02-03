# Digi18

This project is intended to emulate host PC requests via Digi18 protocol to the sampler device

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
4. Check/install 'inputimeout' module:
```
pip install inputimeout
```

# Run
1. Download and unpack (or clone) project from here https://github.com/Kimych/Digi18
2. Open command line console (cmd or PowerShell) and navigate into the project folder.
3. Check COM/UART port name (and boud rate) in the COMHost.py. For Linux the port should be like '/dev/ttyUSB0', for Windows like 'COM1'.
4. run command:
### Windows
```
python COMHost.py
```

# Compile
If you changed proto/Digi18Com.proto file then new bin/Digi18Com_pb2.py should be compiled. How to do it (and also some additional information) can be found here https://developers.google.com/protocol-buffers/docs/pythontutorial
## Unbuntu
run build/compile_proto.sh to compile it in Linux
