'''
### Q) 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하여라.
'''

import math
x=[True for i in range(1001)]

for i in range(2,int(math.sqrt(1000)+1)):
    if x[i]==True:   
        j=2
        while i * j <=1000:
            x[i*j]=False
            j+=1

for i in range(2,1001):
    if x[i]:
        print(i, end=" ")