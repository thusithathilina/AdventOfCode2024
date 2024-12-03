import re

def part1():
    with open("input.txt") as file:
        sum = 0
        for line in file:
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
            for match in matches:
                match = match[4:-1]
                x, y = match.split(",")
                sum += int(x) * int(y)
        print(sum)

def part2():
    with open("input.txt") as file:
        sum = 0
        text = ""
        for line in file:
            text += line[0:-1]
        replaced = re.sub('don\'t\(\).*?do\(\)', 'a', text)
        matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', replaced)
        for match in matches:
            match = match[4:-1]
            x, y = match.split(",")
            sum += int(x) * int(y)
        print(sum)
