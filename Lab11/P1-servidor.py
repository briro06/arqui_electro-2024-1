from threading import Thread
import json 
import socket 
import time

fila=list()
#global client_socket,client_address

#Thread número 1 para leer archivo
def lectura_datos():
    #global client_socket,client_address

    #Conectamos al cliente
    #client_socket, client_address = sock.accept() #se conecta al cliente
    #print(f"Conexion de {client_address[0]}:{client_address[1]}")

    global fila
    with open("partesdeElectronica.csv",'r') as f:
        #Saltamos la primera fila
        next(f)
        #Leemos el resto del archivo
        data_base=f.read()
    #Convertimos cada fila en una lista a excepción de la cabezera
    fila=data_base.split('\n')

#Thread para enviar los datos al cliente
def client_handler(client_socket,client_address):
    i=0
    global fila
    try:
        while True:
            if i<len(fila):
                if fila[i]: #Nos aseguramos que la fila exista
                    contenido=fila[i].split(";")
                    #Convertimos la lista en un diccionario para poder enviarlo
                    contenido_dict=dict(contenido)
                    #Enviamos el contenido de la lista , es decir de cada fila
                    client_socket.sendall(json.dumps(contenido_dict).encode("utf-8"))
                    #Pasamos a la siguiente fila para enviar los datos
                    i=i+1
                    #Intervalo de 1 segundo
                    time.sleep(1)
            else:
                print("No hay más datos")
                break
    except ConnectionResetError:
        print("Cerrando el servidor...")
    finally:
        print("Cerrando el servidor")
        client_socket.close()


if __name__=='__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 8000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        #print("Esperando conexiones...")

        try:
            client_socket, client_address = sock.accept() #se conecta al cliente
            print(f"Conexion de {client_address[0]}:{client_address[1]}")
    
            #Declaremos nuestros dos hilos
            t1  = Thread(target=lectura_datos, args=())
            t2 = Thread(target=client_handler, args=(client_socket, client_address))

            #Inicia le ejecución de los hilos
            t1.start() 
            t2.start()
            #Espera a que ambos hilos terminen ejecución
            t1.join()
            t2.join()


        except KeyboardInterrupt: #en caso ocurrre error al conectarse al cliente
            print("Cerrando el servidor ...")
            break

