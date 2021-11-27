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
def bellmanFord(G, s):
  n = len(G)

  #initialize
  cost = [float('inf')]*n
  cost[s]=0
  path = [-1]*n

  #relax
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u]+w
          path[v]=u
  
  #check negative cygroupse
  for u in range(n):
    for v, w in G[u]:
      if cost[u]+w<cost[v]:
        return None, None

  return path, cost
