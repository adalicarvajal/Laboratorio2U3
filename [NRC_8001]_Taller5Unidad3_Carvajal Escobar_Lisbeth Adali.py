# devuelve el costo mínimo en un vector (si
# hay varios estados de objetivos)
def uniform_cost_search(goal, start):
    '''
    Funcion:Esta función puede ser utilizada 
    para encontrar la ruta más corta desde un nodo de inicio hasta uno o más nodos objetivo en un grafo. 
    La función implementa una búsqueda de costo uniforme utilizando una cola ordenada y un diccionario "visited"
    para evitar ciclos y reducir el tamaño de la cola.

    Parametros: (goal, strart)

    Retorna: answer 

    '''
    #La primera línea declara las variables globales "graph" y "cost".
    global graph, cost
    #inicializa la lista "answer" con valores infinitos para cada nodo objetivo.
    answer = []
    # inicializa una cola de búsqueda vacía y agrega el nodo de inicio y su costo actual.
    for i in range(len(goal)):
        answer.append(10**8)
    queue = []
    queue.append([0, [start]])
    #inicializa un diccionario "visited" para llevar un registro de los nodos que han sido visitados.
    visited = {}
    #inicializa un contador para contar el número de objetivos encontrados.
    count = 0
    #El bucle "while" itera hasta que la cola de búsqueda esté vacía.
    while (len(queue) > 0):
        #ordena la cola por costo y extrae el nodo con el costo más alto.
        queue = sorted(queue)
        #multiplica el costo por -1 para que la cola siga siendo ordenada en orden ascendente.
        p = queue[-1]
        #extrae la ruta actual desde el nodo extraído.
        del queue[-1]
        #extrae la ruta actual desde el nodo extraído.
        p[0] *= -1
        path = p[1][:]
        #comprueba si el nodo actual es un objetivo y actualiza la respuesta con el costo más bajo encontrado hasta el momento si es necesario.
        if (path[-1] in goal):
            index = goal.index(path[-1])
            # comprueba si el nodo actual ya ha sido visitado. 
            if (answer[index] == 10**8):
                count += 1
            #Si no lo ha sido, agrega todos sus vecinos a la cola de búsqueda con su costo actualizado.
            if (answer[index] > p[0]):
                answer[index] = p[0]
                path = p[1][:]
               #marca el nodo actual como visitado. 
            if (count == len(goal)):
                return answer, path
        # devuelve la lista de respuestas y la ruta más corta encontrada, o una lista vacía si no se encontraron soluciones.        
        if (path[-1] not in visited):
            for i in range(len(graph[path[-1]])):
                new_path = path[:]
                new_path.append(graph[path[-1]][i])
                queue.append([(p[0] + cost[(path[-1], graph[path[-1]][i])]) * -1, new_path])
        visited[path[-1]] = 1
        #finaliza la función.
    return answer, []

if __name__ == '__main__':
    #establece dos variables globales "graph" y "cost". La variable "graph" es una lista de listas que representa un grafo con 8 nodos. La variable "cost" es un diccionario que almacena los costos de las aristas entre los nodos.
    graph, cost = [[] for i in range(8)], {}
    #agregar información sobre los nodos y las aristas en "graph" y "cost".
    graph[0].append(1)
    #agregar información sobre los nodos y las aristas en "graph" y "cost".
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)


    # establece una lista de objetivos con un solo elemento, el nodo 6.
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7
    #llama a la función "uniform_cost_search" con el nodo objetivo "goal" y el nodo de inicio "0".
    goal = [6]
    #imprime el costo mínimo para el camino desde el nodo 0 hasta el nodo 6, que se almacena en "answer[0]".
    answer, path = uniform_cost_search(goal, 0)
    #imprime un mensaje para indicar que el camino con 3 pasos seguirá.
    print("El costo mínimo de 0 a 6 es =", answer[0])
    print("Camino con 3 pasos:")
