import socket
from datetime import date
from commands import print
import threading
from time import time


# Define a whitelist of safe commands
white_list = ['len','print','str','int','min','sum','dict']


def check_command(command: str) -> bool:
    return command in white_list


def handle_client(client_socket):
    """
    Handle the client connection, allowing them to execute commands.
    """
    client_socket.send("hello user, enter a python command to exec - just the command name\n for example first type len and then [1,2,3,4], this should output 4..\n".encode())
    while True:
        # Receive the command from the user
        command = client_socket.recv(1024).decode().strip()

        # Check if the command is allowed
        if check_command(command):
            client_socket.send("enter values for command(enter if aren't)\n".encode())
            values = client_socket.recv(1024).decode().strip()
            values = values.replace("(","")#for my server safety!
            try:
                #
                # Execute the command using eval
                result = eval(command + "("+values+")")
                client_socket.send(f"Command executed: {command}, result is: {result}\nEnter command to exec\n".encode())
            except Exception as e:
                client_socket.send(f"Error executing command: {e}\nEnter command to exec\n".encode())
        else:
            client_socket.send("Command not allowed\nEnter command to exec\n".encode())


def main():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Listen on port 9999
    server_socket.listen(5)
    print("Server is listening on port 9999...")

    while True:
        client_socket, client_address = server_socket.accept()
        #print(f"Connection established with {client_address}")
        t = time()
        # Use threading to handle multiple clients
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == '__main__':
    main()
