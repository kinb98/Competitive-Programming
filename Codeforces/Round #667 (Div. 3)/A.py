t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a == b:
        print(0)
    else:
        if a > b:
            a,b = b,a 
        temp = b-a 
        if temp%10 == 0:
            print(temp//10)
        else:
            print(temp//10 + 1)