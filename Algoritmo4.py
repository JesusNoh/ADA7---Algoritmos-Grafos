class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(vertices)
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            mst_weight += weight

    return mst_edges, mst_weight

if __name__ == "__main__":
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    vertices = 4

    mst_edges, mst_weight = kruskal(vertices, edges)

    print("Aristas del Árbol de Expansión Mínima:")
    for u, v, weight in mst_edges:
        print(f"({u}, {v}) - Peso: {weight}")
    
    print(f"Peso total del MST: {mst_weight}")