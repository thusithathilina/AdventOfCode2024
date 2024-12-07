import itertools
import operator

def part1():
    with open("input.txt") as file:
        sum = 0
        for line in file:
            target, values = line.strip().split(":")
            target = int(target)
            values = list(map(int, values.strip().split(" ")))
            possibilities = itertools.product([operator.add, operator.mul], repeat=len(values) - 1)
            for possibility in possibilities:
                ans = values[0]
                for i in range(1, len(values)):
                    ans = possibility[i-1](ans, values[i])
                if ans == target:
                    sum += target
                    break
    print(sum)

def part2():
    with open("input.txt") as file:
        sum = 0
        lines = []
        for line in file:
            lines.append(line.strip())
        j = 0
        while j < len(lines):
            line = lines[j].strip()
            target, values = line.split(":")
            target = int(target)
            values = list(map(int, values.strip().split(" ")))
            possibilities = itertools.product([operator.add, operator.mul], repeat=len(values) - 1)
            for possibility in possibilities:
                ans = values[0]
                for i in range(1, len(values)):
                    ans = possibility[i-1](ans, values[i])
                if ans == target:
                    sum += target
                    lines.remove(line)
                    j -= 1
                    break
            j += 1
        for line in lines:
            target, values = line.strip().split(":")
            target = int(target)
            values = list(map(int, values.strip().split(" ")))
            possibilities = itertools.product([operator.add, operator.mul, operator.concat], repeat=len(values) - 1)
            for possibility in possibilities:
                ans = values[0]
                for i in range(1, len(values)):
                    if possibility[i-1] == operator.concat:
                        ans = int(f"{ans}{values[i]}")
                    else:
                        ans = possibility[i-1](ans, values[i])
                if ans == target:
                    sum += target
                    break
    print(sum)
