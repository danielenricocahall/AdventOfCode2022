from typing import List, Optional

THRESHOLD = 100000


class Node:
    children: List["Node"] = []
    parent: Optional["Node"] = None
    size: Optional[int] = None

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.value})"


def find_parent(node: Node):
    if node.parent is None:
        return node
    else:
        return find_parent(node.parent)


def calculate_size(node: Node):
    # A recursive function that finds directories with no size, then looks through its children
    # and calculates its total size.
    dir_size = 0
    for child in node.children:
        if child.size is None:  # This means this is a directory we haven't sized yet
            child.size = calculate_size(child)  # Recursively calculate size of child directory
        dir_size += child.size  # Add the size of this child directory or file to the total
    return dir_size


if __name__ == "__main__":
    with open('input.txt', 'r') as fp:
        commands = list(map(str.strip, fp.readlines()))
        nodes = []
        current_node = None
        for command in commands:
            if '$ cd' in command:
                _, current_directory = command.split('$ cd ')
                if current_directory == "..":
                    current_node = current_node.parent
                else:
                    if current_node:
                        current_node = next(
                            node for node in current_node.children if node.value == current_directory)
                    else:
                        current_node = Node(current_directory)
            elif "dir " in command:
                _, directory_name = command.split("dir ")
                child_node = Node(directory_name)
                child_node.parent = current_node
                current_node.children.append(child_node)
                nodes.append(child_node)
            elif "$ ls" not in command:
                file_size, file = command.split(" ")
                leaf_node = Node(file)
                leaf_node.size = int(file_size)
                current_node.children.append(leaf_node)
        root = find_parent(current_node)
        final_size = 0
        calculate_size(root)
        for node in nodes:
            if node.size <= THRESHOLD:
                final_size += node.size
        print(final_size)
