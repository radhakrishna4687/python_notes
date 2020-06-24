def cal(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return sum,sub,mul,div
t=cal(199,4)
print('The result are: ')
for i in t:
    print(i)
