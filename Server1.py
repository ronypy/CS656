import socket
import threading
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def create_servers():
   server_1=[]
    #client_1=[]
   #client_2=[]
   #client_3=[]
   for x in range(1,14):
      server_1.append(x)

   return server_1


def SERVER_1(server_1):
  s1= random.choice(server_1)
  server_1.remove(s1)
  return s1, server_1

# Server chooses the client who sent the highest value card by comparing
def comparator(c1_value, c2_value, c3_value):
  c = [c1_value, c2_value, c3_value]
  max_value_position = [i for i, x in enumerate(c) if x == max(c)]
  return max_value_position

  
# Server increments the score of that client with the value of the card that was advertised by the server.
def score_calculation(score,server_return_value, max_value_position):
  length= len(max_value_position)
  if length==1:
    score[max_value_position[0]]=score[max_value_position[0]]+server_return_value
  elif length ==2:
    for i in range(1):
      score[max_value_position[0]]= score[max_value_position[0]]+server_return_value
      score[max_value_position[1]]= score[max_value_position[1]]+server_return_value
  else:
    score=[i+ server_return_value for i in score]
  return score


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    data_client = []
    connected = True
    while connected:
        #ser = create_servers()
        #s1, server_1 = SERVER_1(ser)
        #conn.send(str(s1).encode(FORMAT))
        
        msg = conn.recv(SIZE).decode(FORMAT)
        #for i in range:
        data_client.append(msg)
           #i=i+1

        print(data_client)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        msg = f"Msg received: {msg}"
        #msg = wikipedia.summary(msg, sentences=1)
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    #data_client = []
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()