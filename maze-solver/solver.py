from cell import *


# depth-limited dfs
def dls_solver(maze, limit):
    current = maze.start
    stack = [current]
    path = []
    depth = 0
    while len(stack) > 0:
        cell = stack.pop()

        if cell == maze.goal:
            path.append(cell)
            return path

        if depth < limit:
            for adj_cell in maze.get_neighbors(cell):
                if adj_cell not in path:
                    stack.append(adj_cell)
            depth += 1

        path.append(cell)

    return []


def iterative_dfs_solver(maze):
    depth_limit = 1
    while True:
        path = dls_solver(maze, depth_limit)
        if maze.goal in path:
            return path
        else:
            depth_limit += 1

    return []


def dfs_solver(maze):
    current = maze.start
    stack = [current]
    path = []

    while len(stack) > 0:
        cell = stack.pop()

        if cell == maze.goal:
            path.append(cell)
            return path

        for adj_cell in maze.get_neighbors(cell):
            if adj_cell not in path:
                stack.append(adj_cell)

        path.append(cell)


def bfs_solver(maze):
    current = maze.start
    queue = [current]
    path = []

    while len(queue) > 0:
        cell = queue.pop()

        if cell == maze.goal:
            path.append(cell)
            return path

        #if cell not in path:
        for adj_cell in maze.get_neighbors(cell):
            if adj_cell not in path:
                queue.insert(0, adj_cell)

        path.append(cell)


def astar_heuristic(maze, cell):
    dist_x = abs(maze.goal[0] - cell[0])
    dist_y = abs(maze.goal[1] - cell[1])

    return (dist_x ** 2 + dist_y ** 2)


def astar_solver(maze):
    current = Cell(maze.start[0], maze.start[1])
    open_list = [current]
    path = []
    while len(open_list) > 0:
        cell = min(open_list, key = lambda x: x.g + x.h)
        if tuple((cell.x, cell.y)) == maze.goal:
            path.append((cell.x, cell.y))
            return path

        open_list.remove(cell)

        if tuple((cell.x, cell.y)) not in path:
            for adj in maze.get_neighbors((cell.x, cell.y)):
                if adj not in path:
                    adj_cell = Cell(adj[0], adj[1])
                    new_g = cell.g + 1
                    adj_cell.g = new_g
                    adj_cell.h = astar_heuristic(maze, (adj_cell.x, adj_cell.y))
                    open_list.append(adj_cell)

        path.append((cell.x, cell.y))

