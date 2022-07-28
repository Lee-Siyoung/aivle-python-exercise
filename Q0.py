'''
### Q0

### 두 정수의 최대공약수를 구하라. 최대공약수는 두 정수를 나머지가 0이 되게 나누는 공통된 약수 중 최대값을 가진 수이다. 

### 예
- 12, 16의 최대공약수 4
- 2, 4의 최대공약수 2

### tips
- if 문에 조건이 두 개인 경우는 and 또는 or 논리연산자 사용

### 제한사항 
- 두 정수는 서로 다른 수이다.
'''

# Q0 Answer template

def solution(a, b):
    answer = 0
    if a>b:
        a, b = b, a
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            answer=i
    return answer

a=int(input("a : "))
b=int(input("b : "))
c = solution(a,b)
print(c)