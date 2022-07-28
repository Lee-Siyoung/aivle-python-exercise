'''
Q) 사용자에게 정수를 입력받아, root ** pwr 값이 사용자가 입력 한 정수와 같은 두 개
의 정수 root 및 pwr을 찾아 출력하라 (단, 1 < pwr < 6 ). 그러한 정수 쌍이 없으면 결과
가 없음을 출력하라.
(root ** pwr은 root를 pwr 만큼 거듭제곱하였다는 뜻이다. 예를 들어 2**3 은 2의 세 제
곱이며 값은 8이다.)
'''

a = int(input("정수 입력 : "))
con=0
for i in range(1, a+1):
    for j in range (2, 6):
        if i**j==a:
            print(i ,j)
            con+=1
if con==0:
    print("결과없음")
 