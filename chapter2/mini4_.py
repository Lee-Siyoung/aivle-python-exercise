'''
### Q) 리스트를 사용자로부터 입력받아서 최대값과 최대값이 있는 인덱스를 출력하라.
'''

def max_d(x):
    maxs=x[0]
    for i in range(1,len(x)):
        if maxs<x[i]:
            maxs=x[i]
    return maxs

def binary_se(x, key):
    pl=0
    pr=len(x)-1
    while True:
        pc=(pl+pr)//2
        if x[pc]==key:
            return pc
        elif x[pc]<key:
            pl=pc+1
        elif x[pc]>key:
            pr=pc-1
        if pl>pr:
            break
    return -1


x=[]
while True:
    a=input("리스트 입력 : ")
    if a=='end':
        break
    x.append(int(a))

inx = binary_se(x,max_d(x))
#inx = binary_se(x,max(x))
print(f"위치는{inx}")

# max 함수 써도 되고