#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import *
from threading import Thread
import tkinter


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")


def send_file(event=None):
    if str_file_path.get()=="":
        return
    file = str_file_path.get()
    data = file.read()
    tcp_socket.send(data)
    file.close()


host = '192.168.255.255'
my_ip = gethostbyname(gethostname())

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('', 778))
udp_socket.sendto(str.encode(my_ip), (host, 777))

server_ip, musor = udp_socket.recvfrom(1024)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((server_ip, 777))





top = tkinter.Tk()
top.title("Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

str_file_path = tkinter.StringVar()
str_file_path.set("")
file_path = tkinter.Entry(top, textvariable=str_file_path)
file_path.pack()
send_file_button = tkinter.Button(top, text="Send File", command=send_file)
send_file_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

BUFSIZ = 1024

tkinter.mainloop()  # Starts GUI execution.
