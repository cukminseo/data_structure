
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('SW1216.txt', 'r')

def isPalin(y,x,howmany):
    for now in range(howmany//2):
        if data[y][x+now]!=data[y][x+howmany-1-now]:
            return False
    return True

for _ in range(1,11):
    tc = input()
    max_palin_len = 0
    howmany = 2

    data = [0] * 100
    for i in range(100):
        data[i] = list(input())

    for howmany in range(2, 100):

        ans = 0
        for y in range(100):
            for x in range(100-howmany+1):
                if isPalin(y,x,howmany):
                    max_palin_len = howmany

        for y in range(100):
            for x in range(100):
                if y>x:
                    data[y][x], data[x][y] = data[x][y], data[y][x]

        for y in range(100):
            for x in range(100-howmany+1):
                if isPalin(y,x,howmany):
                    max_palin_len = howmany

    print(f"#{tc} {max_palin_len}")
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
