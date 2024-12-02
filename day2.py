def part1():
    with open("input.txt") as file:
        count = 0
        for line in file:
            values = list(map(int, line.split()))
            sign = values[0]-values[1]
            flag = True
            for i in range(0, len(values)-1):
                diff = values[i]-values[i+1]
                adiff = abs(diff)
                if adiff < 1 or adiff > 3:
                    flag = False
                    break
                if diff < 0 < sign or diff > 0 > sign:
                    flag = False
                    break
            if flag:
                count+=1
        print(count)


def part2():
    with open("input.txt") as file:
    count = 0
    for line in file:
        values = list(map(int, line.split()))
        sign = values[0] - values[1]
        flag = True
        diff_list = []
        for i in range(len(values)-1):
            diff = values[i] - values[i+1]
            diff_list.append(diff)
            adiff = abs(diff)
            if adiff < 1 or adiff > 3:
                flag = False
            if diff < 0 < sign or diff > 0 > sign:
                flag = False
        if flag:
            count+=1
        else:
            for i in range(len(values)):
                updated_diff_list = diff_list[:]
                flag = True
                if i == 0:
                    updated_diff_list = diff_list[1:]
                elif i == len(values) - 1:
                    updated_diff_list = diff_list[0:-1]
                else:
                    updated_diff_list[i-1] = diff_list[i-1] + diff_list[i]
                    del updated_diff_list[i]
                sign = updated_diff_list[0]
                for x in range(len(updated_diff_list)):
                    if updated_diff_list[x] < 0 < sign or updated_diff_list[x] > 0 > sign:
                        flag = False
                        break
                    if abs(updated_diff_list[x]) < 1 or abs(updated_diff_list[x]) > 3:
                        flag = False
                        break
                if flag:
                    count+=1
                    break

    print(count)
