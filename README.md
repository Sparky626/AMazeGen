# COP4533 - Final Project - AMazeGenerator (Kruskal's MST Algorithm)

This project is for UF's Algorithm Abstraction and Design Class and uses Kruskal's Algorithm to generate a Maze which is essentially a Minimum Spanning Tree.

## How to Run
Run `main.py` to view output.

## Constants
- `CELL_SIZE`: Size of each cell in the grid
- `GRID_WIDTH`: Width of the grid in cells (default is 50 but can be changed for different sized mazes)
- `GRID_HEIGHT`: Height of the grid in cells (default is 50 but can be changed for different sized mazes)
- `WINDOW_WIDTH`: Pygame window width
- `WINDOW_HEIGHT`: Pygame window height
- `FPS`: Frames per second for Pygame rendering
- `STEP_DELAY`: Delay between wall removals during Kruskal's algorithm visualization (currently not in use to as visualizing the algorithm slows down the process a lot)
- `LINE_DELAY`: Delay between drawing BFS path lines
- `LINE_WIDTH`: Width of the BFS path lines
- `WHITE`, `BLACK`, `GREEN`, `RED`: RGB color values for rendering the maze, walls, start/end points, and BFS path.

## Functions
### `disjoint_set.py`
- `DisjointSet.__init__(size)`: Initializes a disjoint set for `size` cells, with each cell as its own set.
- `DisjointSet.find(x)`: Finds the root of the set containing cell `x` using path compression.
- `DisjointSet.union(x, y)`: Merges the sets containing cells `x` and `y` using rank-based union, returns `True` if merged, `False` if already connected.

### `maze_generator.py`
- `MazeGenerator.__init__(width, height)`: Initializes the maze with specified dimensions, sets up Pygame, and prepares walls and cells.
- `MazeGenerator.init_grid()`: Creates a list of weighted walls (horizontal and vertical) and sorts them by weight.
- `MazeGenerator.draw_grid()`: Renders the maze grid, walls, and start/end points (green for start, red for end).
- `MazeGenerator.kruskals_algorithm()`: Implements Kruskal's algorithm to generate the maze by removing walls to form a minimum spanning tree.
- `MazeGenerator.bfs()`: Performs a breadth-first search to find a path from the start (top-left) to the end (bottom-right).
- `MazeGenerator.draw_bfs_path()`: Draws the BFS path on the Pygame screen with delays between line segments.
- `MazeGenerator.generate_maze()`: Orchestrates maze generation, visualization, and BFS path drawing, including timing the algorithm.

### `main.py`
- `main()`: Initializes the maze generator, runs the maze generation process, and handles the Pygame event loop.

## How it Works
1. **Grid Initialization**: A grid of cells is created with walls (horizontal and vertical) assigned random weights between 1 and 10.
2. **Kruskal's Algorithm**: Walls are sorted by weight, and the algorithm iteratively removes walls to connect cells, using a `DisjointSet` to prevent cycles, forming a maze.
3. **Visualization**: The maze is rendered in Pygame, with walls drawn as black lines, the start cell (0,0) in green, and the end cell (width-1, height-1) in red.
4. **BFS Pathfinding**: A breadth-first search finds the shortest path from start to end, which is then drawn as a black line with configurable delays.
5. **Customization**: Adjust grid size, delays, and rendering settings in `constants.py`.

To view the implementation for different size grids, wall removal speeds, BFS line drawing speeds, etc., edit values in `constants.py`.

To view the implementation at smaller grid sizes (such as 15 x 15), uncomment the following lines in `kruskals_algorithm()` in `maze_generator.py`:
These are disabled by default to allow for larger input sizes to be run for testing.
```python
# self.draw_grid()
# time.sleep(constants.STEP_DELAY)
```
