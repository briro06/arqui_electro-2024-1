import time 
import asyncio
rutas_posibles = [
	"LPC",
	"LPAHC",
	"LPAOHC",
	"LOAPC",
	"LOAHC",
	"LOHC",
	"LOHAPC",
	"LAPC",
	"LAOHC",
	"LAHC"
]

distancias = {
	"LP": 14,
	"LA": 10,
	"LO": 8,
	"PC": 18,
	"PA": 3,
	"OA": 25,
	"OH": 5,
	"AP": 3,
	"AO": 25,
	"AH": 2,
	"HA": 2,
	"HC": 10
}

tiempos_rutas=list()

async def Evalua_Tiempo_Ruta(ruta_posible:str):
    i=1
    cadena_ruta=''
    tiempo_trayectoria=0

    for let in ruta_posible:
        #Caso de una sola letra
        if i==1:
            cadena_ruta=cadena_ruta+let
        #Caso para dos letras
        elif i==2:
            cadena_ruta=cadena_ruta+let
            tiempo_trayectoria=tiempo_trayectoria+distancias[cadena_ruta]
            await asyncio.sleep(distancias[cadena_ruta]/1000) #Convertimos la espera en ms
        #Caso para más de dos letras , tomaremos la cadane_ruta como las ultimas dos letras para evaluar el tiempo de la trayectoria
        elif i>2:
            cadena_ruta=cadena_ruta[1:] #ultimas dos letras
            cadena_ruta=cadena_ruta+let
            tiempo_trayectoria=tiempo_trayectoria+distancias[cadena_ruta]
            await asyncio.sleep(distancias[cadena_ruta]/1000) #Convertimos la espera en ms
        i=i+1

    tiempos_rutas.append(tiempo_trayectoria)

async def Evaluacion_Rutas():
    await asyncio.gather(*(Evalua_Tiempo_Ruta(rut) for rut in rutas_posibles))

    print(f"La ruta más corta es {rutas_posibles[tiempos_rutas.index(min(tiempos_rutas))]} con una duración de {min(tiempos_rutas)} horas")

if __name__ == "__main__":
	asyncio.run(Evaluacion_Rutas())
     


#En caso se implmenten Threads , el programa que seria más eficiente seria cuando trabajaos asincronamente debido a
#que el multihilo aprovecha su concurrencia cuando trabajamos con operaciones de E/S o interacción con el usuario, como este no es el caso
#lo más conveniente seria trabaja asincronamente
     