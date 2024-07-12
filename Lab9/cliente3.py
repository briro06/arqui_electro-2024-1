import json
import socket
import numpy as np

SOCK_BUFFER = 1024


if __name__ == '__main__':
    #Declaramos una lista para realizar las mediciones de los tiempos
    lista_E_S=list()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)
    print(f"Conectandonos al servidor en {server_address[0]} en el puerto {server_address[1]}\n")
    sock.connect(server_address)
    print("Se logró conectar al servidor\n")
    msg = {"comando": "corte", "modo": "","umbral":"220.4"}

    for i in range(9):
        ti=time.perf_counter()
        sock.sendall(json.dumps(msg).encode("utf-8"))
        #Vamos a recibir el formato de texto .json 
        dato = sock.recv(SOCK_BUFFER)
        tf=time.perf_counter()
        sock.close()
        #print(f"Recibí: {dato}")
        lista_E_S.append(1e6*(tf-ti))

    #Vamos a imprimir los tiempo de E/S que se obtiene en el cliente 3, ya que estamos enviando datos y tambien obtenemos un retorno es por ello que se considera
    #como una operación de entrada/salida a nuestro cliente 3 , para este expermiento se tomo en consideración 10 valores
    print("Los valores de los tiempos de ejecución para operción de entrada/salida para el cliente 3 en microsegundos es: \n")
    print(lista_E_S)

    #Tomaremos la mediana de los 10 tiempos de ejecución que tenemos , ya que como sabemos la mediana es un buena medida de rendimiento debido a que no es suceptible a valores extremos o outliers
    mediana=np.median(lista_E_S)
    print(f"La mediana de los tiempos de ejecución es: {mediana}")