n = int(input())
plan = input().split()

dx = [0,0,-1,1] # L, R, U , D
dy = [-1,1,0,0]

x , y = 1 ,1

move_types = ['L','R','U','D']

for i in range(len(plan)):
    for j in range(len(move_types)):
        if plan[i] == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or nx > n or ny <1 or ny >n :
        continue
    
    x,y = nx,ny

print(x,y)