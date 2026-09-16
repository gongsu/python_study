# 오늘의 Key Point: 
# Python의 기본 타입과 f-string 사용법을 이해하자
# Python에는 {}가 없습니다.
# 대신 들여쓰기가 문법
# if / elif / else 구문 
# for, range 사용법
# Python에서는 ++가 없다: i += 1




value = 10

print(value)
print(type(value))

value = "python"
print(value)
print(type(value)) # 타입확인 방법 type


# python 기본 타입 
name = "Alice"       # str
age = 30             # int
temperature = 0.7    # float
enabled = True       # bool(주의: 대문자 True/False 사용)

# 문자열 안에 값을 넣고 싶다면 가장 자주 사용하는 것이 f-string
message = f"My name is {name} and I am {age} years old."
print(message)

# 숫자 타입과 f-string 예제
price = 100
quantity = 3

print(f"total = {price * quantity}")




# 연습
model = "my-agent"
requests = 10
success = 8
print(f"{model}: {success}/{requests} requests succeeded")

#block 예제
score = 90

if score >= 80:
    print("pass")
    print("good")

print("done")


# if / elif / else 구문 예제
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

token_count = 100

if token_count >= 10000:
    print("large")
elif token_count >= 1000:
    print("medium")
else:
    print("small")

#Python은 앞으로도 계속 "컬렉션이나 iterable에서 값을 하나씩 꺼낸다"는 방식으로 코드를 작성
#0~4까지 반복
for i in range(5):
    print(i)

# 2~4까지 반복
for i in range(2, 5):
    print(i)

# step 2씩 증가하며 반복(10은 포함되지 않음, 0,2,4,6,8)
for i in range(0, 10, 2):
    print(i)

for i in range(1, 6):
    print(f"request-{i}")