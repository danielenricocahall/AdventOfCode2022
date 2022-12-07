from typing import List, Optional

THRESHOLD = 100000


class Node:
    children: List["Node"] = []
    parent: Optional["Node"] = None
    _size: int = 0

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.value})"

    def size(self):
        return self._size + sum(child.size() for child in self.children)


def compute_sum(node: Node) -> int:
    if node.size() > THRESHOLD:
        return sum([compute_sum(child) for child in node.children])
    return node.size()


def find_parent(node: Node):
    if node.parent is None:
        return node
    else:
        return find_parent(node.parent)


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
            elif "dir" in command:
                _, directory_name = command.split("dir ")
                child_node = Node(directory_name)
                child_node.parent = current_node
                current_node.children.append(child_node)
            elif "$ ls" not in command:
                file_size, file = command.split(" ")
                leaf_node = Node(file)
                leaf_node._size = int(file_size)
                current_node.children.append(leaf_node)
                current_node._size += int(file_size)
        root = find_parent(current_node)
        print(compute_sum(root))
