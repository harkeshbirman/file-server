# python client to receive the file hosted by file-server

import socket
import sys
import os
import time

def download_file(server_ip, server_port, save_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((server_ip, server_port))
        print(f"[+] Connected to {server_ip}:{server_port}")

        total_bytes_received = 0
        start_time = time.time()

        with open(save_path, "wb") as f:
            while True:
                chunk = client.recv(8192)
                if not chunk:
                    break

                if chunk.startswith(b"FILE_NOT_FOUND"):
                    print("Error: File not found on the server.")
                    return
                elif chunk.startswith(b"ERROR:"):
                    print(f"Error: {chunk.decode()}")
                    return

                f.write(chunk)
                total_bytes_received += len(chunk)

                # Calculate and print network speed
                elapsed_time = time.time() - start_time
                if elapsed_time > 0:  # Avoid division by zero
                    bytes_per_second = total_bytes_received / elapsed_time
                    mbps = bytes_per_second / (1024 * 1024)  # Convert to MB/s
                    print(f"Speed: {mbps:.2f} MB/s", end="\r")  # \r overwrites the previous line

        print("\n")  # Add a newline after the download finishes

        # Print file size in MB or GB
        file_size_bytes = os.path.getsize(save_path)
        file_size_mb = file_size_bytes / (1024 * 1024)
        if file_size_mb >= 1024:
            file_size_gb = file_size_mb / 1024
            print(f"[+] File saved to {save_path} ({file_size_gb:.2f} GB)")
        else:
            print(f"[+] File saved to {save_path} ({file_size_mb:.2f} MB)")


    except ConnectionRefusedError:
        print(f"[-] Connection refused. Make sure the server is running on {server_ip}:{server_port}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_ip> <server_port> <save_path>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2]) # Convert port to integer
    save_path = sys.argv[3]

    if not os.path.exists(os.path.dirname(save_path)): #check if save directory exists
        os.makedirs(os.path.dirname(save_path))

    download_file(server_ip, server_port, save_path)