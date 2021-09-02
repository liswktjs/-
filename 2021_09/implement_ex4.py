#구현문제 마지막
#게임개발 

#n *m 크기의 맵, x,y는 좌표 , d는 방향 

#게임 룰 
#북 0, 동 1, 남 2, 서 3  
#map에서 1은 가지 못하는 곳 0 은 갈 수 있는 곳 / map이 모두 1이 되거나 움직일 수 없을 때 까지 이동한다 
#1단계 플레이어의 왼쪽 부터 보기 
#2단계 왼쪽이 1이 아닌 경우 dircetion index -1 하기 + 그쪽 방향으로 이동
# 또는 왼쪽이 1인경우 dirction 만 -1 하기 -> 왼쪽으로 방향 틀기 (1단계)
# 또는 왼쪽이 1이고  그쪽 방향이 모두 가본 곳이라면  뒤록 갈 수 있다면 뒤로 이동한다 

#풀이 


n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x,y,direction = map(int, input().split())
#유저가 현재 위치한 곳을 방문한 것으로 처리한다 
d[x][y] = 1

#map에 대한 정보를 입력 받는다
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time =0 

print(count)




