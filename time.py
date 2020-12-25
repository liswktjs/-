n = int(input())

count = 0 

for h in range(0,n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s): # 숫자 3이 십의자리나 일의 자리에 와도 되기 때문에 
                count = count + 1


print(count)
            
