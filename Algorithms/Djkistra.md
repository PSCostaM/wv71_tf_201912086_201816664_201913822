# Algoritmo Djkistra
 
 | Topic | Desc |
 | ------ | ------ |
 | Autor | Paulo Sergio Costa Mondragón | 
 | Técnica | Djkistra | 
 
 
 Debido a que tanto DFS y BFS no trabajan con wighted graphs el algoritmo a trabajar fue el Djkistra.
 El peso en los edges será denotado por la distancia que hay entre el camión, el punto de entrega y el almacén; estos vendrían a ser los nodos.

Este algoritmo trabaja desde un source node y encuentra el mínimo camino para llegar recorrerlos, teniendo dos sets, nodos ya agregados y los que no se encuentran en este set.

![image](https://user-images.githubusercontent.com/48858434/135736150-0b9d079c-f4bd-493d-835d-2c7e3f736a71.png)
 
El nodo source empieza con 0 y las demás distancias se da cómo INF.
Djkistra agrega al siguiente nodo 1 debido a la distancia minima entre los dos puntos de salida.
Al momento de estar en 1, tenemos dos salidas, a 2 la cuál nos daría distancia total de 12 o regresar a 7 por el source node que nos daría distancia solo de 8; se agrega al set {0, 1, 7}.

En el caso de VRP, el source node empezaría en el camión ya habiendo visitado el almacén más cercano y guardardando la distancia recorrida hasta ese almacén, luego ir recorriendo desde el almacén a los siguientes nodos que son los puntos de entrega. 

```python
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print "Vertex \tDistance from Source"
        for node in range(self.V):
            print node, "\t", dist[node]
 
    def minDistance(self, dist, sptSet):
        min = sys.maxint
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index

    def dijkstra(self, src):
 
        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
 
            sptSet[x] = True
            
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.dijkstra(0);
```
Código simplificado para visualizar el funcionamiento de Djkistra.

## Análisis de Complejidad

Djkistra viene a ser O(V * 2) pero usando una min-priority queue baja a ser O(V + E log V) dónde V son los nodos y E las aristas.
