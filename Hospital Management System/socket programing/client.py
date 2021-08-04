import socket
import json

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))




patient_id =int(input("enter the patient id: "))
p_name = input("Enter the Patient Name: ")
doctor_id=int(input("enter the doctor id: "))
d_name = input("Enter the doctor Name: ")
date = input("Enter the Date of patient checkup: ")
time = input("Enter the time of patient checkup: ")
report = input("Enter the  patient report: ")
tests = input("Enter name of tests and report: ")
perception= input("Enter the perception: ")

x = {'patient_id': patient_id, 'p_name': p_name,  'doctor_id': doctor_id, 'd_name': d_name,'date': date, 'time': time, 'report': report, 'tests': tests,'perception':perception}
y = json.dumps(x)
send(y)