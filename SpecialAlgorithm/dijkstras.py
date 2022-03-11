def dijkstrasAlgorithm(start, edges):
    edge_len = len(edges)

    smallest_distance_arr = [float("inf") for _ in range(edge_len)]
    smallest_distance_arr[start] = 0
    visited_arr = set()
    while len(visited_arr) < edge_len:
        vertex, smallest_distance = getVertex(smallest_distance_arr, visited_arr)

        if smallest_distance == float("inf"):
            smallest_distance_arr[vertex] = -1
            visited_arr.add(vertex)
            continue

        visited_arr.add(vertex)
        for destination, destination_distance in edges[vertex]:
            if destination in visited_arr:
                continue
            current_distance = smallest_distance_arr[destination]
            smallest_distance_arr[destination] = min(current_distance, destination_distance + smallest_distance)
    return smallest_distance_arr

def getVertex(distance, visited):
    smallest_distance = float("inf")
    vertex = 0
    for v, dist in enumerate(distance):
        if v not in visited and dist <= smallest_distance:
            smallest_distance = dist
            vertex = v
    return vertex, smallest_distance


edges = [
         [
             [1, 7]
         ],
         [
             [2, 6],
             [3, 20],
             [4, 3]
         ],
         [
             [3, 14]
         ],
         [
             [4, 2]
         ],
         [],
         []]

print(dijkstrasAlgorithm(1, edges))