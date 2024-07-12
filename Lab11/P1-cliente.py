from threading import Thread
import socket
import json
import numpy as np

datos = list()
costo_total = list()
clasificacion = list()
conteo_costo_elevado= 0
conteo_costo_elevado_paso= 0
conteo_costo_bajo= 0

SOCK_BUFFER=1024

#Primer thread se encarga de recibit los datos
def recibir_datos_del_servidor(sock):
    global datos

    try:
        while True:
            #Recibimos la data en formato de texto .json
            data_recibida=sock.recv(SOCK_BUFFER)
            if data_recibida:
                #Convertimos el formato de texto .json a un diccionario
                data_recibida_actual=json.loads(data_recibida)
                #Ahora convertimos a una lista el diccionario 
                data_lista=list(data_recibida_actual)
                #Agregamos a la lista datos cada fila 
                datos.append(data_lista)
                print(datos)
            else:
                break
    finally:
        print("Cerrando socket")
        sock.close()

#Segundo thread que se encarga de procesar los datos
def procesar_datos():
    global costo_total
    global clasificacion

    global conteo_costo_elevado
    global conteo_costo_elevado_paso
    global conteo_costo_bajo

    i=1
    print(f"------------------------Nombre: {datos[i][1]} --------------------------")
    #Nuestra lista datos será una lista que contenga listas dentro de el donde cada sublista es 
    #una fila del archivo partesdeElectronica.csv

    if datos[i]:
        #Debemos tener en cuenta que la columna 0 es ID, columna 1 es Nombre
        #columna 2 es Número de Partes y asi sucesivamente

        #Definimos el costo y lo convertimos a float ya que se encuentra en string
        costo=float(datos[i][5])
        #Definimos cantidad y convertimos a entero ya que se encuentra en string
        cantidad=int(datos[i][3])
        #Realizamos lo mismo para el peso y convertimos a gramos
        peso=float(datos[i][4])/10000

        #Ahora calculamos el costo total de cada fila y vamos agregandolo a la lista
        costo_total.append(costo*cantidad)

        print(f"Costo total: {costo_total[i]}")
        #Evaluamos las condiciones
        if costo_total[i]<=75:
            print('Clasificación por costo:Costo bajo')
            conteo_costo_bajo+=1
        elif costo_total[i]>75.0 and costo_total[i]<=149.9:
           print('Clasificación por costo:Costo regular')
        elif costo_total[i]>=150 and costo_total[i]<=199.9:
            print('Clasificación por costo:Costo alto')
        else:
            print('Clasificación por costo:Costo elevado')
            conteo_costo_elevado+=1
            if peso>2000:
                conteo_costo_elevado_paso+=1
    #Imprimimos el número de componentes para cada uno de los casos
    print(f'Número de componentes con costo elevado: {conteo_costo_elevado}')
    print(f"Número de componentes con costo elevado y con peso mayor a 200g: {conteo_costo_elevado_paso}")
    print(f"Número de componentes con costo bajo {conteo_costo_bajo}")
    

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)  # Dirección IP y puerto del servidor

    print(f"Conectandonos al servidor en {server_address[0]} en el puerto {server_address[1]}")

    sock.connect(server_address)
    t1=Thread(target=recibir_datos_del_servidor, args=(sock,))
    t2=Thread(target=procesar_datos, args=())
    #Declaramos y ejecutamos los hilos 
    t1.start()
    t2.start()
    #Esperamos a que se ejecuten 
    t1.join()
    t2.join()