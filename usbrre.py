import pyudev
import socket

def get_local_ip():
    try:
        # Get the local IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        print(f"Error retrieving IP address: {e}")
        return None

def on_usb_device_event(action, device):
    if action == 'add':
        print(f"USB device connected: {device.device_node}")
        ip_address = get_local_ip()
        if ip_address:
            print(f"Local IP Address: {ip_address}")

def monitor_usb_devices():
    context = pyudev.Context()
    observer = pyudev.MonitorObserver(pyudev.Monitor.from_netlink(context), on_usb_device_event)
    observer.start()

    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Monitoring stopped")

if __name__ == "__main__":
    monitor_usb_devices()
