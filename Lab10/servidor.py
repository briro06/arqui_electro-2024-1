import asyncio
import json
import socket


SOCKET_BUFFER = 1024


#Definimos la función que tiene como parametro de entrada el código del alumno
#y retorna una lista con las notas del alumno
def busca_info(codigo: str) -> list[str]:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    contenido = contenido.split("\n")
    #print(f"longitud de contenido: {len(contenido)}")
    for fila in contenido:
        if codigo in fila:
            return fila.split(",") 
    return list()


#Empaquetamos los datos
def empaqueta_datos(notas: list[str],codigo: str,eval:str) -> dict:
    #Evalualamos la condición para el código
    match codigo:
        #En caso sea promedio
        case"promedio":
            #Vamos a evaluar el promedio de que evaluación pide
            match eval:
                case'lab1':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[1])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab2':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[2])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab3':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[3])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab4':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[4])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab5':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[5])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab6':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[6])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab7':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[7])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab8':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[8])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab9':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[9])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab10':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[10])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab11':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[11])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'lab12':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[12])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'e1':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[13])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
                case'e2':
                    nota_prom=0
                    #Realizamos una iteración del total de alumnos
                    for idx in range(10):
                        codigo_base=20240000
                        codigo_alumno=f"{codigo_base + idx}"
                        notas_alumno=busca_info(codigo_alumno)
                        nota_prom=nota_prom+int(notas_alumno[14])
                    nota_prom=nota_prom/10
                    r_dict={'nota':nota_prom,"error":'false'}
        case _:
            match eval:
                case'lab1':
                    r_dict = {"nota": int(notas[1]),"error": "false"}
                case'lab2':
                    r_dict = {"nota": int(notas[2]),"error": "false"}
                case'lab3':
                    r_dict = {"nota": int(notas[3]),"error": "false"}
                case'lab4':
                    r_dict = {"nota": int(notas[4]),"error": "false"}
                case'lab5':
                    r_dict = {"nota": int(notas[5]),"error": "false"}
                case'lab6':
                    r_dict = {"nota": int(notas[6]),"error": "false"}
                case'lab7':
                    r_dict = {"nota": int(notas[7]),"error": "false"}
                case'lab8':
                    r_dict = {"nota": int(notas[8]),"error": "false"}
                case'lab9':
                    r_dict = {"nota": int(notas[9]),"error": "false"}
                case'lab10':
                    r_dict = {"nota": int(notas[10]),"error": "false"}
                case'lab11':
                    r_dict = {"nota": int(notas[11]),"error": "false"}
                case'lab12':
                    r_dict = {"nota": int(notas[12]),"error": "false"}
                case'e1':
                    r_dict = {"nota": int(notas[13]),"error": "false"}
                case'e2':
                    r_dict = {"nota": int(notas[14]),"error": "false"}
    return r_dict



def procesa_mensaje(dato: bytes) -> dict:
    try:
        msg_cliente = json.loads(dato)
        print(f"Mensaje del cliente: {msg_cliente}")
        #Si tenemos el valor de 'codigo' y 'eval' en nuestras llaves
        if "codigo" in msg_cliente.keys() and "eval" in msg_cliente.keys():
            print("Codigo y eval existen")
            #Si nuestro valor de la llave código es diferente a promedio entonces será el código
            if(msg_cliente["código"]!='promedio'):
                notas = busca_info(msg_cliente["codigo"])
            else:
                notas=[0,0]
            if len(notas) > 0:
                msg_respuesta = empaqueta_datos(notas, msg_cliente['código'],msg_cliente['eval'])
            else:
                msg_respuesta = {"nota": 20, "error": "false"}
        else:
            msg_respuesta = {"estado": "error", "mensaje": "Solicitud enviada en formato incorrecto"}
    except json.decoder.JSONDecodeError:
        msg_respuesta = {"estado": "error", "mensaje": "No se pudo decodificar el mensaje de JSON"}

    print(f"Respuesta: {msg_respuesta}")

    return msg_respuesta


async def handle_client(reader, writer):
    print("Cliente conectado")
    msg_bytes = await reader.read(SOCKET_BUFFER)
    print(f"Recibi {msg_bytes}")
    if msg_bytes:
        print("msg_bytes tiene data, procesando")
        msg_respuesta = procesa_mensaje(msg_bytes)
        print(f"Enviando respuesta: {msg_respuesta}")
        msg_respuesta_str = json.dumps(msg_respuesta)

        await writer.write(msg_respuesta_str.encode("utf-8"))
        await writer.drain()

    writer.close()
    await writer.wait_closed()
    print("conexion cerrada")



async def main():
    server_adddress = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_adddress[0], server_adddress[1])

    async with server:
        print("Empezando servidor...")
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())