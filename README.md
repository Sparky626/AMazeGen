
# COP4533 - Final Project - AMazeGenerator (Kruskal's MST Algorithm)

This project is for UF's Algorithm Abstraction and Design Class and uses Kruskal's Algorithm to generate a Maze which is basically a Minimum Spanning Tree

## How to run
after cloning with git clone, install pygame in terminal with:
"pip install pygame"

run main.py to view output

## Variables

## Functions

## How it Works

To view our implementation for different size grids, wall removal speeds, bfs line drawing speeds, etc., edit values in constants.py.

To view implementation at smaller grid size inputs (such as 15 x 15), uncomment the following lines in kruskals_algorithm() in maze_generator.py:

"# self.draw_grid()"                 
"# time.sleep(constants.STEP_DELAY)"

These are disabled by default to allow for larger input sizes to be ran for testing

In main.py, set "running" to False to test very large input sizes, which will stop rendering to pygame, otherwise leave as True to view kruskal's algorithm 

