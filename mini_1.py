'''
Q) 다음과 같이 계산되는 전기 요금 산출 함수 electricPay( )를 만들고, 전기사용량
(kWh)을 인수로 전해주면 전기 요금(원)을 계산하여 return해 준다.

--------------------------------------------------------------------
기본요금                                 전력량 요금
100kWh미만 사용             : 410        처음 100kwh까지  : 60.7
100kWh이상 200kWh이하 사용  : 910        다음 100kWh까지  : 125.9     
200kWh초과 사용             : 1600       200kWh초과 부분  : 187.9     
---------------------------------------------------------------------

예를 들어 한달 전기 사용량이 250kWh일 경우, 기본요금 1600원에
전력량 요금이 100kWh x 60.7원 + 100kWh x 125.9원 + 50kWh x 187.9원 = 28,055원이어서
합산하면29,655원이다.
이 요금합계에 부가가치세 10% (29,655원 x 0.1 = 2965.5원)와 전력산업기반기금 3.7% (29,
655원 x 0.037 = 1097.235원)을 더하면 총 전기요금은 29,655원 + 2965.5원 + 1097.235원
= 33717원 (1원미만절사) 이다.
(실수값을 가진 변수를 int 를 활용하여 정수로 변경하면 소수점 값들은 버려진다.)
'''

def electricPay(a):
    money=0
    if a<100:
        money = 410 + a*60.7
    elif a<=200:
        money = 910 + 100*60.7 + (a-100)*125.9
    else:
        money = 1600 + 100*60.7 + 100*125.9 + (a-200)*187.9
    return money

a = int(input("전기사용량 : "))
ele = electricPay(a)
print(f'요금 합계 : {int(ele)}')
ele = ele + (ele*0.1)+(ele*0.037)
print(f'요금 합계 : {int(ele)}')