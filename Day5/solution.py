import re
from collections import defaultdict
crane_version = 9001
if __name__ == "__main__":
    with open('./input.txt') as fp:
        rows = fp.readlines()
        rows_of_crates = []
        instructions = []
        stacks = defaultdict(lambda: [])

        # gross parsing code
        for row in rows:
            if '[' in row:
                for i, x in enumerate(range(0, len(row), 4)):
                    crate = row[x:x+4].strip()
                    if crate:
                        stacks[i+1].append(crate)
            if 'move' in row:
                # create tuple of (number of crates to move, source crate, destination crate)
                instructions.append(tuple(map(int, re.findall(r'\d+', row))))
        stacks = dict(stacks)
        for number_of_crates_to_move, source_crate, destination_crate in instructions:
            if crane_version == 9000:
                for crate in stacks[source_crate][:number_of_crates_to_move]:
                    stacks[destination_crate].insert(0, crate)
                    stacks[source_crate].remove(crate)
            elif crane_version == 9001:
                stacks[destination_crate] = stacks[source_crate][:number_of_crates_to_move] + stacks[destination_crate]
                stacks[source_crate] = stacks[source_crate][number_of_crates_to_move:]
        print("".join([stacks[stack][0] for stack in sorted(stacks)]).replace("[", "").replace("]", ""))



