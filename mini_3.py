'''
Q) 1부터 12까지를 for loop를 활용하여 출력하는 데, 8은 건너뛰고 출력하라
'''

for i in range(1,13):
    if(i == 8):continue
    print(i, end=' ')