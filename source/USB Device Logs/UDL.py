#USB Device Logs or UDL
import os
from datetime import datetime
import win32com.client

def log(drive, drives):
    drive_count = len(drives)

    path = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(path):
        os.mkdir(path)


    All = os.path.join(path, 'All_Connected_Drives')
    if not os.path.exists(All):
        os.mkdir(All)


    New = os.path.join(path, 'New_Connected_Drives')
    if not os.path.exists(New):
        os.mkdir(New)

    filename = f'{datetime.today().strftime("%Y-%m-%d %H-%M-%S")}_log.txt'
    all_file_path = os.path.join(All, filename)
    new_file_path = os.path.join(New, filename)
    logfilename = 'General_logs.txt'



    with open(new_file_path, 'w') as f:
        f.write(datetime.today().strftime("%Y-%m-%d %H-%M-%S"))
        f.write("\n------------------------")
        f.write(f"\nDrive model: {drive.Model}")
        f.write(f"\nDrive capacity: {round(int(drive.Size) / (1024**3), 2)} GB")
        f.write(f"\nDrive interface type: {drive.InterfaceType}")
        f.write(f"\nDrive serial number: {drive.SerialNumber}")
        f.close()
    with open(all_file_path, 'w') as f:
        f.write(datetime.today().strftime("%Y-%m-%d %H-%M-%S"))
        f.write("\n------------------------")
        f.write(f"\nConnected drives: {drive_count}")
        for number in range(drive_count):
            f.write(f"\n{number + 1}. {drives[number].Model}")

        for drive1 in drives:
            f.write(f"\nDrive model: {drive1.Model}")
            f.write(f"\nDrive interface type: {drive1.InterfaceType}")
            f.write(f"\nDrive capacity: {round(int(drive1.Size) / (1024 ** 3), 2), } GB")
            f.write(f"\nDrive serial number: {drive.SerialNumber}")
            f.write("\n------------------------")
        f.close()

def detect_new_drive():
    wmi = win32com.client.GetObject("winmgmts:")
    drives = wmi.InstancesOf("Win32_DiskDrive")
    initial_drive_count = len(drives)

    while True:
        drives = wmi.InstancesOf("Win32_DiskDrive")
        current_drive_count = len(drives)

        if current_drive_count > initial_drive_count:
            new_drive = [drive for drive in drives if drive.Index == current_drive_count - 1][0]
            print("New drive detected!")
            print("Drive model:", new_drive.Model)
            print("Drive capacity: ", round(int(new_drive.Size) / (1024**3), 2), "GB")
            print("Drive interface type:", new_drive.InterfaceType)
            print("Drive serial number:", new_drive.SerialNumber)

            log(new_drive, drives)



            initial_drive_count = current_drive_count

        elif current_drive_count < initial_drive_count:
            print("Drive unplugged!")
            initial_drive_count = current_drive_count


def detect_all_drives():
    wmi = win32com.client.GetObject("winmgmts:")
    drives = wmi.InstancesOf("Win32_DiskDrive")
    initial_drive_count = len(drives)

    print(f"\nCurrently connected drives: {initial_drive_count}")
    for number in range(initial_drive_count):
        print(f"\n{number + 1}. {drives[number].Model}")

    for drive in drives:
        print("\nDrive model:", drive.Model)
        print("Drive interface type:", drive.InterfaceType)
        print("Drive capacity:", round(int(drive.Size) / (1024 ** 3), 2), "GB")
        print("Drive serial number:", drive.SerialNumber)
        print("---")


detect_all_drives()
detect_new_drive()


