# CuteTools
Cute tools I created using python :3

# Saved Wifi Password Retrever or S.W.P.R
S.W.P.R basically runs the following command using subprocess: for /f "skip=9 tokens=1,2 delims=:" %i in (\'netsh wlan show profiles\') do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "Key Content") >> wifipasswords.txt.
This command saves all saved wifi passwords on the PC into a text document called wifipassword.txt
