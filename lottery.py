# coding: utf-8

n, m = [int(i) for i in input().split()]

array = []
for i in range(n):
    array.append([int(i) for i in input().split()])


maximums = []

for i in range(m):
    columns = []
    for x in range(n):
        columns.append(array[x][i])git 
    maximums.append(max(columns))

print(min(maximums))
