import socket
import threading





class myDiscordServer:
    def __init__(self, selfIp):
        self.__selfIp = selfIp
        self.__output_connection = []

    def redirect_audio(self, input_connection):
        while True:
            data = input_connection.recv(4096)
            for i in self.__output_connection:
                print(self.__output_connection, i)
                i.send(data)
    
    def remove_pending(self):
        self.__output_connection = []
            
    def audio_server(self):
        sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sending_socket.bind((self.__selfIp, 7000))
    
        sending_socket.listen()
        connection, address = sending_socket.accept()
        self.__output_connection.append(connection)
        
        server_thread = threading.Thread(target=self.redirect_audio, args=(connection,))
        server_thread.start()
    
test = myDiscordServer("10.10.2.22")
test.audio_server()

        

    