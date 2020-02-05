import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
start, finish = map(int, input().split())
start -= 1
finish -= 1
if start == finish:
    print(0)
else:
    visited = set()
    visited.add(start)
    queue = []
    queue.append((start, [start]))
    flag = 0
    while queue:
        tmp, way = queue.pop()
        if tmp == finish:
            flag = 1
            print(len(way) - 1)
            break
        for i in range(n):
            if graph[tmp][i] == 1 and i not in visited:
                visited.add(i)
                queue.insert(0, (i, way + [i]))
    if flag == 0:
        print(-1)