from typing import List


def print_grid(grid: List[List[bool]]):
    for row in grid:
        for col in row:
            print(col, end='\t')
        print()

if __name__ == "__main__":
    with open('./input.txt') as f:
        motions = list(map(lambda x: x.split(" "), map(str.strip, f.readlines())))
        motions = list(map(lambda x: (x[0], int(x[1])), motions))
        cols = max(steps for direction, steps in motions if direction in ('R', 'L')) + 1
        rows = max(steps for direction, steps in motions if direction in ('U', 'D')) + 1
        #print(rows)
        #print(cols)
        grid = [cols*[False] for _ in range(rows)]
        head_x_position = 0
        head_y_position = rows - 1
        tail_x_position, tail_y_position = head_x_position, head_y_position
        grid[head_y_position][head_x_position] = True
        print_grid(grid)
        for direction, steps in motions:
            print(direction, steps)
            for step in range(steps):
                old_head_position = head_x_position, head_y_position
                if direction == 'R':
                    head_x_position += 1
                elif direction == 'L':
                    head_x_position -= 1
                elif direction == 'U':
                    head_y_position -= 1
                elif direction == 'D':
                    head_y_position += 1
                if abs(head_x_position - tail_x_position) <= 1 and abs(head_y_position - tail_y_position) == 0 or \
                    abs(head_y_position - tail_y_position) <= 1 and abs(head_x_position - tail_x_position) == 0:
                        # we're on or next to the head, no movement
                    ...
                elif abs(head_x_position - tail_x_position) == 1 and abs(head_y_position - tail_y_position) == 1:
                     # the head has moved diagonally - don't do anything. We'll get it next time.
                    ...
                else:
                    # the head has moved on the same axis - just follow
                    tail_x_position, tail_y_position = old_head_position
                grid[tail_y_position][tail_x_position] = True
                #print_grid(grid)
        print(sum(sum(col for col in row) for row in grid))
