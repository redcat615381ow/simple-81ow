"""Simple 2D grid game prototype."""

def main():
    grid = [
        list("P...."),
        list("..#.."),
        list("..#.."),
        list("..#.."),
        list("....G")
    ]
    moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    while True:
        for row in grid:
            print(''.join(row))
        cmd = input("Move (w/a/s/d): ").lower()
        if cmd not in moves:
            print("Invalid move.")
            continue
        dr, dc = moves[cmd]
        r, c = next((r, c) for r, row in enumerate(grid)
                    for c, v in enumerate(row) if v == 'P')
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
            grid[r][c] = '.'
            grid[nr][nc] = 'P'
            if grid[nr][nc] == 'G':
                print("You reached the goal!")
                break
        else:
            print("Can't move there.")

if __name__ == "__main__":
    main()