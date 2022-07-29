'''
### Q1

### 두 정수의 최소공배수를 구하라. 최소공배수는 두 정수의 배수인 수 중 최솟값을 가진 값을 수이다.

### 예
- 12, 16의 최소공배수 48
- 2, 4의 최소공배수 4

### tips
- if 문에 조건이 두 개인 경우는 and 또는 or 논리연산자 사용


### 제한사항 
- 두 정수는 서로 다른 수이다.
'''
# Q1 Answer template

def solution(a, b):
    answer = 1
    if a>b:
        a, b = b, a
    for i in range(b, a*b+1):
        if i%a==0 and i%b==0:
            answer=i
            break
    return answer

a=int(input("a : "))
b=int(input("b : "))
c = solution(a,b)
print(c)