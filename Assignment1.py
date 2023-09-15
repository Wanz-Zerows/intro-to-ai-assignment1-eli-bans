class Graph:
    def __init__(self, graph_dict, heuristic):
        self.graph = graph_dict
        self.heuristic = heuristic

    def dfs(self, start, goal, path=None):
        if path is None:
            path = []
        path.append(start)
        if start == goal:
            print(f"DFS path: {path}")
            return path
        for neighbor in self.graph[start]:
            if neighbor not in path:
                self.dfs(neighbor, goal, path.copy())

    def all_paths(self, start, goal, path=None):
        if path is None:
            path = []
        path.append(start)
        if start == goal:
            print(f"Possible path: {path}")
            return
        for neighbor in self.graph[start]:
            if neighbor not in path:
                self.all_paths(neighbor, goal, path.copy())

    def greedy_best_first_search(self, start, goal):
        open_list = [(start, [start])]  #priority queue
        while open_list:
            current, path = min(open_list, key=lambda x: self.heuristic[x[0]])
            open_list.remove((current, path))
            if current == goal:
                print(f"Greedy best first path: {path}")
                return path
            for neighbor in self.graph[current]:
                if neighbor not in path:
                    open_list.append((neighbor, path + [neighbor]))

    # returns optimal path from start to goal
    def a_star(self, start, goal):
        open_list = [(start, [start], 0)] # priority queue
        while open_list:
            current, path, g = min(open_list, key=lambda x: x[2] + self.heuristic[x[0]])
            open_list.remove((current, path, g))
            if current == goal:
                print(f"A* path: {path}")
                return path
            for neighbor, cost in self.graph[current].items():
                if neighbor not in path:
                    open_list.append((neighbor, path + [neighbor], g + cost))


# given graph and heuristic
graph_dict = {
    'A': {'B': 1, 'C': 4, 'E': 3},
    'B': {'A': 1, 'D': 5, 'E': 2},
    'C': {'A': 4, 'F': 2},
    'D': {'B': 5, 'G': 5},
    'E': {'A': 3, 'B': 2, 'F': 6},
    'F': {'C': 2, 'E': 6, 'G': 4},
    'G': {'D': 5, 'F': 4}
}

heuristic = {
    'A': 0,
    'B': float("inf"),  #assigning unknown cost to infinity
    'C': 1,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 0
}

# Initialize graph object
g = Graph(graph_dict, heuristic)

# Example usage
g.dfs('A', 'G')
g.all_paths('A', 'G')
g.greedy_best_first_search('A', 'G')
g.a_star('A', 'G')