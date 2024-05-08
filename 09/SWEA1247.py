import sys


def DFS(node):
    global min_distance, distance

    # 너무 커지지 않도록
    if min_distance < distance:
        return

    # 집인지 확인
    if node == go_list[1]:
        # 집이면 다른 손님들 집 다 돌고왔는지 확인
        if all(visited) and min_distance > distance:
            # 이때까지 거리보다 짧으면 새로 변경
            min_distance = distance
        return

    now_x, now_y = node[0], node[1]
    for next_node in range(map_size):
        if not visited[next_node]:
            next_x, next_y = go_list[next_node]
            distance += abs(now_x - next_x) + abs(now_y - next_y)
            visited[next_node] = 1

            DFS((next_x, next_y))

            # 흔적 지우기
            distance -= abs(now_x - next_x) + abs(now_y - next_y)
            visited[next_node] = 0


sys.stdin = open('SWEA1247.txt', 'r')

for tc in range(int(input())):
    num_of_customer = int(input())
    input_link = list(map(int, input().split()))

    map_size = num_of_customer + 2

    visited = [0 for _ in range(map_size)]
    go_list = []

    # input
    for idx in range(0, (num_of_customer + 2) * 2, 2):
        start, end = input_link[idx], input_link[idx + 1]
        go_list.append((start, end))

    min_distance = 9999
    distance = 0

    visited[0] = 1
    DFS(go_list[0])

    print(f"#{tc+1} {min_distance}")
