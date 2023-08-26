import socket
import random
import math
from rsa import RSA

def main():
    bit_size = 4096
    _, private_key = generate_keypair(bit_size)

    serverPort = 12500
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("",serverPort))
    print ("UDP server\n")

    while True:
        encrypted_data, client_address = server_socket.recvfrom(4096)
        encrypted_message = list(map(int, encrypted_data.decode('utf-8').split(',')))

        decrypted_message = rsa.decrypt(private_key, encrypted_message)
        rsa = RSA()
        print("Mensagem Recebida:", decrypted_message)

if __name__ == "__main__":
    main()

