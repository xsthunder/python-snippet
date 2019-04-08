# abc123 d
# priority_queue, search in 3d cube
def read_numbers():
    a = read().split(' ')
    a = list(map(int, a))
    return a
[x,y,z,K] = read_numbers()
memo = [[set() for i in range(y)]for i in range(x)]
X = read_numbers()
Y = read_numbers()
Z = read_numbers()
X.sort()
X.reverse()
Y.sort()
Y.reverse()
Z.sort()
Z.reverse()
import queue
def cal(px, py,pz):
    return X[px]+Y[py]+Z[pz]
memo[0][0].add(0)
cnt = 0
pq = queue.PriorityQueue()
# print(X,Y,Z)
pq.put((-cal(0,0,0) ,0,0,0))
while(cnt < K):
#     print(cnt)
    cost , px, py, pz = pq.get(timeout=1)
#     print(cost, px, py,pz)
    for i in range(px-1, px + 2):
        for j in range(py-1, py + 2):
            for k in range(pz-1, pz + 2):
                if (i >= 0 and i < x and 
                    j >= 0 and j < y and 
                    k >=0 and k < z and
                    k not in memo[i][j]
                   ):
                    memo[i][j].add(k)
                    pq.put((-cal(i,j,k),i,j,k))
    print(-cost)
    cnt = cnt + 1
