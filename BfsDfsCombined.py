def main():
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    BfsDfsCombine(g, 1, 1)
    print()
    BfsDfsCombine(g, 1, 0)


def BfsDfsCombine(g, s, bfs=True):
    vis = set()
    ds = [s]

    while ds:
        u = ds.pop(0) if bfs else ds.pop()

        if u in vis:
            continue

        vis.add(u)
        print(u, end=" ")

        for v in g[u]:
            if v not in vis:
                ds.append(v)

main()