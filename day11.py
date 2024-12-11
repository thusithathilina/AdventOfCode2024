def part1():
  with open("input.txt") as file:
    numbers = file.readline().split()
    print(numbers)
    for i in range(75):
        print(i)
        new_numbers = []
        for n in numbers:
            if n == "0":
                new_numbers.append("1")
            elif len(n)%2 == 0:
                half = int(len(n)/2)
                new_numbers.append(n[0:half])
                new_numbers.append(str(int(n[half:])))
            else:
                new_numbers.append(str(int(n) * 2024))
        numbers = new_numbers
    print(len(new_numbers))
