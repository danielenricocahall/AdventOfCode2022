

if __name__ == "__main__":
    all_elf_cals = []
    current_elf_cals = []
    with open('./input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                current_elf_cals.append(int(line))
            else:
                all_elf_cals.append(current_elf_cals)
                current_elf_cals = []

    all_elf_total_cals = list(map(sum, all_elf_cals))
    sorted_all_elf_total_cals =sorted(all_elf_total_cals, reverse=True)
    print(sum(sorted_all_elf_total_cals[:3]))
