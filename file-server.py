# python server to host a file

import socket
import os
import sys
import time

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345

def handle_client(conn, addr, filepath):
    print(f"[+] Connection from {addr}")
    try:
        with open(filepath, "rb") as f:

            while chunk := f.read(8192):  # Read 8KB at a time
                conn.sendall(chunk)

            print(f"Sent file: {filepath} to {addr}")
            time.sleep(2)

            conn.shutdown(socket.SHUT_WR)  # ??? 
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        conn.sendall("FILE_NOT_FOUND".encode()) # Send a message to the client
    except Exception as e:
        print(f"Error sending file: {e}")
        conn.sendall(f"ERROR:{e}".encode())  # Send error message to the client
    finally:
        print(f"[-] Connection closed from {addr}")
        conn.close()


def start_server(filepath):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[+] Server listening on {HOST}:{PORT}")

        while True:
            print("into this while loop")
            conn, addr = server.accept()
            handle_client(conn, addr, filepath) # Pass the filepath to the handler

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server.close()
        print("[+] Server stopped.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    start_server(filepath)