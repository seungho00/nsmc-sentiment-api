# 프로젝트 설계

## 프로젝트 목표
1. 기존 NSMC 감성분석 프로젝트를 실제 서비스 형태로 확장
2. 학습된 모델을 API로 제공
3. Streamlit으로 웹 UI 구현
4. Docker로 실행 환경 통일
5. 모델 오류 분석

## 전체 구조
사용자 <br>
↓ <br>
Streamlit <br>
↓ HTTP <br>
FastAPI <br>
↓ <br>
전처리 → Tokenizer → BERT 모델 → 감성 결과 <br>
↓ HTTP <br>
Streamlit <br>
↓ <br>
화면 출력

## 디렉토리 구조
```
nsmc-sentiment-api
├── app
│   ├── main.py
│   ├── config.py
│   ├── inference.py                # 전처리 및 추론
│   └── ui.py
├── docs
│   ├── project_design.md           # 프로젝트 설계
│   └── todo.md
├── models                          # gitignore 설정
│   └── best_bert.pt
├── .gitignore
├── README.md
└── requirements.txt
```

## 세부 모듈 구조
### 추론 모델
- 기존 프로젝트의 BERT 모델을 그대로 사용
- 기존의 방식대로 62를 max_length로 지정
```
입력 문장
↓
BERT Tokenizer
↓
Tensor 변환
↓
BERT 모델
↓
logits
↓
Softmax
↓
긍정/부정 확률
```

### API
- FastAPI 사용
- 서버 주소: 127.0.0.1:8000
- `/predict` endpoint를 통해 문장 입력 및 감성분석 결과 반환

### UI
- 간단하게
- 문장 입력하면 긍정과 부정의 비율을 보여줌