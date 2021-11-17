def neighbours(w, bs):
    """neighbours from a white (w) vertex to black vertices (bs)"""
    return [b for b in bs if b == w]


def degree(w, bs):
    """number of edges from a white vertex (w) to black vertices (bs)"""
    return sum(1 for _ in neighbours(w, bs))


def vert_of_degree(d, ws, bs):
    """white vertices (ws) of a specified degree with edges to blacks (bs)"""
    return [w for w in ws if degree(w, bs) == d]


def subgraphs_of_size_two(ws, bs):
    """finds clusters of size 2, i.e. one-to-one mappings"""
    # two pass of filtering to degree 1
    for _ in range(2):
        ws, bs = vert_of_degree(1, ws, bs), vert_of_degree(1, bs, ws)

    for w in ws:
        b = neighbours(w, bs)[0]
        yield w, b
