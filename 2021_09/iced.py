#음료수 얼려먹기 
#난이도 1.5/ 3.0
 
n, m = map(int,input().split())

map_list = list()
for i in range(n):
    map_list.append(list(map(int,input().split())))

result = 0 

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >=m:
        return False
    if map_list[x][y] == 0:
        print(x,y)
        map_list[x][y] = 1

        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False 

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
