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

## 2026-08-21
(docker 이미지 생성)
- 기존 `pip freeze` 명령어로 생성한 `requirements.txt`로 이미지를 만들었더니 이미지 용량이 너무 커져버렸다.
- `pipreqs`로 해당하는 소스코드가 실제로 사용하는 패키지들만 추려낼 수 있었다. 항상 정확한 것은 아니다. 실행 명령에서 사용하는 패키지인 uvicorn은 추가가 안 되어서 직접 추가했다.
- 호스트에서 docker 컨테이너의 서비스를 접근할 수 있게 하기 위해 포트를 연결하는 과정이 필요하다. 따라서 아래와 같이 옵션을 추가해야한다.
```
docker run -p 8000:8000 <이미지 이름>
```
- backend와 frontend 각 이미지는 독립적으로 실행할 수 있지만, 두 컨테이너가 서로 통신하려면 같은 네트워크를 구성해야 한다. compose는 이 과정을 자동화해주는 도구이다.
- docker 컨테이너로 실행 시 127.0.0.1는 컨테이너를 가르킨다. 따라서 ui.py에서 기존에 `http://127.0.0.1:8000/predict`로 통신을 보내는 부분을 `http://nsmc-sentiment-backend:8000/predict`로 수정했다. compose로 실행하기 때문에 가능한 부분이다.
- 컨테이너 내부의 파일 구조를 고려해야 한다. Dockerfile에서 `COPY backend/. .`을 사용했더니 **main.py**의 `from backend.predict` 부분에서 에러가 발생했다. 로컬 개발 환경과의 구조를 동일하게 하기 위해서 `COPY backend ./backend`로 수정했다.
- `COPY backend .`과 `COPY backend/. .`의 역할은 같다.

## 2026-08-22
(README.md 작성, 최종 검수)
- `requirements-backend.txt`에서 `app==0.0.1` 항목이 있었다. 이는 이전에 `backend` 폴더명을 `app`이었을 때, pipreqs가 내부 로컬 패키지를 pip로 설치한 패키지라고 잘못 파익해서 생긴 항목이었다. *Package 'app' is not installed in the selected environment.* 라고 VSCODE에서 경고 메시지를 보여줘서 발견할 수 있었다.