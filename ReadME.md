# File Server Project

This project implements a simple file server and client using Python's `socket` module. It allows a user to host a file on a server and then download that file from a client.

## Purpose

The primary purpose of this project is to demonstrate basic network programming concepts using sockets in Python. It provides a practical example of how to:

- Establish TCP connections between a client and server.h
- Transfer data (files) over a network.
- Handle basic errors like file not found.
- Implement a simple client-server architecture.

This project is suitable for educational purposes, learning about network programming, or as a starting point for more complex file transfer applications.

## Usage

### Server

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/harkeshbirman/file-server.git
    cd file-server
    ```

2.  **Run the server:**

    ```bash
    python server.py <filepath>
    ```

    Replace `<filepath>` with the absolute path to the file you want to share. For example:

    ```bash
    python server.py /path/to/my/file.mkv
    ```

3.  The server will start listening on port 12345 (default). It will print messages indicating its status and any connections.

### Client

1.  **Run the client:**

    ```bash
    python client.py <server_ip> <server_port> <save_path>
    ```

    - `<server_ip>`: The IP address of the machine running the server.
    - `<server_port>`: The port the server is listening on (default is 12345).
    - `<save_path>`: The path where you want to save the downloaded file on the client machine.

    For example:

    ```bash
    python client.py 192.168.1.100 12345 /save/path/downloaded_file.mkv
    ```

    Replace `192.168.1.100` with the server's IP address.

2.  The client will connect to the server, download the file, and save it to the specified path. It will also display the download speed and file size.

## Important Notes

- **Firewall:** Ensure that your firewall allows connections on port 12345 (or the port you are using) for both the server and client.
- **IP Address:** Make sure the client is using the correct IP address of the server. If the server is running on a local network, you might need to use its local IP address (e.g., 192.168.x.x).
- **File Path:** Use the correct absolute file path when starting the server.
- **Error Handling:** The server and client include basic error handling for file not found and connection issues.
- **Large Files:** The code is designed to handle large files efficiently by transferring data in chunks.
- **Binary Mode:** The client and server use binary mode for file transfer, which is essential for handling all file types correctly.
