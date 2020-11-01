"""
Client that sends the file (uploads)
"""

"""
Here we use network programming module to complete the task of sending and receiving files over network
we generally call it socket programming with python
Here are some module to import to support our code

Tkinter is the module to create gui applications.

socket module is useful to connect the system with another system to transfer files in connected network



"""
import socket
import tqdm
import os
import argparse
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# we assign Tk() root element to a variable window to use it later 
window = Tk()
# geometry is to give dimensions for Gui Window of our programs 
window.geometry('800x650')
# window.title to name the the gui with a title
window.title("Welcome to Material Sharing app")

# global declaration of some variables
global ip,por,file,msg1,progrssb


# Label is component to give labels in the Gui (to print some text on the gui)
mainlbl = Label(window,text='Enter Receivers Ip & Port number to Send File').grid(row=0,column=1,padx=10,pady=20)


filelbl = Label(window, text='Enter File Name: ').grid(column=0,row=2,padx=10,pady=20)
# Entry is the method used in tkinter to input from user in GUI application
file = Entry(window, width = 50)
# To give focus to the textfield
file.focus()
# grid method is used to place component in specified location in GUI
file.grid(column=1,row=2)


# label for input IPADDRESS
iplbl = Label(window, text='Enter Host Ip Address: ').grid(column=0,row=6,padx=10,pady=20)
# TEXTFIELD for to take input ipaddress
iptxt = Entry(window, width = 50)
# fix component at specified location
iptxt.grid(column=1,row=6)


# Label for PORT NUMBER
portlbl= Label(window, text="Enter Port Number: ").grid(column=0,row=10,padx=10,pady=20)
# TEXTFIELD to take Port number input
por = Entry(window, width = 50)
# fix component at specified location
por.grid(column=1,row=10)


# Function to get IP and PORT number from user
def getIpPort():
    #condition to check weather user input some text or not
    # .get() is a default function to extract input from TEXTFIELD of GUI
    if iptxt.get()=="" and por.get()=="" and file.get()=="":
        messagebox.showerror("Error","All Fields Required")
    i = iptxt.get()
    ipaddr = bytes(i,'utf-8')
    p = por.get()
    port = int(p)
    filename = file.get()
    send_file(filename,ipaddr,port)

# variable to seperate filename with extension while transfer
SEPARATOR = "<SEPARATOR>"
# Buffer_size to send or receive data at the datarate
global BUFFER_SIZE
# 1024bytes = 1kb here we used 4kb of datarate to transfer file
BUFFER_SIZE = 1024 * 4 #4KB

# function to Get file from user and Transfer 
def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # msg1 = Label(f"[+] Connecting to {host}:{port}")
    messagebox.showinfo("Info","Click ok to send file")
    s.connect((host, port))
    print("[+] Connected.")
    # send the filename and filesize to client(Receiver)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file Get progress for transfering file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    # OPEN FILE with python open function and read file in bytes mode 
    with open(filename, "rb") as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            
            
            # if progressb['value']==100:
            #     progressb.config(value=0)
            progress.update(len(bytes_read))

    # close the socket
    s.close()
    # message box will show message after successfull transfer
    messagebox.showinfo("Info","File Sent Successfully")
    
# Buttons to make some operations with user input and these are tkinter components 
btn1 = Button(window, text="Proceed",command=  getIpPort).grid(column=1,row=15)
btn2 = Button(window,text="Exit",command=window.destroy)
btn2.grid(column=1,row=17,pady=15,padx=10)
# msg = Label(window, text= send_file.msg1).grid(column=1,row=19,pady=10)
# this window.mainloop will loop the program until we exit
window.mainloop()













































# SEPARATOR = "<SEPARATOR>"
# BUFFER_SIZE = 1024 * 4 #4KB
# 
# def send_file(filename, host, port):
#     # get the file size
#     filesize = os.path.getsize(filename)
#     # create the client socket
#     s = socket.socket()
#     print(f"[+] Connecting to {host}:{port}")
#     s.connect((host, port))
#     print("[+] Connected.")
# 
#     # send the filename and filesize
#     s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# 
#     # start sending the file
#     progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
#     with open(filename, "rb") as f:
#         for _ in progress:
#             # read the bytes from the file
#             bytes_read = f.read(BUFFER_SIZE)
#             if not bytes_read:
#                 # file transmitting is done
#                 break
#             # we use sendall to assure transimission in 
#             # busy networks
#             s.sendall(bytes_read)
#             # update the progress bar
#             progress.update(len(bytes_read))
# 
#     # close the socket
#     s.close()
# 
# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser(description="Simple File Sender")
#     parser.add_argument("file", help="File name to send")
#     parser.add_argument("host", help="The host/IP address of the receiver")
#     parser.add_argument("-p", "--port", help="Port to use, default is 5001", default=21)
#     args = parser.parse_args()
#     filename = args.file
#     host = args.host
#     port = args.port
#     send_file(filename, host, port)
