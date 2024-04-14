'''
Created by: minseo
Date: 4/14/24
Desc : 백준 1325
Excute time : 84ms(백준)
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys
from collections import deque


def BFS():
    while myQueue:
        node = myQueue.popleft()
        for i in range(4):
            next_x, next_y = node[0] + dx[i], node[1] + dy[i]
            # 맵을 벗어날 경우 패스
            if next_x < 0 or next_y < 0 or next_x >= width or next_y >= length:
                continue
            # 범위 내에 있을 경우에만 graph와 visited 확인
            if graph[next_y][next_x] and not visited[next_y][next_x]:
                myQueue.append((next_x, next_y))
                distance[next_y][next_x] = distance[node[1]][node[0]] + 1
                visited[next_y][next_x] = True


sys.stdin = open("BAJ1325.txt")
length, width = map(int, input().split())

# 그래프 생성
graph = [[0 for _ in range(width)] for __ in range(length)]
visited = [[False for _ in range(width)] for __ in range(length)]
distance = [[1 for _ in range(width)] for __ in range(length)]
visited[0][0] = True
# queue 자료구조 생성
myQueue = deque([])

for i in range(length):
    graph[i] = list(map(int, list(input().strip())))

# 좌 우 위 아래 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

myQueue.append((0, 0))
BFS()
print(distance[length - 1][width - 1])

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
