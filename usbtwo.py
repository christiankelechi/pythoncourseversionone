import win32api
import win32con
import win32file

def list_usb_devices():
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    for drive in drives:
        drive_type = win32api.GetDriveType(drive)
        if drive_type == win32con.DRIVE_REMOVABLE:
            print(f"USB Device: {drive}")

if __name__ == "__main__":
    list_usb_devices()
