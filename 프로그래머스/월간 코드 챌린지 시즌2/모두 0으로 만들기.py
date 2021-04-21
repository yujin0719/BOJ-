# 모두 0으로 만들기
import sys
sys.setrecursionlimit(300000)
from collections import defaultdict
answer = 0

def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def dfs(u, v):
        global answer
        for node in graph[u]:
            if node != v:
                dfs(node,u)
        answer += abs(a[u])
        a[v] += a[u]
        a[u] = 0
    dfs(0,0)   
    return answer