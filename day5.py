def part1():
    with open("input.txt") as file:
        rules = {}
        updates = []
        for line in file:
            if "|" in line:
                x, y = line.strip().split("|")
                x = int(x)
                y = int(y)
                if x in rules:
                    rules[x].append(y)
                else:
                    rules[x] = [y]
            elif line.strip() == "":
                continue
            else:
                updates.append(list(map(int, line.strip().split(","))))

        sum = 0
        for update in updates:
            valid = True
            for i in range(len(update)):
                if update[i] in rules:
                    breaking_pages = rules[update[i]]
                    if any(item in breaking_pages for item in update[0:i]):
                        valid = False
                        break
            if valid:
                sum += update[int(len(update)/2)]
        print(sum)

def part2():
    with open("input.txt") as file:
        rules = {}
        updates = []
        for line in file:
            if "|" in line:
                x, y = line.strip().split("|")
                x = int(x)
                y = int(y)
                if x in rules:
                    rules[x].append(y)
                else:
                    rules[x] = [y]
            elif line.strip() == "":
                continue
            else:
                updates.append(list(map(int, line.strip().split(","))))
    
        sum = 0
        for update in updates:
            valid = True
            for i in range(len(update)):
                if update[i] in rules:
                    breaking_pages = rules[update[i]]
                    if any(item in breaking_pages for item in update[0:i]):
                        valid = False
                        break
            if valid:
                continue
            for i in range(len(update)):
                swapped = False
                for j in range(0, len(update)-i-1):
                    if update[j+1] in rules and update[j] in rules[update[j+1]]:
                        update[j], update[j+1] = update[j+1], update[j]
                        swapped = True
                if not swapped:
                    break
            sum += update[int(len(update)/2)]
        print(sum)
