import socket
import random


IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def create_clients():
   #server=[]
    #client_1=[]
   #client_2=[]
   client_3=[]
   for x in range(1,14):
      #server.append(x)
      #client_1.append(x)
      #client_2.append(x)
      client_3.append(x)
   return client_3

#client_3= [1]
def CLIENT_3(c3, client_3):
  c3= random.choice(client_3)
  client_3.remove(c3)
  return c3, client_3



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()