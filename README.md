# python_study

* Markdown 형태로보기: Cmd + Shift + V

## Python 환경 설정(/W VSCode)


* 1.파이썬 설치
* 2.가상환경 생성: python -m vent .venv
* 3.활성화: source .venv/bin/activate
* 4.VS Code에서 Python 인터프리터를 선택
```
  -Cmd + Shift + P
  -Python: Select Interpreter (선택)
  -.venv/bin/python(선택)
```
 
* 5.패키지는 가상환경 안에서 설치
 -pip install requests
* 6.현재 프로젝트 패키지를 저장
 -pip freeze > requirements.txt
* 7.다른 환경에서 다시 설치할 때
 -pip install -r requirements.txt
* 8..VS Code 설정에서 자동으로 .venv를 사용하게 하고 싶다면 .vscode/settings.json
```
{ 
"python.terminal.activateEnvironment": true 
}
```

## TEST1

### TEST2
