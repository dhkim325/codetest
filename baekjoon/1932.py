import sys

n = int(input())
triangle = []

for idx in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
    
for i_idx in range(1,len(triangle)):
    for j_idx in range(len(triangle[i_idx])):
        if j_idx == 0:
            triangle[i_idx][j_idx] += triangle[i_idx - 1][j_idx]
        elif j_idx == len(triangle[i_idx]) - 1:
            triangle[i_idx][j_idx] += triangle[i_idx - 1][j_idx - 1]
        else:
            triangle[i_idx][j_idx] += max(triangle[i_idx - 1][j_idx - 1], triangle[i_idx - 1][j_idx])

print(max(triangle[-1]))