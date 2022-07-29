'''
### Q6 (https://programmers.co.kr/learn/courses/30/lessons/12935)

### 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

### 제한 조건
- arr은 길이 1 이상인 배열입니다.
- 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

### 입출력 예
|arr |return
|----|----
|[4,3,2,1] |[4,3,2]
|[10] |[-1]


### 리스트에서 원소 제거 함수
- a.pop(0) : 0번 인덱스의 원소가 제거됨
- a.remove(10) : 10 값을 가진 원소가 제거됨, 10이라는 값이 여러개라면 맨 처음에 있는 것만 제거됨
'''

# Q6 Answer template

def solution(arr):
    mins=arr[0]
    check=0
    for i in range(len(arr)):
        if mins>arr[i]:
            mins=arr[i]
            check=i
            print(mins, check)
    del arr[check]
    if not arr:
        return [-1]
        
    return arr