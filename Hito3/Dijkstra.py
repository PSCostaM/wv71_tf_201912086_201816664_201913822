import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import time
import math

whouse_pts = "https://raw.githubusercontent.com/PSCostaM/wv71_tf_201912086_201816664_201913822/main/DataSet/Almacenes.csv"
delivery_pts_csv = "https://raw.githubusercontent.com/PSCostaM/wv71_tf_201912086_201816664_201913822/main/DataSet/PuntosEntrega.csv"
whouses_file = pd.read_csv(whouse_pts).to_numpy()
delivery_points_file = pd.read_csv(delivery_pts_csv).to_numpy()

size_of_side=1000

warehouse_points=[]
for line in whouses_file:
  m=size_of_side*(int(line[0]))+int(line[1])
  warehouse_points.append(m)

delivery_points=[]
for line in delivery_points_file:
  m=size_of_side*(int(line[0]))+int(line[1])
  delivery_points.append(m)
  

def Mark_Visited(visited):
  for w_point in warehouse_points:
    visited[w_point] = True

def dijkstra(G, size_of_side, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  Mark_Visited(visited)
  visited[s]=False
  while queue:
    if all(visited[p] for p in delivery_points): break
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v] and not visited[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost

def Get_Path_by_delivery_point(lis,node):
  l=[]
  def _get_Path(node):
    if node==None: return
    else:
      l.append(node)
      _get_Path(lis[node])
  
  _get_Path(node)
  l.reverse()
  return l
def gen_city(n):
  def NodeAdj(dir,i,j):
      if dir=='U':
        return n*(i-1)+j
      elif dir =='D':
        return n*(i+1)+(j)
      elif dir=='L':
        return n*(i)+(j-1)
      elif dir =='R':
        return n*(i)+(j+1)

  G=[]
  for i in range(n):
    for j in range(n):
      l=[]
      if i==0 or i==n-1 or j==n-1 or j==0:
        if i==0:
          if j==0:
            l.append(NodeAdj('R',i,j))
            l.append(NodeAdj('D',i,j))
          elif j==n-1:
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('D',i,j))
          else:
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('R',i,j))
            l.append(NodeAdj('D',i,j))
        elif i==n-1:
          if j==0:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('R',i,j))
          elif j==n-1:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('L',i,j))
          else:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('R',i,j))
        elif j==0:
          l.append(NodeAdj('U',i,j))
          l.append(NodeAdj('R',i,j))
          l.append(NodeAdj('D',i,j))
        elif j==n-1:
          l.append(NodeAdj('U',i,j))
          l.append(NodeAdj('L',i,j))
          l.append(NodeAdj('D',i,j))
      else:
        l.append(NodeAdj('U',i,j))
        l.append(NodeAdj('L',i,j))
        l.append(NodeAdj('R',i,j))
        l.append(NodeAdj('D',i,j))
      m=[]
      for node in l:
        m.append(tuple([node,1]))
      G.append(m)
  return G

G=gen_city(size_of_side)
for i in warehouse_points:
  inicio=time.time()
  path, cost = dijkstra(G,size_of_side, i)
  fin=time.time()
  print(f"For n: {i} - {round((fin-inicio),5)} s")
  print(cost[811965]) #delivery Cost
  print(cost[8687]) #Whouse_cost
  print(cost[0]) #inf->Already visited node


print("done")
