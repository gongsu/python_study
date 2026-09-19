# 1. Python의 기본 자료형( Python은 동적 타이핑(dynamic typing) 언어 )
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

value = 10
print(type(value))
value = "10"
print(type(value))
print(value * 3) # 주의: 문자열 "10"이 3번 반복되어 출력됨 (즉, "101010")


#2. 컬렉션: list / tuple / dict / set
# Python	Java에서 비슷한 것
#-------------------------
# list	ArrayList
# tuple	불변 데이터 묶음
# dict	HashMap
# set	HashSet

## list 예제
models = ["gpt-5", "claude", "gemini"]

print(models[0])
print(models[-1]) #-1은 마지막 요소입니다.

models.append("llama")

print(models)
for model in models:
    print(f"모델 이름: {model}")
    
## dict 예제 ( Java의 Map<String, Object>와 비슷 ) 
model_info = {
    "name": "gpt-5",
    "developer": "OpenAI",
    "release_year": 2024
}

print(model_info["name"])
print(model_info.get("developer"))

print("---------------------")
for key, value in model_info.items():
    print(f"{key}: {value}")

print("---------------------")
model_info["enabled"] = True

for key, value in model_info.items():
    print(f"{key}: {value}")
print("---------------------")