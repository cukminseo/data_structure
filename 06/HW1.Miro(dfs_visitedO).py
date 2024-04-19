import sys
from collections import deque

sys.stdin = open("HW1.Miro.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(next):
    now_x, now_y = next[0], next[1]
    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0 <= next_x < 16 and 0 <= next_y < 16 and miro[next_y][next_x] != 1 and not visited[next_y][next_x]:
            if miro[next_y][next_x] == 3:
                visited[next_y][next_x] = 3
                break
            else:
                visited[next_y][next_x] = 1
            DFS((next_x, next_y))


for i in range(1, 11):
    tc = int(input())

    miro = []
    visited = [[0 for _ in range(16)] for _ in range(16)]

    for _ in range(16):
        miro.append(list(map(int, list(input()))))

    DFS((1, 1))
    if max(map(max, visited)) == 3:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
