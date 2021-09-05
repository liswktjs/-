#성적이 낮은 순서로 학생 출력하기
#난이도 1.0 

n = int(input())

data_list = []

for i in range(n):
    data = input().split()
    data_list.append((data[0], data[1]))

data_list = sorted(data_list, key=lambda student: student[1])

for student in data_list:
    print(student[0], end=' ')
