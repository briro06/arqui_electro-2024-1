from multiprocessing import Process
from multiprocessing import Pool
import time 

#Definimos la función que calcula el factorial de manera serial
def Funcion_Serial(N:int)->int:
    #Inicializamos la productoria en 1 
    factorial=1
    for i in range(1,N+1):
        factorial=factorial*i

    return factorial

#Definimos la función que nos ayudarra para hallar el factorial de manera paralela
def Calculo_Factorial_Paralelo(lim_inferior:int,lim_superior:int)->int:
    #Tendra como argumentos de entrada el limite inferior y superior
    fac=1
    for i in range(lim_inferior,lim_superior+1):
        fac=fac*i
    return fac


def Funcion_Multiprocesos(N)->int:
    #Dividimos el número N en dos partes 
    N_2=N//2
    #Declaramos pool que nos ayudará a obtener los valores para cada proceso por separado
    pool=Pool(processes=2)
    #Declaramos los argumentos que tendremos para cada proceso, donde el primer argumento será la tupla (1,N_2) el siguiente (N_2+1,N)
    argumentos=[(1,N_2),(N_2+1,N)]

    #Hacemos uso de starmap para poder obtener los resultados de la función cuando tengamos más de un argumento , como es el caso nuestro donde tenemos 2
    #pool.starmap() es bastante similar a la de pool.map() solamente que map solo acepta una tupla de argumento 
    resultado1,resultado2=pool.starmap(Calculo_Factorial_Paralelo,argumentos)

    #Multiplicamos ambos resultados para obtener el total
    resultado_total = resultado1 * resultado2
    return resultado_total


if __name__=='__main__':
    N=80_000

    #Medimos el tiempo de ejecución de la función Serial y guardamos el valor obtenido 
    i1=time.perf_counter()
    res_serial=Funcion_Serial(N)
    f1=time.perf_counter()
    tex1=f1-i1
    print(f"El tiempo de ejecución de la función de forma serial es {tex1:0.4f}")

    #Medimos el tiempo de ejecución de la función paralela y guardamos el valor obtenido
    i2=time.perf_counter()
    res_multi=Funcion_Multiprocesos(N)
    f2=time.perf_counter()
    tex2=f2-i2
    print(f"El tiempo de ejecución de la función usando multiprocessing es: {tex2:0.4f}")

    #Calculamos el speedup, dividiendo el tiempo de ejecución de la función de forma paralela entre el tiempo de ejecución de la función en forma serial
    speedup=tex1/tex2
    print(f"El speed up resultante es: {speedup:0.4f}")

    #Hacemos uso de la función assert() gracias al siguiente link https://realpython.com/python-assert-statement/ 
    #Donde menciona que la sintaxis de assert es la siguiente assert expresion, mensaje
    #el mensaje será impreso en caso no se cumpla la veracidad de la expresion
    assert res_serial == res_multi, "Los resultados no son iguales"
    



