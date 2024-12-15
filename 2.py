from collections import deque, defaultdict

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.capacity = defaultdict(int)

    def add_edge(self, u, v, cap):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.capacity[(u, v)] += cap

    def bfs(self, s, t, level):
        queue = deque([s])
        level[s] = 0
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if level[v] == -1 and self.capacity[(u, v)] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] != -1

    def dfs(self, u, t, flow, level, ptr):
        if u == t:
            return flow
        while ptr[u] < len(self.adj[u]):
            v = self.adj[u][ptr[u]]
            if level[v] == level[u] + 1 and self.capacity[(u, v)] > 0:
                pushed = self.dfs(v, t, min(flow, self.capacity[(u, v)]), level, ptr)
                if pushed > 0:
                    self.capacity[(u, v)] -= pushed
                    self.capacity[(v, u)] += pushed
                    return pushed
            ptr[u] += 1
        return 0

    def max_flow(self, s, t):
        total_flow = 0
        while True:
            level = [-1] * self.n
            if not self.bfs(s, t, level):
                break
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), level, ptr)
                if pushed == 0:
                    break
                total_flow += pushed
        return total_flow

n = 6  # количество вершин
dinic = Dinic(n)

# Добавление рёбер
dinic.add_edge(0, 1, 10)
dinic.add_edge(0, 2, 10)
dinic.add_edge(1, 2, 2)
dinic.add_edge(1, 3, 4)
dinic.add_edge(1, 4, 8)
dinic.add_edge(2, 4, 9)
dinic.add_edge(3, 5, 10)
dinic.add_edge(4, 3, 6)
dinic.add_edge(4, 5, 10)
s, t = 0, 5  # исток и сток
print("Максимальный поток:", dinic.max_flow(s, t))