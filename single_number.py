def check(n):
    ans=0
    for num in n:
        ans = ans^num
    return ans
n = list(map(int,input("Enter the values : ").split()))
print(check(n))