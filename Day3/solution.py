from functools import reduce

if __name__ == "__main__":
    import string
    with open('./input.txt', 'r') as f:
        item_to_priority = {item: priority + 1 for priority, item in enumerate(string.ascii_letters)}
        sum_of_priorities = 0
        for line in f:
            line = line.strip()
            first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]
            items_appearing_in_both_compartments = set(first_compartment) & set(second_compartment)
            sum_of_priorities += sum(map(item_to_priority.get, items_appearing_in_both_compartments))
        print(sum_of_priorities)
    with open('./input.txt') as f:
        elf_group_size = 3
        rucksacks = [x.strip() for x in f.readlines()]
        groups = [rucksacks[i:i+elf_group_size] for i in range(0, len(rucksacks), elf_group_size)]
        badges = [list(reduce(set.intersection, map(set, group)))[0] for group in groups]
        sum_of_priorities = sum(map(item_to_priority.get, badges))
        print(sum_of_priorities)
