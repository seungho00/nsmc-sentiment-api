import streamlit as st
import requests


st.title("영화 리뷰 감성분석 AI")

sentence = st.text_area("영화 리뷰를 입력하세요.")

if st.button("분석"):
    response = requests.post(
        "http://nsmc-sentiment-backend:8000/predict",
        json={"sentence": sentence}
    )

    result = response.json()

    st.write("### 분석 결과")
    st.write(f"긍정: {result['positive']:.2%}")
    st.write(f"부정: {result['negative']:.2%}")