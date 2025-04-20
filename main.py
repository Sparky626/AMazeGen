import pygame
import constants
from maze_generator import MazeGenerator

def main():
    maze = MazeGenerator(constants.GRID_WIDTH, constants.GRID_HEIGHT)
    maze.generate_maze()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        maze.clock.tick(constants.FPS)
    pygame.quit()

if __name__ == "__main__":
    main()