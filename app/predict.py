import torch
from transformers import (
    AutoTokenizer,
    BertForSequenceClassification,
)

from config import (
    TOKENIZER,
    MAX_LENGTH,
    MODELS_DIR,
)


## 모델 호출 ##

# 토크나이저 불러오기
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)

# 장치 설정
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(f'using device: {device}')

# 모델 생성
model = BertForSequenceClassification.from_pretrained(
    "klue/bert-base",
    num_labels=2
).to(device)

# 가중치 불러오기
model.load_state_dict(
    torch.load(MODELS_DIR, map_location=device)
)


## 토큰화 ##

def tokenize(sentence):
    encoding = tokenizer(
        sentence,
        padding="max_length",
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt"
    )

    return encoding


## 추론 ##

def predict(encoding):

    # 추론 진행
    model.eval()

    with torch.no_grad():
        input_ids = encoding["input_ids"].to(device)
        attention_mask = encoding["attention_mask"].to(device)

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )

        results = torch.softmax(
            input=outputs.logits,
            dim=1
        )

        negative = results[0][0].item()
        positive = results[0][1].item()

    return negative, positive


if __name__ == "__main__":
    sentence = input("영화평: ")
    encoding = tokenize(sentence)
    negative, positive = predict(encoding)
    print(f'부정 : {negative}\n긍정 : {positive}')
