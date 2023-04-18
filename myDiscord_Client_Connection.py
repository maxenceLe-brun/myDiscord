import pyaudio
import socket
import threading


class Client:
    def __init__(self, server_info: tuple, input_device=1, mute=False):
        self.__server_ip = server_info[0]
        self.__server_port = server_info[1]
        self.__socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__audio = pyaudio.PyAudio()
        self.__input_device = input_device
        self.__mute = mute
        
    def __connect(self):
        self.__connection = self.__socket_connection.connect((self.__server_ip, self.__server_port))

    def __send_audio(self):        
        self.__stream = self.__audio.open(44100, 1, pyaudio.paInt16, input=True, input_device_index=self.__input_device)
        while True:
            if not self.__mute:
                self.__socket_connection.send(self.__stream.read(4096))
    
    def __get_audio(self):
        self.__get_stream = self.__audio.open(44100, 1, pyaudio.paInt16, output=True)
        while True:
            self.__data = self.__socket_connection.recv(4096)
            self.__get_stream.write(self.__data)

    def StartAudioConnection(self, send_audio=True, recieve_audio=True):
        self.__connect()
        if send_audio:
            self.__send_thread = threading.Thread(target=self.__send_audio)
            self.__send_thread.start()
        if recieve_audio:
            self.__get_thread = threading.Thread(target=self.__get_audio)
            self.__get_thread.start()
    
    def Mute(self):
        self.__mute = True
    
    def Unmute(self):
        self.__mute = False

                
    

        
        