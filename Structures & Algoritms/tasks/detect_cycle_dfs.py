def detect_cycle_dfs(graph, node, visited, rec_stack):
    # Mark the current node as visited and a part of recursion stack
    visited[node] = True
    rec_stack[node] = True

    # Recur for all neighbors of the node
    for neighbor in graph[node]:
        if visited[neighbor] == False:
            # If the neighbor node is not visited, perform DFS on it
            if detect_cycle_dfs(graph, neighbor, visited, rec_stack):
                # If there is a cycle in the DFS, return True
                return True
        elif rec_stack[neighbor] == True:
            # If the neighbor node is already in the recursion stack, return True
            # indicating there is a cycle in the graph
            return True

    # Mark the node as not part of the recursion stack
    rec_stack[node] = False
    return False


def is_cyclic(graph):
    # Initialize the visited and recursion stack dictionaries
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    # Perform DFS for every node in the graph
    for node in graph:
        if visited[node] == False:
            # If a cycle is found, return True
            if detect_cycle_dfs(graph, node, visited, rec_stack) == True:
                return True
    # If no cycle is found, return False
    return False


# Example usage:

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3],
}

print(is_cyclic(graph))  # Output: True
