from collections import deque

def bfs(queue,day):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        day += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                check_x, check_y = x + valid_x[i], y + valid_y[i]

                if 0 <= check_x < N and 0 <= check_y < M:
                    if matrix[check_x][check_y] == 0:
                        if matrix[check_x][check_y] != -1:
                            matrix[check_x][check_y] = 1
                            queue.append([check_x,check_y])
    return day

M, N = map(int, input().split())
matrix =[list(map(int, input().split())) for _ in range(N)]
queue = deque()
result = -1
flag = True

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
            
result = bfs(queue, result)

for i in matrix:
    if 0 in i:
        print(-1)
        flag = False
        break

if flag == True:
    print(result)