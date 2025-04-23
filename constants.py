CELL_SIZE = 20  # size of each cell in grid
GRID_WIDTH = 30 # width of grid in cell size
GRID_HEIGHT = 30 # height of grid in cell size
# dimensions for the pygame window
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 60
STEP_DELAY = 0.1 # Delay between wall removals from Kruskal's algorithm on pygame screen
LINE_DELAY = 0.1 # Delay between BFS line placements from start node to end node in pygame (not relevant to Kruskals algorithm implementation)
LINE_WIDTH = 3  # Size of BFS line drawn on pygame screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)