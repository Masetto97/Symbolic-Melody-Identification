import socket, pickle
import os
s = socket.socket()
s.bind(('', 5000))
s.listen(1)
c,a = s.accept()
filetodown = open("./salidaprueba.mid", "wb")
while True:
   aux = c.recv(512)
   if aux[-3:] == 'fin':
        aux1 = aux[:-3]
        #data = pickle.loads(aux1)
        filetodown.write(aux1)
        break
   #data = pickle.loads(aux)
   filetodown.write(aux)
filetodown.close()
print("ARCHIVO RECIBIDO")
c.send("Thank you for connecting.")

print("PROCESANDO ARCHIVO")
os.system('conda run -n IA ./terminal_client.py --model model.pkl --extract mozart_k136.mxl edusalidaprueba1.mid')
os.system('ls')
c.shutdown(2)
c.close()
s.close()