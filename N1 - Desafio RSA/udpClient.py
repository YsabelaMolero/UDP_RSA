import socket
import random
from rsa import RSA

client_address = ("10.1.70.16", 12500)
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
rsa = RSA()
print("UDP Client\n")

def main():

    public_key = (65537, 29639926667775503588514708722185371740256285986530679994753696186941393044029618984677159940567928796390009890419382501101828707940485314087426088844282127629996381702036605836035548601021641365511259888282193257798322577422267968425850989122198193544256416307615264166519518309319486250678151005031804371948177327248107683401979737823449034307147527398141942934219605296472484584085346221977970301041402140094982075226527928526219260971421521038049358964723188370481901459020877311934776262103705432262337972475219127998713067026984606080224821342620215179593106283037613836991794076047036012382183)
    message = "The information security is of significant importance to ensure the privacy of communications"
    
    encrypted_message = rsa.encrypt(public_key, message)
    encrypted_data = ','.join(map(str, encrypted_message)).encode('utf-8')
    print(message)
   
    client_socket.sendto(encrypted_data, client_address)
    clientSocket.close()

if __name__ == "__main__":
    main()

# while 1:
#     message = input("Input message: ")
#     if message == "exit":
#         break
#     else:

#         public_key = (65537, 29639926667775503588514708722185371740256285986530679994753696186941393044029618984677159940567928796390009890419382501101828707940485314087426088844282127629996381702036605836035548601021641365511259888282193257798322577422267968425850989122198193544256416307615264166519518309319486250678151005031804371948177327248107683401979737823449034307147527398141942934219605296472484584085346221977970301041402140094982075226527928526219260971421521038049358964723188370481901459020877311934776262103705432262337972475219127998713067026984606080224821342620215179593106283037613836991794076047036012382183)
#         message = ce.encrypt(message, 4)
#         encrypted_message = rsa.encrypt(public_key, message)
#         encrypted_data = ','.join(map(str, encrypted_message)).encode('utf-8')
#         print(message)
#     client_socket.sendto(encrypted_data, client_address)
# clientSocket.close()