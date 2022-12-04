from typing import List, Set


def compute_section_range(section: str) -> Set[int]:
    section_begin, section_end = map(int, section.split("-"))
    return set(range(section_begin, section_end+1))


def check_for_section_overlap(first_elf_section: str, second_elf_section: str) -> bool:
    first_elf_section_begin, first_elf_section_end = map(int, first_elf_section.split("-"))
    second_elf_section_begin,second_elf_section_end = map(int, second_elf_section.split("-"))
    return (first_elf_section_begin >= second_elf_section_begin and first_elf_section_end <= second_elf_section_end) or \
            (second_elf_section_begin >= first_elf_section_begin and second_elf_section_end <= first_elf_section_end)





if __name__ == "__main__":
    count = 0
    count_part_2 = 0
    with open('./input.txt') as f:
        assignment_pairs = [x.strip() for x in f.readlines()]
        for assignment_pair in assignment_pairs:
            first_elf_assignment, second_elf_assignment = assignment_pair.split(",")
            count += check_for_section_overlap(first_elf_assignment, second_elf_assignment)
            count_part_2 += 1 if compute_section_range(first_elf_assignment) & compute_section_range(second_elf_assignment) else 0
    print(count)
    print(count_part_2)



