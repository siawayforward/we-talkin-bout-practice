# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/
from itertools import combinations
from math import prod

# input
def kittys_calculation(edges, queries):
    result = 0
    # get the pairs that can be made from the query
    pairs = [list(p) for p in list(combinations(queries, 2))]
    
    # check distance between each of the queries for each edge pair
    # how many array do you have to get through to find both numbers after you find the first one?
    for p in pairs:
        start = [edges.index(e) for e in edges if p[0] in e][0]
        ct = 0 #start tracking how far we have to go to find the second edge in the pair
        for e in edges[start:]:
            while p[1] not in e:
                ct += 1
                break
            # append distance to the end of the pair
        p.append(ct)
        # with distances, find the product of the pair and distance and sum them
        result += prod(p)
    return result

# with this case, we should get a sum of 214
edges = [[1,2], [1,3], [1,4], [3,5], [3,6], [3,7]]
queries = [4,5,7]    
    
    
if __name__ == "__main__":
    res = kittys_calculation(edges, queries) 
    print('summation is:', res)