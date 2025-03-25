from collections import deque

G = {
    "Biratnagar": {"Itahari": 22, "Biratchowk": 30, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Rangeli": {"Kanepokhari": 25, "Biratnagar": 25},
    "Biratchowk": {"Itahari": 11, "Biratnagar": 30, "Kanepokhari": 10},
    "Dharan": {"Itahari": 20},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Rangeli": 40, "Kanepokhari": 12, "Damak": 6},
    "Damak": {"Urlabari": 6},
}

def BFS(start, goal, graph):
    queue = deque([start])  
    visited = set()
    prev = {start: None} 

    while queue:
        current = queue.popleft()  

        if current == goal:
            return True, prev 

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    prev.setdefault(neighbor, current)

    return False, {}

def constructPath(goal, prev):
    path = []
    while goal is not None:
        path.append(goal)
        goal = prev[goal]
    return " -> ".join(reversed(path))


start = input("Enter the start location: ").strip()
goal = input("Enter the goal location: ").strip()

sol, path = BFS(start, goal, G)

if sol:
    print("Path found:", constructPath(goal, path))
else:
    print(f"No path found between {start} and {goal}")