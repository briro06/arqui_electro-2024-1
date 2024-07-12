import asyncio
import json
from random import randint, random
import csv


async def send(writer,msg):
    msg_envio_bytes=json.dumps(msg).encode("utf-8")
    writer.write(msg_envio_bytes)
    await writer.drain()

async def recv(reader):
    print("Esperando respuesta")
    result_bytes=await reader.readline
    result=json.loads(result_bytes)
    return result

async def cliente():
    server_address = ("localhost", 5500)
    print(f"Conectando a {server_address[0]}:{server_address[1]}")
    reader, writer = await asyncio.open_connection(server_address[0], server_address[1])
    print("Conectado")
    codigo_base=20240000
    for idx in range(10):
        msg_dict = {"codigo": f"{codigo_base+ idx}",'eval':'e1'}
        await send(writer,msg_dict)

    res = await recv(reader)

    print("cerrando la conexion")
    writer.close()
    await writer.wait_closed()

    return res
async def main():
    res = await asyncio.gather(*(cliente()))

    return res


if __name__ == '__main__':
    notas = asyncio.run(main())
    #Convertimos a arhivo csv
    with open("final.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(zip(*notas))
        
