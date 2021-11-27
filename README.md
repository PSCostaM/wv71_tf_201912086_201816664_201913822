# WV71_tf_201912086_201816664_201913822
Repositorio creado con el fin de desarrollar el Trabajo Parcial y Final del curso Complejidad Algoritmica.

# Integrantes

| * | Integrantes |
| ------ | ------ |
| 1 | Diego Enrique Osorio Horna |
| 2 | Piero Martin Palomino Calderon |
| 3 | Paulo Sergio Costa Mondragón |

# Planteamiento de Vehicle Routing Problem(VRP)

 Es un problema de optimización que tiene como objetivo minimizar los costos de transporte asociados a rutas de reparto, Se presentan muchas restricciones para desarrollar este algoritmo los cuales son:
- Cada vehículo tiene una capacidad limitada.
- Cada cliente tiene que ser visitado dentro de una determinada franja horaria
- Varios puntos de suministro
- Los clientes pueden ser atendidos por varios vehículos
- Algunas variables del problema son aleatorias, como el número de clientes, sus demandas, etc.
- Las entregas se deben realizar en determinado tiempo definido

# Reporte de Actividades 

| * | Actividades | Desarrollado por |
| ------ | ------ | ------ |
| 1 | Crear el dataset con puntos de entrega y almacenes | Piero - Diego |
| 2 | Definir los espacios de búsqueda y graficarlo | Paulo - Diego |
| 3 | Definir el costo de vehículos | Paulo - Piero|
| 4 | Realizar un Algoritmo por integrante | Paulo - Piero - Diego |
| 5 | Grabar video | Piero |
| 6 | Presentacion del Trabajo Parcial | Paulo - Piero - Diego |

# Algortimo por Estudiante

| Algoritmo | Integrante |
| ------ | ------ |
| Djkistra | Paulo Sergio Costa Mondragón |
| Brute Force | Piero Martin Palomino Calderon |
| Naive | Diego Enrique Osorio Horna |

# Video del primer reporte
https://youtu.be/ISeBbDpy1xs

# Resolviendo VRP con 3 distintos algoritmos
| * | Integrantes | Algoritmos usados |
| ------ | ------ | ------ |
| 1 | Diego Enrique Osorio Horna | Naive Algorithm/Prim - Dijkstra |
| 2 | Piero Martin Palomino Calderon | Prim | 
| 3 | Paulo Sergio Costa Mondragón | BellmanFord modified |

# Conceptos a considerar

Para empezar a solucionar el VRP problem con cualquier algoritmo, debemos tratar de agrupar los almacenes con los puntos de delivery más cercanos para saber que puntos de delivery visitar después de recoger paquetes.
```
get_dist = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])
def group_delivery_whouses(warehouse_points, delivery_points):

  groups = []
  for i in range(len(warehouse_points)):
    groups.append([])

  for j in range(len(delivery_points)):
    d = delivery_points[j]
    mn = math.inf
    idmn = 0
    for i in range(len(warehouse_points)):
      w = warehouse_points[i]
      dis = get_dist(d,w)#get Distance from delivery_pts & whouse
      if(dis < mn):
        mn = dis
        idmn = i

    groups[idmn].append(d)

  return groups
```
Para eso utilizamos la función group_delivery_whouses(). De manera que los almacenes y punto de entrega terminan viéndose así.
```import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['figure.figsize'] = (10,10)

def plot_points():
    plt.scatter(x=[w[0] for w in wh], y=[w[1] for w in wh], color='r', s=60)
    plt.scatter(x=[d[0] for d in dp], y=[d[1] for d in dp], color='g', s=15)
plot_line = lambda s, d: plt.plot([s[0], d[0]], [s[1], d[1]],'b-.', linewidth=1)
distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

wh = pd.read_csv('../DataSet/Almacenes.csv').values.tolist()
dp = pd.read_csv('../DataSet/PuntosEntrega.csv').values.tolist()

pdp = 0.2
pdw = 0.5
dps = int(len(dp)*pdp)
whs = int(len(wh)*pdw)
dp = dp[:dps]
wh = wh[:whs]
plot_points()
for d in dp:
    c = min(wh, key=lambda x: distance(x, d))
    plot_line(c, d)
```
