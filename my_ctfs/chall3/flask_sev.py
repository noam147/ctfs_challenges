from flask import Flask, make_response, render_template, request, redirect, url_for
import hashlib

PORT = 11113
app = Flask(__name__)


@app.route('/')
def handle_user():
    return """
    <html>
        <head><title>Welcome</title></head>
        <body>
            <h2>Connect with ncat to port 99999 and find the flag!</h2>
            <p>Here is the source code for your pleasure :)</p>
            <p><em>Remember, in this world, things are rarely as they seem...</em></p>

            <pre>
import socket
from datetime import date
from commands import print
import threading
from time import time

# Define a whitelist of safe commands
white_list = ['len', 'print', 'str', 'int', 'min', 'sum', 'dict']

def check_command(command: str) -> bool:
    "
    Check if the
    command is in the
    whitelist.
    "
    command_parts = command.split()
    return command_parts[0] in white_list

def handle_client(client_socket):
    client_socket.send("Hello user, enter a Python command to exec - just the command name\n"
                       "For example, first type 'len' and then [1, 2, 3, 4], this should output 4..\n")
    while True:
        command = client_socket.recv(1024).decode().strip()

        if check_command(command):
            client_socket.send("Enter values for command (enter if aren't)\n".encode())
            values = client_socket.recv(1024).decode().strip()
            values = values.replace("(", "")  # For server safety!
            try:
                result = eval(command + "(" + values + ")")
                client_socket.send(f"Command executed: {command}, result is: {result}\nEnter command to exec\n".encode())
            except Exception as e:
                client_socket.send(f"Error executing command: {e}\nEnter command to exec\n".encode())
        else:
            client_socket.send("Command not allowed\nEnter command to exec\n".encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Listen on port 9999
    server_socket.listen(5)
    print("Server is listening on port 9999...")

    while True:
        client_socket, client_address = server_socket.accept()
        t = time()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
            </pre>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=False, port=PORT, host='0.0.0.0')
