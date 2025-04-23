import pygame
import random
import time
import constants
from disjoint_set import DisjointSet
from collections import deque

# Initializing Pygame (for Maze Visuals)
pygame.init()

class MazeGenerator:
    # Manages the generation and visualization of the maze.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.walls = []
        self.cells = []
        self.maze_edges = []
        self.start = (0,0)
        self.end = (width - 1, height - 1)
        self.init_grid()
    
    # Creates all possible walls with random weights
    def init_grid(self):
        for y in range(self.height):
            for x in range (self.width):
                cell_id = y * self.width + x
                if x < self.width - 1:
                    # Assign random weight between 1 and 100
                    weight = random.randint(1, 10)
                    self.walls.append((weight, cell_id, cell_id + 1))
                if y < self.height - 1:
                    weight = random.randint(1, 10)
                    self.walls.append((weight, cell_id, cell_id + self.width))
        # Sort walls by weight (ascending)
        self.walls.sort(key=lambda x: x[0])
        self.cells = [(x, y) for y in range(self.height) for x in range(self.width)]
    
    # Draws cells and walls
    def draw_grid(self):
        self.screen.fill(constants.WHITE)
        for y in range(self.height):
            for x in range (self.width):
                cell_x = x * constants.CELL_SIZE
                cell_y = y * constants.CELL_SIZE
                if x < self.width - 1 and (x + y * self.width, x + 1 + y * self.width) not in self.maze_edges:
                    pygame.draw.line(self.screen, constants.BLACK, (cell_x + constants.CELL_SIZE, cell_y), (cell_x + constants.CELL_SIZE, cell_y + constants.CELL_SIZE))
                if y < self.height - 1 and (x + y * self.width, x + (y + 1) * self.width) not in self.maze_edges:
                    pygame.draw.line(self.screen, constants.BLACK, (cell_x, cell_y + constants.CELL_SIZE), (cell_x + constants.CELL_SIZE, cell_y + constants.CELL_SIZE))
                if y == 0:
                    pygame.draw.line(self.screen, constants.BLACK, (cell_x, cell_y), (cell_x + constants.CELL_SIZE, cell_y))
                if x == 0:
                    pygame.draw.line(self.screen, constants.BLACK, (cell_x, cell_y), (cell_x, cell_y + constants.CELL_SIZE))
        start_x, start_y = self.start
        pygame.draw.rect(self.screen, constants.GREEN, (start_x * constants.CELL_SIZE + 2, start_y * constants.CELL_SIZE + 2, constants.CELL_SIZE - 4, constants.CELL_SIZE - 4))
        end_x, end_y = self.end
        pygame.draw.rect(self.screen, constants.RED, (end_x * constants.CELL_SIZE + 2, end_y * constants.CELL_SIZE + 2, constants.CELL_SIZE - 4, constants.CELL_SIZE - 4))
        pygame.display.flip()
    
    # Removes the walls and actually builds the maze using weights
    def kruskals_algorithm(self):
        ds = DisjointSet(self.width * self.height)
        for weight, u, v in self.walls:
            if ds.union(u, v):
                self.maze_edges.append((u, v))
                self.maze_edges.append((v, u))
                # Uncomment below to see wall removal at each step, slows down execution of algorithm at higher grid sizes
                # self.draw_grid()           
                # time.sleep(constants.STEP_DELAY)
    
    def bfs(self):
        # init adjacency list
        adj_dict = {}
        for i in range(self.width * self.height):
            adj_dict[i] = []
        for u, v in self.maze_edges:
            adj_dict[u].append(v)
        start_square = self.start[0] + (self.start[1] * self.width)
        end_square   = self.end[0] + (self.width * self.end[1])
        seen = {start_square: None}
        
        # bfs start
        q = deque([start_square])
        while q:
            u = q.popleft()
            if u == end_square:
                break
            for neighbor_node in adj_dict[u]:
                # print("neighbor node: ", neighbor_node)
                if neighbor_node not in seen:
                    seen[neighbor_node] = u
                    q.append(neighbor_node)
                else:
                    continue
                    # print("node seen already: ", neighbor_node)

        # return path that bfs takes from start to end
        path = []
        while end_square != None:
            path.append(end_square)
            end_square = seen[end_square]
        return path

    def draw_bfs_path(self):
        path_arr = []
        path = self.bfs() 
        for square in path:
            # coords for center of cells
            x = (square % self.width) * constants.CELL_SIZE + (constants.CELL_SIZE // 2)
            y = (square // self.width) * constants.CELL_SIZE + (constants.CELL_SIZE // 2)
            path_arr.append((x, y))
        
        # draw lines on screen from start to end
        path_arr.reverse()
        for i in range(1, len(path_arr)):
            pygame.draw.line(self.screen, constants.BLACK, path_arr[i-1], path_arr[i], constants.LINE_WIDTH)
            time.sleep(constants.LINE_DELAY)
            pygame.display.flip()
        
    # Organizes the generation process.          
    def generate_maze(self):
        self.draw_grid()
        time.sleep(2)
        start_time = time.perf_counter()
        # Code to measure
        self.kruskals_algorithm()
        end_time = time.perf_counter()
        print(f"Execution time: {(end_time - start_time):.4f} seconds")
        self.draw_grid()
        self.draw_bfs_path()