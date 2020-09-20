def euclidean_dist(x, y):
    if (x == [] or y == []):
        raise ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        raise ValueError("lengths must be equal")

    return sum([abs(x[i] - y[i])**2 for i in range(len(x))])**(1/2)

def manhattan_dist(x, y):
    if (x == [] or y == []):
        raise ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        raise ValueError("lengths must be equal")
    
    return sum([abs(x[i] - y[i]) for i in range(len(x))])

def jaccard_dist(x, y):
    if (x == [] or y == []):
        raise ValueError("lengths must not be zero")

    return 1 - len(set(x) & set(y)) / len(set(x) | set(y))

def cosine_sim(x, y):
    if (x == [] or y == []):
        raise ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        raise ValueError("lengths must be equal")

    sumx = 0
    sumy = 0
    sumxy = 0
    for i in range(len(x)):
        x_i = x[i]
        y_i = y[i]
        sumx += x_i**2
        sumy += y_i**2
        sumxy += x_i*y_i
    
    return sumxy/(sumx*sumy)**(1/2)
