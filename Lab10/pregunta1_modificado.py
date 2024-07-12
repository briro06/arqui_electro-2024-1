import asyncio
import httpx
import time 

urls = ["https://www.amazon.com", "https://www.nvidia.com/en-us/", "https://www.openai.com",
        "https://www.python.org", "https://www.microsoft.com/en-us/", "https://www.google.com",
        "https://www.wikipedia.com", "https://x.com/"]

async def async_fetch(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text 

def sync_fetch(url:str) -> str:
    with httpx.Client() as client:
        response = client.get(url)
    return response.text

#Parte a)
def sync_scraper(urls: list[str]) -> list[str]:
    #Creamos nuestra lista que será neustro retorno
    lista_http=list()
    #Iteramos sobre nuestras direcciones de URL
    for url in urls:
        lista_http.append(sync_fetch(url))
    return lista_http

#Parte b)
async def async_scraper(urls: list[str])-> list[str]:
    lista_urls=list()
    #Iteramos sobre nuestras direcciones de URL
    for url in urls:
        dir= async_fetch(url)
        #Añadimos a la lista los valores de task en cada iteración
        lista_urls.append(dir)
        #Ejecutamos todas las corutinas y guardamos sus valores en la lista asincrona
    lista_http_async = await asyncio.gather(*lista_urls, return_exceptions=True)

    return lista_http_async

if __name__=="__main__":
    # Version sincrona
    #print(sync_fetch(urls[0]))

    # Version asincrona
    #print(asyncio.run(async_fetch(urls[0])))

    #Parte c)
    #Calculamos el tiempo de ejecución de la función asincrona 
    i1 = time.perf_counter()
    html_contentenido1 =asyncio.run(async_scraper(urls))
    f1 = time.perf_counter()
    tex1=f1-i1
    print(f"El tiempo de ejecución de la función asincrona es: {tex1:0.4f}")
    print("Longitudes de manera asincrona")
    for contenido in html_contentenido1:
        print(len(contenido))

    print('\n')
    
    #Calculamos el tiempo de ejecución de la función sincrona
    i2 = time.perf_counter()
    html_contenido2 = sync_scraper(urls)
    f2 = time.perf_counter()
    tex2=f2-i2
    print(f'El tiempo de ejecución de la función sincrona es: {tex2:0.4f}')
    print("Longitudes de manera sincrona")
    for contenido in html_contenido2:
        print(len(contenido))

    #Calculamos el speedup de nuestra función
    speedup=tex2/tex1
    print(f"El speed up es el siguiente: {speedup:0.3f}")

    #Los resultados en la parte c son los esperados ya que lo que esperariamos es que el tiempo de ejecución de la función
    #asincrona sea menor al de la función sincrona , esto podemos comprobar al correr el código ya que la función asincrona esta 
    #haciendo uso de la concurrencia, el speed up nos representa que tan más rapido es la función asincrona respecto a la asincrona



    #Parte d
    #Speed up de las primeras dos URLS
    #Calculamos el tiempo de ejecución de la función asincrona para las dos primeras URLS
    i3 = time.perf_counter()
    html_cont_1 =asyncio.run(async_scraper(urls[0:2]))
    f3 = time.perf_counter()
    tex3=f3-i3
    
    #Calculamos el tiempo de ejecución de la función sincrona para las dos primeras URLS
    i4 = time.perf_counter()
    html_cont = sync_scraper(urls[0:2])
    f4 = time.perf_counter()
    tex4=f4-i4

    #Calculamos el speedup de nuestra función
    speedup_1=tex4/tex3
    print(f"El speed up para las dos primeras URL's es el siguiente: {speedup_1:0.3f}")

    
    #Speed up de las ultimas dos URLS
    #Calculamos el tiempo de ejecución de la función asincrona para las dos ultimas URLS
    i5 = time.perf_counter()
    html_cont_3 =asyncio.run(async_scraper(urls[6:8]))
    f5 = time.perf_counter()
    tex5=f5-i5
    
    #Calculamos el tiempo de ejecución de la función sincrona para las dos ultimas URLS
    i6 = time.perf_counter()
    html_cont_4= sync_scraper(urls[6:8])
    f6 = time.perf_counter()
    tex6=f6-i6

    #Calculamos el speedup de nuestra función
    speedup_2=tex6/tex5
    print(f"El speed up para las dos ultimas URL's es el siguiente: {speedup_2:0.3f}")

    #Para el caso de la pregunta d, el mayor speed up es para el caso en donde tenemos todas las URL's esto se debe 
    #a que agarramos el contenido de todas las URL's , es decir que mientras menos contenido tenga la URL de la pagina
    #como en el caso de las dos ultimas URL's podemos notar que el tiempo que demora la función asincrona se
    # va volviendo bastante parecido al de la sincrona, esto guarda sentido ya que para aquellas tareas que sean 
    #más pesadas es donde saca probecha la concurrencia frente a la secuancialidad
