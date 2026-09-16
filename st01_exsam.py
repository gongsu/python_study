agent_name = "research-agent"
request_count = 7
success_count = 5

result = success_count/request_count*100

print(f"Success rate: {result}%")

if result >= 90:    
    print("excellent")
elif result >= 70:
    print("good")
else:
    print("needs improvement")