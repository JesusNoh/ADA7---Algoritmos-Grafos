def warshall(graph):
    # Número de vértices en el grafo
    num_vertices = len(graph)

    # Creamos una matriz de alcance inicializando con los valores del grafo
    reach = [[False] * num_vertices for _ in range(num_vertices)]

    # Llenamos la matriz de alcance con las conexiones directas
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:  # Hay una arista entre i y j
                reach[i][j] = True
            if i == j:  # Cada vértice puede alcanzar a sí mismo
                reach[i][j] = True

    # Aplicamos el algoritmo de Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if not reach[i][j]:
                    reach[i][j] = reach[i][k] and reach[k][j]

    return reach

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un nuevo grafo como una matriz de adyacencia
    graph = [
        [0, 1, 0, 0, 1],  # Vértice 0 conectado a 1 y 4
        [0, 0, 1, 0, 0],  # Vértice 1 conectado a 2
        [0, 0, 0, 1, 0],  # Vértice 2 conectado a 3
        [0, 1, 0, 0, 0],  # Vértice 3 conectado a 1
        [1, 0, 0, 0, 0]   # Vértice 4 conectado a 0
    ]

    # Llamamos a la función y mostramos el resultado
    transitive_closure = warshall(graph)

    print("Matriz de cierre transitivo:")
    for row in transitive_closure:
        print(row)