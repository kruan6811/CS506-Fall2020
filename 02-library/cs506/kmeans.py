from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    if (points == []):
        raise ValueError("must contain at least one point")

    center = points[0].copy()
    for i in range(1,len(points)):
        next_point = points[i]

        for j in range(0, len(center)):
            center[j] += next_point[j]    

    center = [x/len(points) for x in center]
    return center

def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    clusters = {}

    for i in range(0,len(dataset)):
        if assignments[i] in clusters:
            clusters[assignments[i]].append(dataset[i])
        else:
            clusters[assignments[i]] = [dataset[i]]
    
    centers = []
    for key in clusters:
        centers += [point_avg(clusters[key])]

    return centers        

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    if (a == [] or b == []):
        raise ValueError("lengths of a and b must not be zero")
    
    return (sum([(x - y) ** 2 for x, y in zip(a, b)])) ** (0.5)

def distance_squared(a, b):
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k=k)

def cost_function(clustering):
    cost = 0

    for key in clustering:
        cluster = clustering[key]
        center = point_avg(cluster)

        for point in cluster:
            cost += distance_squared(point, center)
    
    return cost

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = generate_k(dataset, 1)

    while(k != 0):
        distances = []

        for point in dataset:
            distances += [min([distance_squared(point, center) for center in centers])]

        probs = [x/sum(distances) for x in distances]
        centers += random.choices(dataset, weights=probs, k=1)
        k-=1

    return centers[1:]

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
