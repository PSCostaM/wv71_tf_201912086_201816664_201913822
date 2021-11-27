import pandas as pd
import math

whouse_pts = "https://raw.githubusercontent.com/PSCostaM/wv71_tf_201912086_201816664_201913822/main/DataSet/Almacenes.csv"
delivery_pts_csv = "https://raw.githubusercontent.com/PSCostaM/wv71_tf_201912086_201816664_201913822/main/DataSet/PuntosEntrega.csv"
whouses_file = pd.read_csv(whouse_pts).to_numpy()
delivery_points_file = pd.read_csv(delivery_pts_csv).to_numpy()


warehouse_points=[]
for line in whouses_file:
  warehouse_points.append((int(line[0]),int(line[1])))

delivery_points=[]
for line in delivery_points_file:
  delivery_points.append((int(line[0]),int(line[1])))

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
groups = group_delivery_whouses(warehouse_points, delivery_points)

def BellmanFord_modified(group, origin):
  group.insert(0,origin)  
  n = len(group)
  cost = [float('inf')]*n
  cost[0]=0
  previous = [-1]*n

  listadj = [[]for _ in range(n)]  
  for i in range(n):
    for j in range(n):
      if i!=j:
          if get_dist(group[j],group[i]) < 50: 
            listadj[i].append((j, get_dist(group[j], group[i]))) # agregamos el destino y su costo
      
  for _ in range(n-1):
    for u in range(n):
      for v, w in listadj[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          previous[v] = u

  for u in range(n):
    for v, w in listadj[u]:
      if cost[u] + w < cost[v]:
        return None, None

  return previous, cost
final_groups = group_delivery_whouses(warehouse_points, delivery_points)
for i in range(0,25):
  print(BellmanFord_modified(final_groups[i], warehouse_points[i]))
