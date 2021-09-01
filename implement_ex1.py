#구현문제 예제 
#상하좌우 문제  소요시간 20분 

n = int(input())
plans = input().split()

x, y = 1, 1

# L = (0, -1) R = (0, +1) U = (-1, 0) D = (+1, 0)
#L,R,U,D 차례대로 조합 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']


for i in plans:
    nx = x + dx[move_types.index(i)]
    ny = y + dy[move_types.index(i)]

    if nx > n or ny > n or nx < 1 or ny <1:
        continue
    
    x, y = nx, ny 

print(x,y)
