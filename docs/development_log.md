# Development Log

## 2026-08-18
(프로젝트 설계, 추론 코드 구현)

## 2026-08-20
(api 구현, ui 구현)
- Streamlit은 HTML/CSS/JavaScript를 Python 문법으로 감싸 놓은 라이브러리라기보다는, Python 코드로 웹 애플리케이션의 UI를 만들고 실행할 수 있게 해주는 프레임워크였다.
- api용 서버와 ui용 서버 2개를 구동시켜야 한다.
- 터미널 창을 2개 띄워놓고 아래의 명령어를 각각 입력하면 된다.
```
uvicorn app.main:app
streamlit run app/ui.py
```