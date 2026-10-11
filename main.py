"""Simple 2D grid game prototype."""
WIDTH, HEIGHT = 10, 10

def init_grid(p_pos):
    return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def draw(grid, p_pos):
    g = [row[:] for row in grid]
    x, y = p_pos
    g[y][x] = 'P'
    print("\n".join("".join(row) for row in g))

def move(p_pos, key):
    x, y = p_pos
    if key == 'w' and y > 0: y -= 1
    elif key == 's' and y < HEIGHT-1: y += 1
    elif key == 'a' and x > 0: x -= 1
    elif key == 'd' and x < WIDTH-1: x += 1
    return x, y

def main():
    pos = (0, 0)
    while True:
        grid = init_grid(pos)
        draw(grid, pos)
        cmd = input("Move (w/a/s/d) or q to quit: ").strip().lower()
        if cmd == 'q': break
        if cmd in 'wasd': pos = move(pos, cmd)
        print("\n" * 2)

if __name__ == "__main__":
    main()