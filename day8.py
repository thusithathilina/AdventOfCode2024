def part1():
  with open("input.txt") as file:
    sum = 0
    dict = {}
    i = 0
    for line in file:
        j = 0
        for c in line.strip():
            if c != '.':
                if c in dict:
                    dict[c].append((i,j))
                else:
                    dict[c] = [(i,j)]
            j += 1
        i += 1
    length = i

    antinodes = set()
    for key in dict.keys():
        values = dict[key]
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                x1, y1 = values[i]
                x2, y2 = values[j]
                xdiff = x1-x2
                ydiff = y1-y2

                if xdiff < 0:
                    newX1 = x1 + xdiff
                    newX2 = x2 - xdiff
                else:
                    newX1 = x1 - xdiff
                    newX2 = x2 + xdiff

                newY1 = y1 + ydiff
                newY2 = y2 - ydiff

                if 0 <= newX1 < length and 0 <= newY1 < length:
                    antinodes.add((newX1, newY1))
                if 0 <= newX2 < length and 0 <= newY2 < length:
                    antinodes.add((newX2, newY2))
    print(len(antinodes))


