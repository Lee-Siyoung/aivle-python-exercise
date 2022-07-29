'''
### Q) 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는 인덱스를 출력하라.
### 검색방안은 어떤 방안을 사용하여도 됩니다.
'''

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
key = int(input("검색할 값: "))

inx = binary_se(x,key)
print(f"위치는{inx}")