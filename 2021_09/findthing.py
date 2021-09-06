#부품찾기 문제
#난이도 1.5 소요시간 10분

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

def search(array, t):
    for i in range(len(array)):
        if array[i] == t:
            return True 

for i in m_list:
    if search(n_list,i):
        print('yes')
    else:
        print('no')
