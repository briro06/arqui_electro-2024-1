from multiprocessing import Process
from multiprocessing import Pool
import random
import math


def Elegir_Area(N:int,area:int)->int:
    muestras_dentro_area=0
    #Definimos las areas como los cuadrantes que conocemos en geometria
    #Esto quiere decir que area==1 será el primer cuadrante , area==2 segundo cuadrante y asi sucesivamente 
    if area==1:
        for i in range(N+1):
            x=random.uniform(0,1)
            y=random.uniform(0,1)
            r=math.sqrt(x**2+y**2)
            if(r<=1):
                muestras_dentro_area+=1
    elif area==2:
        for i in range(N+1):
            x=random.uniform(-1,0)
            y=random.uniform(0,1)
            r=math.sqrt(x**2+y**2)
            if(r<=1):
                muestras_dentro_area+=1
    elif area==3:
        for i in range(N+1):
            x=random.uniform(-1,0)
            y=random.uniform(-1,0)
            r=math.sqrt(x**2+y**2)
            if(r<=1):
                muestras_dentro_area+=1
    elif area==4:
        for i in range(N+1):
            x=random.uniform(0,1)
            y=random.uniform(-1,0)
            r=math.sqrt(x**2+y**2)
            if(r<=1):
                muestras_dentro_area+=1
    return muestras_dentro_area

if __name__=='__main__':
    N=10_000_000
    N_4=N//4
    pool=Pool(processes=4)
    #Cada uno de los resultados a continuación representarán el número de muestras dentro de cada área 
    resultado1,resultado2,resultado3,resultado4=pool.starmap(Elegir_Area,[(N_4,1),(N_4,2),(N_4,3),(N_4,4)])
    #Si sumamos todos los resultados obtendremos el número total de muestras dentro del circulo 
    total_dentro_circulo=resultado1+resultado2+resultado3+resultado4
    #Hacemos uso de la formula para poder hallar pi 
    calculo_pi=(total_dentro_circulo/N)*4
    #Imprimimos el valor de pi con 6 decimales de aproximación
    print(f"El valor de pi con {N} muestra es: {calculo_pi:0.6f}")