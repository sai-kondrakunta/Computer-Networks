import socket
import threading
import pandas
import json

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def server_function():
    df = pandas.read_csv('DATABASE_HOSPITAL.csv')
    patient_id = input("Enter the patient_id")
    for i in range(len(df)):
        if(df.iloc[i, 0] == patient_id):
            print(df.iloc[i])
            print("\n")



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            df = pandas.read_csv('DATABASE_HOSPITAL.csv')

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            userinput = json.loads(msg)
            print(userinput)
            print(f"[{addr}] {userinput}")

            df2 = {'patient_id': userinput['patient_id'], 'p_name': userinput['p_name'],'doctor_id': userinput['doctor_id'], 'd_name': userinput['d_name'],
                   'date': userinput['date'], 'time': userinput['time'], 'report': userinput['report'], 'tests': userinput['tests'], 'perception': userinput['perception']}
            df = df.append(df2, ignore_index=True)
            df.to_csv('DATABASE_HOSPITAL.csv', index=False)
            print(df)

            conn.send("Values are Updated".encode(FORMAT))

    conn.close()


def start():

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    x = int(input("press 1- server function"))
    if x == 1:
        server_function()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()