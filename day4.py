import pandas as pd
import numpy as np
import re


def part1():
    with open("input.txt") as file:
        sum = 0
        lines = []
        for line in file:
            lines.append(line)
            sum += len(re.findall(r'XMAS', line))
            sum += len(re.findall(r'XMAS', line[::-1]))

        df = pd.DataFrame([list(line) for line in lines])
        df = df.drop(df.columns[-1], axis=1)
        for i in range(len(df.columns)):
            tmpword = ''.join(df.loc[:,i])
            sum += len(re.findall(r'XMAS', tmpword))
            sum += len(re.findall(r'XMAS', tmpword[::-1]))

        matrix = np.array(df)
        ndim = matrix.shape[0]
        diags = [np.diag(matrix, i).tolist() for i in range(-ndim + 1, ndim)][::-1]
        for d_row in diags:
            tmpword = ''.join(d_row)
            sum += len(re.findall(r'XMAS', tmpword))
            sum += len(re.findall(r'XMAS', tmpword[::-1]))

        matrix = np.fliplr(matrix)
        ndim = matrix.shape[0]
        diags = [np.diag(matrix, i).tolist() for i in range(-ndim + 1, ndim)][::-1]
        for d_row in diags:
            tmpword = ''.join(d_row)
            sum += len(re.findall(r'XMAS', tmpword))
            sum += len(re.findall(r'XMAS', tmpword[::-1]))
        print(sum)


def part2():
    with open("input.txt") as file:
        sum = 0
        lines = []
        for line in file:
            lines.append(line)
        df = pd.DataFrame([list(line) for line in lines])
        df = df.drop(df.columns[-1], axis=1)
        matrix = df.to_numpy()
        for i in range(len(lines)-2):
            for j in range(len(matrix[i])-2):
                right = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2]
                left = matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j]
                if (right == "MAS" or right == "SAM") and (left == "MAS" or left == "SAM"):
                    sum += 1
        print(sum)
