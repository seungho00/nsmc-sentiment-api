# nsmc-sentiment-api
기존 nsmc-sentiment-analysis 프로젝트를 FastAPI와 Docker를 이용해서 API 서비스로 확장하였다.

## 1. 프로젝트 소개

- 목적
  - AI 모델을 가지고 어떻게 서비스로 만드는지 학습한다.
  - API 통신을 이해한다.
  - docker 사용법을 익힌다. 

- AI 모델
  - 기존  nsmc-sentiment-analysis 프로젝트에서 만들고 학습시킨 bert 모델을 가져왔다.
  - 자세한 모델 구조는 기존 프로젝트 참고

- 참고 자료
  - ChatGPT (개념 학습, 코드 리뷰 및 개발 보조)

## 2. 개발 환경

- **OS**: macOS
- **의존성 패키지**: `requirements-backend.txt`, `requirements-frontend.txt` 참고

## 3. 프로젝트 구조
```
nsmc-sentiment-api
├── backend
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── predict.py                  # 전처리 및 추론
│   └── models                      # gitignore 설정
│       └── best_bert.pt            # 기존 프로젝트에서 BERT 학습 후 생성된 가중치 파일
├── docs
│   ├── development_log.md          # 개발 일지
│   └── project_design.md           # 프로젝트 설계
├── frontend
│   └── ui.py
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── README.md
├── requirements-backend.txt
└── requirements-frontend.txt
```

## 4. 동작 과정

사용자 <br>
↓ <br>
Streamlit 웹 UI (127.0.0.1:8501) <br>
↓ HTTP POST <br>
nsmc-sentiment-backend:8000/predict <br>
↓ <br>
FastAPI <br>
↓ <br>
전처리 → Tokenizer → BERT 모델 → 감성 결과 <br>
↓ HTTP <br>
Streamlit <br>
↓ <br>
긍정, 부정 확률 출력

- Docker Compose를 실행하면 Streamlit은 호스트의 127.0.0.1:8501을 통해 웹 브라우저에서 접속할 수 있다.
- Streamlit 컨테이너는 문장을 입력받은 후 Docker Compose 네트워크를 통해 nsmc-sentiment-backend:8000/predict로 HTTP POST 요청을 전송한다.
- FastAPI 컨테이너는 BERT 모델을 이용해 감성분석을 수행하고 결과를 Streamlit에 반환한다.

## 5. 실행 방법

- `backend/models/best_bert.pt`는 Git 저장소에 포함하지 않았습니다.
- 이 프로젝트를 실행하려면 먼저 `nsmc-sentiment-analysis` 프로젝트에서 BERT 모델을 학습해야 합니다.
- 학습이 완료되면 생성된 `best_bert.pt`를 `backend/models/`에 배치합니다.

```
cd nsmc-sentiment-api
docker compose up --build
```
- http://127.0.0.1:8501 에 브라우저로 접속하고 문장을 입력하면 된다.

- 서버 종료: **Ctrl + C**

## 6. 모델

- klue/bert-base
- NSMC 데이터셋을 학습시켰다.
- max_length: 62
- Test Accuracy: 0.9026
- F1-score: 0.9045
- 자세한 내용은 기존 NSMC-sentiment-analysis 프로젝트 참고