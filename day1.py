def part1():
    list1 = []
    list2 = []
    with open("input.txt") as file:
        for line in file:
            values = line.split()
            list1.append(int(values[0]))
            list2.append(int(values[1]))

    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
    print(sum)

def part2():
    list1 = []
    list2_dict = {}
    with open("input.txt") as file:
        for line in file:
            values = line.split()
            list1.append(int(values[0]))
            no2 = int(values[1])
            if no2 in list2_dict:
                list2_dict[no2] += 1
            else:
                list2_dict[no2] = 1

    sum = 0
    for no1 in list1:
        if no1 in list2_dict:
            sum += no1 * list2_dict[no1]
    print(sum)
