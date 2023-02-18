# 오븐시계
A, B = map(int, input().split())
C = int(input())


hour = (B+C) // 60 # 1 2
min = (B+C) % 60 # 13 0

if A+hour > 23: # 23+1 = 24, 17+2 = 19
    print((A+hour) - 24, min) # 24-24 = 0, 13
else:
    print(A+hour, min) # 19, 0
    


