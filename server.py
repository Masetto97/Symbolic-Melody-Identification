import socket, pickle
import os
import requests

while True:
   #CREAMOS EL SOCKET
   s = socket.socket()
   s.bind(('', 5000))

   s.listen(1)
   c,a = s.accept()

   #OBTENEMOS EL TITULO DE LA CANCION Y CALCULAMOS LAS SALIDAS
   ruta='./Salidas_pruebas_TFM/salida.mid'

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

   #PROCESAMOS EL ARCHIVO Y LO GUARDAMOS EN EL DIRECTORIO CORRESPONDIENTE
   print("PROCESANDO ARCHIVO")
   os.system('conda run -n IA ./terminal_client.py --model model.pkl --extract  recibido.mid ' + ruta)

   #ENVIAMOS EL ARCHIVO A DOCKER WEB PARA QUE LO GUARDE EN LA BBDD
   fichero = {'file1': open(ruta, 'rb')}
   r = requests.post('http://web:5000/procesado', files=fichero)

   #BORRAMOS EL ARCHIVO RECIBIDO AL ESTAR YA PROCESADO Y ENVIADO
   os.system('rm recibido.mid')
   os.system('rm ruta')
   print("PROCESO TERMINADO") 
   c.shutdown(2)
   c.close()
   s.close()
