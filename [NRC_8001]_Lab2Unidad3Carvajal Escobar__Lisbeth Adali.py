def validarenteros():
    '''
    Funcion que valida el ingreso de numeros enteros
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        numero : int
    '''
    #ciclo repetitivo que valida si ha ingresado el numero entero
    while True:
        try:
            #ingreso un numero por teclado
            numero = int(input("Ingrese un número entero positivo: "))
            #si el numero es menor a 1 imprimira un mensaje diciendo que solo pide numeros positivos
            if numero < 0:
                raise ValueError("El número debe ser positivo")
            #caso contrario rompe el ciclo repetitivo
            break
        except ValueError as e:
            print(e)
    #retorna el numero validado
    return numero
def creacion_grafo():
    '''
    Funcion que crea y une a los nodos 
    Parametros:
        esta funcion no tiene parametros
    Retorna:
        grafo : list
    '''
    # Crear grafo
    grafo = [[] for i in range(35)]
    casa=0
    tambillo=1
    universidad=2
    marin=3
    desvio=4
    guajalo=5
    #uniendo nodos
    grafo[casa].append(tambillo)
    grafo[casa].append(marin)
    grafo[casa].append(guajalo)
    grafo[tambillo].append(universidad)
    grafo[tambillo].append(casa)
    grafo[universidad].append(tambillo)
    grafo[universidad].append(marin)
    grafo[universidad].append(desvio)
    grafo[marin].append(casa)
    grafo[marin].append(universidad)
    grafo[desvio].append(universidad)
    grafo[desvio].append(guajalo)
    grafo[guajalo].append(casa)
    grafo[guajalo].append(desvio)
    return grafo

def nombre_de_ubicacion(ruta_universidad):
    '''
    Funcion que da el nombre de los nodos
    Parametros:
        ruta_universidad : lista
    Retorna: 
        ruta_universidad : lista
    '''
    #recorremos la lista entera y damos el nombre de la ubicacion dependiendo el numero que tenga el nodo
    for i in camino:
        if(i==0):
            ruta_universidad.append("Casa")
        if(i==1):
            ruta_universidad.append("Tambillo")
        if(i==2):
           ruta_universidad.append("Universidad")
        if(i==3):
           ruta_universidad.append("Marin")
        if(i==4):
            ruta_universidad.append("Desvio")
        if(i==5):
            ruta_universidad.append("Guajalo")
        

    #retornamos el camino
    return ruta_universidad
def busqueda_ruta(grafo, costo, inicio, fin):
    '''
    Funcion que busca el camino mas corto en las ubicaciones de la espe
    Parametros:
        grafo : lista
        costo : diccionario
        inicio : int
        fin : int
    Retorna:
        float('inf') : float
        [] : lista
        
    '''
    #variable tipo cola que almacena tupplas con tres elementos: (1) la distancia del nodo 
    #de origen al nodo actual, (2) el nodo actual, y (3) el camino desde el nodo de origen hasta el nodo actual. 
    cola = [(0, inicio, [])]
    #variable que lleva el registro de los nodos que se han visitado durante la búsqueda.
    visitados = set()
    #recorremos la cola mientras no este vacia
    while cola:
        #Se toma el primer elemento de la cola (el nodo con la distancia mínima hasta ese momento)
        (dist, actual, camino) = cola.pop(0)
        #Si el nodo actual es el nodo de destino fin
        if actual == fin:
            #se devuelve la distancia total y el camino desde el nodo de origen hasta el nodo de destino.
            return dist, camino + [actual]
        #Si el nodo actual ha sido visitado previamente
        if actual in visitados:
            #se omite este nodo y se continúa con el siguiente.
            continue
        #Se agrega el nodo actual al conjunto de nodos visitados.
        visitados.add(actual)
        #Se recorre sobre los vecinos del nodo actual.
        for vecino in grafo[actual]:
            #Se obtiene el costo para llegar desde el nodo actual hasta su vecino, o se asigna un costo predeterminado 
            #de 1 si no se encuentra en el diccionario costo.
            costo_vecino = costo.get((actual, vecino), 1)
            #Se agrega una nueva tupla a la cola con la nueva distancia total, el vecino y el camino actualizado 
            # (agregando el nodo actual al camino).
            cola.append((dist + costo_vecino, vecino, camino + [actual]))
    #Si no se encuentra un camino desde el nodo de origen hasta el nodo de destino, se devuelve una distancia infinita y un camino vacío.
    return float('inf'), []
if __name__ == '__main__':
    ruta=[]
    grafo=creacion_grafo()
    costo={}
    print("En donde se encuentra usted?: \n0. Casa\n1. Tambillo\n2. Universidad\n3. La Marin\n4. Desvio\n5. Guajalo\nIngrese una opcion: ")
    punto_de_salida=validarenteros()
    print("En donde se encuentra usted?: \n0. Casa\n1. Tambillo\n2. Universidad\n3. La Marin\n4. Desvio\n5. Guajalo\nIngrese una opcion: ")
    punto_de_llegada=validarenteros()
    tambillo=1
    universidad=2
    marin=3
    desvio=4
    guajalo=5
    #buscamos la ruta mas corta con la ayuda de los nodos
    costo_1,camino=busqueda_ruta(grafo,costo,punto_de_salida,punto_de_llegada)
    #agrego los caminos a la lista
    ruta=nombre_de_ubicacion(ruta)
    print("El costo es: ",costo_1)
    print("El camino que debes tomar es:", ruta)