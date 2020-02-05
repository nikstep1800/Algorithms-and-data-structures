import sys
sys.setrecursionlimit(1000000)


def dfs(num, used, comp, matr):
    used[num] = True
    comp.append(num)
    for i in range(len(matr[num])):
        next = matr[num][i]
        if not used[next]:
            dfs(next, used, comp, matr)


def find_comps(n, matr):
    k = 0
    comp = []
    for i in range(n):
        if not used[i]:
            if len(comp) > 0:
                comp = []
            dfs(i, used, comp, matr)
            k += 1
            ANS.append([len(comp)])
            ANS.append([j+1 for j in sorted(comp)])
    print(k)
    [print(*i, sep=' ') for i in ANS]

n, m = map(int, input().split())
matr = [[]*n for i in range(n)]
used = [False]*n
ANS = []
for i in range(m):
    k, t = map(int, input().split())
    matr[k-1].append(t-1)
    matr[t-1].append(k-1)
matr = [sorted(list(set(i))) for i in matr]
find_comps(n, matr)