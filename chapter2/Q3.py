'''
### Q3 (programmers)

### 컴퓨터 매장에는 n개의 부품이 있으며, 부품마다 정수 형태의 고유한 번호가 있다. 어느 날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 부품의 재고유무를 문의하였다. 매장에 부품 재고가 있는지 확인하는 프로그램을 작성하라. 

### 매장이 가지고 있는 부품 리스트와 고객이 확인하고자 하는 부품 리스트를 입력받는다. 고객이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력한다. 

### 제한사항
- 부품 재고의 갯수는 고려하지 않으며 부품이 있는지 여부만 체크한다
- 부품 리스트 길이(n, m)는 1이상, 15이하입니다.
- 매장 보유 부품 번호는 오름차순으로 정렬된 형태로 입력한다.
- 부품 리스트의 원소는 100 이하인 자연수입니다.


### 입출력 예
|store | customer | answer
|------|----------|-------
|[2,3,7,8,9]|[7,5,9]|['yes', 'no', 'yes']
|[1,2,3,7,8]|[1,5,8,4,6]|['yes', 'no', 'yes', 'no', 'no']

'''

# Q3 answer template

def solution(store, customer):
    answer = []
    for i in customer:
        if i in store:
            answer.append('yes')
        else:
            answer.append('no')
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)