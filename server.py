import socket, pickle
import os
import requests
s = socket.socket()
s.bind(('', 5000))
s.listen(1)
c,a = s.accept()
titulo = c.recv(512)
titulo_final='./'+titulo+'_procesado.mid'
print(titulo_final)
filetodown = open('./recibido.mid', "wb")
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
#os.system('conda run -n IA ./terminal_client.py --model model.pkl --extract  recibido.mid ' + titulo_final)
#os.system('ls')

ficheros = {'file1': open('./Salidas_pruebas_TFM/albinoni_adagio_procesado.mid', 'rb')}
r = requests.post('http://localhost:5000/procesado/', files=ficheros)

#x = requests.post('172.18.0.4:5000/index')

c.shutdown(2)
c.close()
s.close()
