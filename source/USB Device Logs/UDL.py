#USB Device Logs or UDL
import subprocess
def run_powershell_command(command):
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

command = "Get-PnpDevice -Class 'DiskDrive'"
output, error = run_powershell_command(command)
if output:
    with open('log.txt', 'w')as f:
        f.write(output)
        f.close()
if error:
    print("Error:")
    print(error)