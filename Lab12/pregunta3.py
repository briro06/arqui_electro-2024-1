import math
from multiprocessing import Process
from multiprocessing import Pool

def Funcion_Serial(N:int)->list:
	lista_resultante=list()
	raiz_N=int(math.sqrt(N))
	for i in range(2,raiz_N+1):
		if N%i==0:
			num_primo1=i
			num_primo2=N//i
	lista_resultante.append(num_primo1)
	lista_resultante.append(num_primo2)
	return lista_resultante

def Factor_Primo(inf:int,sup:int,N:int)->int:
	for i in range(inf,sup+1):
		if N%i==0:
			return i

def Funcion_Paralela(N):
	N_2=N//2
	lista_retornante=list()
	inf=int(math.sqrt(N_2))
	sup=int(math.sqrt(N))

	pool=Pool(processes=2)
	num1,num2=pool.starmap(Factor_Primo,[(inf,sup,N),(inf,sup,N)])
	#Si los numeros son iguales entonces tendre que hallar el siguiente
	if num1==num2:
		num3=int(N/num1)
	lista_retornante.append(num1)
	lista_retornante.append(num3)
	return lista_retornante

if __name__=='__main__':
	N=1000000016000000063
	lista_serial=list()
	lista_paralela=list()

	lista_serial=Funcion_Serial(N)
	print(f"El número N será la multiplicacióm de los siguientes factores primos de manera serial: {lista_serial}")

	lista_paralela=Funcion_Paralela(N)
	print(f"El número N será la multiplicacióm de los siguientes factores primos utilizando multiprocessing: {lista_paralela}")

	