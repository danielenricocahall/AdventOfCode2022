if __name__ == "__main__":
    map_of_trees = []
    with open('./input.txt') as f:
        for line in f:
            map_of_trees.append(list(map(int, list(line.strip()))))

    rows = len(map_of_trees)
    cols = len(map_of_trees[0])
    trees_visible_on_interior = 0
    trees_visible_on_exterior = 2 * rows + 2 * cols - 4
    print(trees_visible_on_exterior)
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            current_tree = map_of_trees[row][col]
            trees_below = [map_of_trees[_row][col] for _row in range(row+1, rows)]
            trees_above = [map_of_trees[_row][col] for _row in range(row)]
            trees_left = [map_of_trees[row][_col] for _col in range(col)]
            trees_right = [map_of_trees[row][_col] for _col in range(col+1, cols)]
            if all(current_tree > tree for tree in trees_below) or \
                all(current_tree > tree for tree in trees_above) or \
                all(current_tree > tree for tree in trees_left) or \
                all(current_tree > tree for tree in trees_right):
                trees_visible_on_interior += 1
    print(trees_visible_on_interior + trees_visible_on_exterior)





