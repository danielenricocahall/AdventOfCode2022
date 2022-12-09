if __name__ == "__main__":
    map_of_trees = []
    with open('./input.txt') as f:
        for line in f:
            map_of_trees.append(list(map(int, list(line.strip()))))

    rows = len(map_of_trees)
    cols = len(map_of_trees[0])
    trees_visible_on_interior = 0
    trees_visible_on_exterior = 2 * rows + 2 * cols - 4
    scenic_scores = []
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            current_tree = map_of_trees[row][col]
            trees_below = [map_of_trees[_row][col] for _row in range(row+1, rows)]
            trees_above = [map_of_trees[_row][col] for _row in range(row)]
            trees_left = [map_of_trees[row][_col] for _col in range(col)]
            trees_right = [map_of_trees[row][_col] for _col in range(col+1, cols)]
            # Part 1
            if all(current_tree > tree for tree in trees_below) or \
                all(current_tree > tree for tree in trees_above) or \
                all(current_tree > tree for tree in trees_left) or \
                all(current_tree > tree for tree in trees_right):
                trees_visible_on_interior += 1
            # Part 2
            # NOTE: we need to do `reversed` on above and left because they were added in sequential order,
            # but from the perspective of the tree, we need to count outward
            scenic_score = next((i+1 for i, tree in enumerate(trees_below) if tree >= current_tree), len(trees_below)) * \
                next((i+1 for i, tree in enumerate(reversed(trees_above)) if tree >= current_tree), len(trees_above)) * \
                next((i+1 for i, tree in enumerate(reversed(trees_left)) if tree >= current_tree), len(trees_left)) * \
                next((i+1 for i, tree in enumerate(trees_right) if tree >= current_tree), len(trees_right))
            print(f"Scenic score {scenic_score} at {current_tree} ({row}, {col})")
            scenic_scores.append(scenic_score)
    print(trees_visible_on_interior + trees_visible_on_exterior)
    print(max(scenic_scores))





