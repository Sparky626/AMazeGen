import pygame
import random
import time
import constants
from disjoint_set import DisjointSet

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
    
    # Creates all possible walls
    def init_grid(self):
        for y in range(self.height):
            for x in range (self.width):
                cell_id = y * self.width + x
                if x < self.width - 1:
                    self.walls.append((cell_id, cell_id + 1))
                if y < self.height - 1:
                    self.walls.append((cell_id, cell_id + self.width))
        random.shuffle(self.walls)
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
    # Removes the walls and actually builds the maze
    def kruskals_algorithm(self):
        ds = DisjointSet(self.width * self.height)
        for u, v in self.walls:
            if ds.union(u, v):
                self.maze_edges.append((u, v))
                self.maze_edges.append((v, u))
                self.draw_grid()
                time.sleep(constants.STEP_DELAY)
    # Organizes the generation process.          
    def generate_maze(self):
        self.draw_grid()
        time.sleep(2)
        self.kruskals_algorithm()
        self.draw_grid()