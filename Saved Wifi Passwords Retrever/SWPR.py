#Saved Wifi Password Retrever or S.W.P.R
import subprocess

cmd = 'for /f "skip=9 tokens=1,2 delims=:" %i in (\'netsh wlan show profiles\') do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "Key Content") >> wifipasswords.txt'
subprocess.run(cmd, shell=True)