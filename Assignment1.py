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
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 3},
    'C': {'E': 5},
    'D': {'F': 2, 'G': 4},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 5,
    'B': 4,  #assigning unknown cost to infinity
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

# initialize graph object
g = Graph(graph_dict, heuristic)

# allow user input for dfs start note
dfs_start = input("Please enter a start node for the dfs traversal.\n"
                  "You may choose between A and G ")
g.dfs(dfs_start.upper(),'F')

# method usage
g.all_paths('A', 'G')
g.greedy_best_first_search('A', 'G')
g.a_star('A', 'G')
