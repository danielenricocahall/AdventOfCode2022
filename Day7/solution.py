import random
from collections import defaultdict
THRESHOLD = 100000
if __name__ == "__main__":
    with open('input.txt', 'r') as fp:
        commands = list(map(str.strip, fp.readlines()))
        stack = []
        hierarchy = defaultdict(list)
        directory_to_size = defaultdict(int)
        for command in commands:
            if '$ cd' in command:
                _, directory = command.split('$ cd ')
                if directory == "..":
                    directory = stack.pop()
                else:
                    if stack:
                        if len(stack) > 1:
                            parent_directory = stack[-2]
                            duplicated_directory = next(
                                (directory for directory, children_directories in hierarchy.items()
                                 if directory != parent_directory and current_directory in children_directories), None)
                            if duplicated_directory:
                                print(f"THIS IS WHAT PHIL WAS TALKING ABOUT - {current_directory} is in both {parent_directory} and {duplicated_directory}")
                                directory = f"{directory}_{random.randint(0, 1000)}"
                        hierarchy[stack[-1]].append(directory)
                    else:
                        hierarchy[directory] = []
                    stack.append(directory)
            elif "$ ls" not in command and "dir" not in command:
                file_size, file = command.split(" ")
                current_directory = stack[-1]
                directory_to_size[current_directory] += int(file_size)
        sum_of_sizes = 0
        for parent_directory, child_directories in hierarchy.items():
            total_size_of_directory = directory_to_size[parent_directory] + \
                                      sum(map(lambda x: directory_to_size.get(x, 0), child_directories))
            print(f"Directory {parent_directory} has size {total_size_of_directory} bytes")
            if total_size_of_directory <= THRESHOLD:
                sum_of_sizes += total_size_of_directory
        for directory, size_of_directory in directory_to_size.items():
            if directory not in hierarchy.keys():
                print(f"Directory {directory} has size {size_of_directory} bytes")
                if size_of_directory <= THRESHOLD:
                    sum_of_sizes += size_of_directory
        print(sum_of_sizes)

