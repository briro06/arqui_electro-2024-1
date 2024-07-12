import random
import math

if __name__=='__main__':
    #Definimos el valor de N
    N=10_000_000
    #Inicializamos el valor de la variable que contará el numero de muestras que se encuentren dentro del circulo 
    muetras_dentro_circulo=0
    #Iteramos en el número de muestras que definimos
    for i in range(N+1):
        #Definimos la coordenada x de manera aleatoria
        x=random.uniform(-1,1)
        #Definimos la coordenada y de manera aleatoria
        y=random.uniform(-1,1)
        #Ahora calculamos su radio o hipotenusa
        r=math.sqrt(x**2+y**2)
        #Para verificar que se encuentre dentro del circulo tenemos que probar que el radio o hipotenusa es menor a 1
        if r<=1:
            #Si se cumple nuestra condición aumentamos en 1 el numero de muestras dentro del circulo
            muetras_dentro_circulo+=1

    #Calculamos el valor de pi en base a la formula 
    valor_pi=(muetras_dentro_circulo/N)*4
    #Imprimimos el valor de pi con 6 decimales de aproximación
    print(f"El valor de pi con {N} muestra es: {valor_pi:0.6f}")