
G = {
    "Biratnagar": {"Itahari": 22, "Biratchowk": 30, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Rangeli": {"Kanepokhari": 25, "Biratnagar": 25, "Urlabari": 40},
    "Biratchowk": {"Itahari": 11, "Biratnagar": 30, "Kanepokhari": 10},
    "Dharan": {"Itahari": 20},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Rangeli": 40, "Kanepokhari": 12, "Damak": 6},
    "Damak": {"Urlabari": 6},
}

H = {
    "Biratnagar": 46, "Itahari": 39, "Dharan": 41, "Rangeli": 28, 
    "Biratchowk": 29, "Kanepokhari": 17, "Urlabari": 6, "Damak": 0,
}

def Astar(start, goal, graph, heuristic):
    open_set = {start}
    prev = {start: None}
    g_cost = {start: 0}
    visited = set()

    while open_set:
        current_state = min(open_set, key=lambda node: g_cost[node] + heuristic[node])
        open_set.remove(current_state)

        if current_state == goal:
            return True, prev, g_cost[goal]  
        visited.add(current_state)

        for neighbor, cost in graph[current_state].items():
            if neighbor in visited:
                continue
            new_g = g_cost[current_state] + cost 

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                prev[neighbor] = current_state
                open_set.add(neighbor)
                
    return False, {}, float('inf')

def constructPath(goal, prev):
    
    path = []
    
    while goal is not None:
        path.append(goal)
        goal = prev[goal]
    return " -> ".join(reversed(path))


start = input("Enter the start location: ").strip()
goal = input("Enter the goal location: ").strip()

sol, path, cost = Astar(start, goal, G, H)

if sol:
    print("Path found:", constructPath(goal, path))
    print(f"Minimum cost: {cost}")
else:
    print(f"No path found between {start} and {goal}")