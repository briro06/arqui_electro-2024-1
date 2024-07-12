import json 
import sockets

#Definimos el tamaño del buffer que vamos a utilizar
SOCK_BUFFER=1024

#Vamos a definar uan sola función principal que nos retornará el elemento que deseemos segun sea el caso
#Nuestro diccionario que recibiremos será
#"comando" puede tomar 3 valores : "medidores" ,"corte" o "sobrevoltaje"
#"modo" puede tomar 2 valores : "precesado" o "lista" siempre y cuando el comando sea medidas
#"umbral" el valor que deseemos siempre y cuando el comando sea corte o sobrevoltaje

def Funcion_Principal(mediciones:list[str],voltajes:list[str],comando:str,modo:str,umbral:str)->dict:
    r_dict=dict()
    num_voltajes_corto=0
    num_voltajes_sobrevoltaje=0
    match comando:
        case"medidores":
            match modo:
                case"procesado":
                    #Para contar el numero de medidores debemos tener en cuenta que habrá algunos medidores que se repitan
                    #Por ello el comando set te permite crear una lista con elementos sin repetirse 
                    #Una vez utilizado el comando set tenemos que calcular el tamaño o longitud de ese nueva lista 
                    #es por ello que utilizamos el comando len
                    num_medidores=len(set(medidores))
                    r_dict={"estado":"exito","valor":num_medidores,"lista":"","mensaje":""}
                case"lista":
                    #Ahora si nuestro case es de lista vamos a retornar la lista que obtuvimos 
                    #Definimos el diccionario para este caso
                    r_dict={"estado":"exito","valor":"","lista":medidores,"mensaje":""}                    
        case"corte":
            for i in range(len(voltajes)):
                #Obtengo de 3 en 3 los valores de voltaje 
                for j in range(2):
                    if(float(voltajes[i])<float(umbral)):
                        #Si se cumple la condición el número de voltajes por debajo del umbral aumenta
                        num_voltajes_corto+=1
                        break
            #Definimos el dictionario que será retornado
            r_dict={"estado":"exito","valor":num_voltajes_corto,"lista":"","mensaje":""}
        case"sobrevoltaje":
            for i in range(len(voltajes)):
                for j in range(2):
                    if(float(voltajes[i])>float(umbral)):
                        #Si se cumple la condición el número de voltajes por encima del umbral aumenta
                        num_voltajes_sobrevoltaje+=1
                        break
            #Definimos el dictionario que será retornado
            r_dict={"estado":"exito","valor":num_voltajes_sobrevoltaje,"lista":"","mensaje":""}
    return r_dict

#A parte de la primera función crearemos otra función que nos retorne la lista de mediciones y de voltajes
def Mediciones_Voltj(archivo:str):
    #Abrimos el archivo en modo lectura
    with open(archivo,'r') as f:
        #Nos saltaremos la cabecera con el comando next
        next(f)
        #En cada ciclo de iteración tenemos una linea del archivo
        for idx in f:
            #Por cada ciclo de iteración se crea una lista con los elementos de cada linea que vaya iterando
            arr_f=idx.split(',')
            #Creamos la lista medideores la cual será el elemento 1(identicador del medidor) de cada lista creada en cada iteración
            medidores.append(arr_f[1])
            #Para los valores de los voltajes debemos tener en cuenta que tenemos 3 mediciones por cada linea
            #Entonces tendrán que ser las columnas 3,4 y 5 
            voltajes.append(arr_f[3])
            voltajes.append(arr_f[4])
            voltajes.append(arr_f[5])
    return medidores,voltajes

if __name__=='__main__':
    #Definimos las listas de voltajes y medidores que vamos a utilizar
    voltajes=list()
    medidores=list()
    #Definimos el nombre del archivo.csv
    archivo_csv=f"mediciones_trifasicas_junio.csv"
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)
    print(f"Levantando el servidor en {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(5)
    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion de {client_address[0]}:{client_address[1]}")
        try:
            while True:
                #Recibimos el dato
                dato = conn.recv(SOCK_BUFFER)
                #Si hemos recibido algo en la variable dato entonces
                if dato:
                    #Imprimiremos lo que hemos recibido
                    print(f"Recibí: {dato}")
                    #Ahora convertiremos la cadena de texto que se encuentra en formato .json a un diccionario en python
                    d = json.loads(dato)

                    if "comando" in d.keys() and "modo" in d.keys() and "umbral" in d.keys():
                        medidores,voltajes=Mediciones_Voltj(archivo_csv)
                        msg_dict=Funcion_general(medidores,voltajes,d["comando"],d["modo"],d["umbral"])
                        #Imprimo el diccionario obtenido
                        print(msg_dict)
                    else:
                        msg_dict = {"estado": "error", "mensaje": "Solicitud enviada en formato incorrecto"}
                    #Vamos a convertir el diccionario msg_dict en una cadena de texto .json y esa cadena de texto la convertimos en bytes
                    conn.sendall(json.dumps(msg_dict).encode("utf-8"))
                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente cerró la conexión de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()