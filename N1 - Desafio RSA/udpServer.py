from socket import *
from random import *
from math import *
from rsa import RSA

rsa = RSA()


serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print ("UDP server\n")
    
def main():
    bit_size = 4096
    _, private_key = generate_keypair(bit_size)
    
    while True:
        encrypted_data, client_address = server_socket.recvfrom(4096)
        encrypted_message = list(map(int, encrypted_data.decode('utf-8').split(',')))

        decrypted_message = RSA.decrypt(private_key, encrypted_message)
        
        print("Mensagem Recebida:", decrypted_message)

# if __name__ == "__main__":
#     main()

