from collections import deque

n, q = int(input()), deque()
x1, y1 = map(int, input().split())
x1, y1 = x1-1, y1-1
x2, y2 = map(int, input().split())
x2, y2 = x2-1, y2-1
x = [-2, -2, -1, -1, 1, 1, 2, 2]
y = [-1, 1, -2, 2, -2, 2, -1, 1]
stol = [0]*n
for i in range(n):
    stol[i] = [1000000000]*n
stol[x1][y1] = 0
q.appendleft([x1, y1])
while q:
    front = q.popleft()
    i = front[0]
    j = front[1]
    for l in range(8):
        k = (i + x[l])
        t = (j + y[l])
        if (k >= 0 and k < n):
                if t >= 0 and t < n:
                    if stol[k][t] > stol[i][j] + 1:
                        stol[k][t] = stol[i][j] + 1
                        q.appendleft([k, t])
print(stol[x2][y2])