import time
import requests

def keep_alive():
    while True:
        try:
            # Gửi yêu cầu đến Google Cloud Console (hoặc URL bất kỳ)
            requests.get('https://shell.cloud.google.com/?hl=en_US&fromcloudshell=true&show=terminal')
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(300)  # Ngủ 5 phút

if __name__ == "__main__":
    keep_alive()