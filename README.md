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
![Uploading image.png…]()
Para eso utilizamos la función group_delivery_whouses()

