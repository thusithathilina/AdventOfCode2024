def part1():
  with open("input.txt") as file:
    line = file.readline()
  representation = ""
  i = 0
  j = 0
  for d in line:
      if i % 2 == 0:
          representation += str(j) * int(d)
          j += 1
      else:
          representation += "." * int(d)
      i += 1
  
  representation = [c for c in representation]
  left = 0
  right = len(representation) - 1
  while left < right:
      if representation[left] != ".":
          left += 1
      if representation[left] == "." and representation[right] != ".":
          representation[left] = representation[right]
          representation[right] = "."
          left += 1
          right -= 1
      if representation[right] == ".":
          right -= 1
  
  sum = 0
  i = 0
  for d in representation:
      if d != ".":
          sum += i * int(d)
      i += 1
  print(sum)
