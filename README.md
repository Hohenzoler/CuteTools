# CuteTools
Cute tools I created using python :3 I'm planning on combining all tools in this repo into an all in one file sort of thing.

# Known bugs
1. NDS printing just a couple of connected devices.


# Saved Wifi Password Retriever or SWPR
S.W.P.R basically runs the following command using subprocess: for /f "skip=9 tokens=1,2 delims=:" %i in (\'netsh wlan show profiles\') do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "Key Content") >> wifipasswords.txt.
This command saves all saved wifi passwords on the PC into a text document called wifipassword.txt.

# Network Device Scanner or NDS
N.D.S. scans your local network using the scapy.arping() command. It prints every 10 secounds all connected devices' IPv4 and MAC addresses along side the manufacture of the given device's wifi antenna.
