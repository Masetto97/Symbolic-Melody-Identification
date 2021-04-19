import socket, pickle
import os
import requests

#CREAMOS EL SOCKET
s = socket.socket()
s.bind(('', 5000))
s.listen(1)
c,a = s.accept()

#OBTENEMOS EL TITULO DE LA CANCION Y CALCULAMOS LAS SALIDAS
titulo = c.recv(512)
titulo_procesado = titulo+'_procesado.mid'
ruta='./Salidas_pruebas_TFM/'
print(titulo_procesado)

#RECIBIMOS EL FICHERO
filetodown = open('recibido.mid', "wb")
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

print(ruta+titulo_procesado)
#PROCESAMOS EL ARCHIVO Y LO GUARDAMOS EN EL DIRECTORIO CORRESPONDIENTE
print("PROCESANDO ARCHIVO")
os.system('conda run -n IA ./terminal_client.py --model model.pkl --extract  recibido.mid ' + titulo_procesado)

#ENVIAMOS EL ARCHIVO A DOCKER WEB PARA QUE LO GUARDE EN LA BBDD
#fichero = {'file1': open(titulo_final, 'rb')}
#r = requests.post('http://web:5000/procesado/'+titulo_procesado +'/'+ fichero)

#BORRAMOS EL ARCHIVO RECIBIDO AL ESTAR YA PROCESADO Y ENVIADO
os.system('rm recibido.mid')
os.system('ls')        
c.shutdown(2)
c.close()
s.close()
