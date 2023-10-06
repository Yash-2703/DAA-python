'''
---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement: Implement a problem of activity selection problem with K persons.
                    -Given two arrays S[] and E[] of size N denoting starting and closing time of the shops and an integer value K denoting the
                     number of people, the task is to find out the maximum number of shops they can visit in total if they visit each shop optimally based
                     on the following conditions:
                     1) A shop can be visited by only one person
                     2) A person cannot visit another shop if its timing collide with it.
---------------------------------------------------------------------------------------------------------------------------------------------'''
def max_shops_to_visit(shops, k):
    n = len(shops)

    shops.sort(key=lambda x: x[1])

    visited = 1  # First shop is always visited
    prev_shop = 0  # Index of the last visited shop

    for i in range(1, n):
        if shops[i][0] > shops[prev_shop][1]:
            visited += 1
            prev_shop = i
        if visited == k:
            break  # All persons have visited a shop

    return visited

# Example usage:
N = 5  # Number of shops
K = 3  # Number of people
shops = [(1, 3), (2, 5), (3, 7), (5, 8), (6, 9)]

max_shops = max_shops_to_visit(shops, K)
print("Maximum number of shops that can be visited:", max_shops)
