import socket	# package for connect to sockets for connection establishment
import tqdm	# package to represent the progress of file transfer
import os
from tkinter import *
from tkinter import messagebox

window = Tk()
global porttxt,client_socket,address
window.title("Welcome to File Sharing Platform")
window.geometry('800x650')
mainlbl = Label(window,text="Enter your IP & Port to receive file").grid(padx=150,pady=25,column=1)

iplbl = Label(window,text='IP Address: ').grid(column=0,row=3,padx=10,pady=15)
iptxt = Entry(window,width=25)
iptxt.grid(column=1,row=3,padx=10,pady=15)

portlbl = Label(window,text='PORT Number: ').grid(column=0,row=5,padx=10,pady=15)
porttxt = Entry(window,width=25)

porttxt.grid(column=1,row=5,padx=10,pady=15)

btn2 = Button(window,text="Exit",command=window.destroy)
btn2.grid(column=1,row=10,pady=15,padx=10)

def connect():
    if porttxt.get()=="":
        messagebox.showerror("Error","All Fields Required.")
    p = porttxt.get()
    # device's IP address
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = int(p)
    # receive 4096 bytes each time
    # High buffer size used to send high data transfer
    BUFFER_SIZE = 1024 * 4 
    SEPARATOR = "<SEPARATOR>"
    # create the server socket
    # TCP socket used to transfer files
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    # accept connection if there is any
    messagebox.showinfo("Connect","Got a connection Request")
    client_socket, address = s.accept() 
    # if below code is executed, that means the sender is connected
    con = f"{address} is connected."
    messagebox.showinfo("Connected",con )
    # msg = Label(window, text=con)
    # msg.grid(column=1,row=12,padx=10,pady=15)

    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for _ in progress:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
        
    # close the client socket
    client_socket.close()
    # close the server socket
    s.close()
    





btn = Button(window,text='Receive File',command=connect)
btn.grid(column=1,row=7)



window.mainloop()













































# # device's IP address
# SERVER_HOST = "0.0.0.0"
# SERVER_PORT = 5001
# # receive 4096 bytes each time
# # High buffer size used to send high data transfer
# BUFFER_SIZE = 1024 * 4 
# SEPARATOR = "<SEPARATOR>"
# # create the server socket
# # TCP socket used to transfer files
# s = socket.socket()
# # bind the socket to our local address
# s.bind((SERVER_HOST, SERVER_PORT))
# # enabling our server to accept connections
# # 5 here is the number of unaccepted connections that
# # the system will allow before refusing new connections
# s.listen(5)
# print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# # accept connection if there is any
# client_socket, address = s.accept() 
# # if below code is executed, that means the sender is connected
# print(f"[+] {address} is connected.")
# 
# # receive the file infos
# # receive using client socket, not server socket
# received = client_socket.recv(BUFFER_SIZE).decode()
# filename, filesize = received.split(SEPARATOR)
# # remove absolute path if there is
# filename = os.path.basename(filename)
# # convert to integer
# filesize = int(filesize)
# # start receiving the file from the socket
# # and writing to the file stream
# progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# with open(filename, "wb") as f:
#     for _ in progress:
#         # read 1024 bytes from the socket (receive)
#         bytes_read = client_socket.recv(BUFFER_SIZE)
#         if not bytes_read:    
#             # nothing is received
#             # file transmitting is done
#             break
#         # write to the file the bytes we just received
#         f.write(bytes_read)
#         # update the progress bar
#         progress.update(len(bytes_read))
#     
# # close the client socket
# client_socket.close()
# # close the server socket
# s.close()
