def read_maze(file_name):

    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not retangular")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected")
        raise SystemExit
    
if __name__ == "__main__":
    maze = read_maze("mazes_txt/maze_normal.txt")
    for row in maze:
        print(row)

    print("\n----------------\n")
    maze = read_maze("mazes_txt/challenge_maze.txt")
    for row in maze:
        print(row)