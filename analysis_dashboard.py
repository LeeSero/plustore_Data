# analysis_dashboard.py

import pandas as pd
import streamlit as st

# 📁 엑셀 파일 불러오기
df = pd.read_excel("네이버플로스스토어 유입 데이터 분석_250618-250701.xlsx", sheet_name="상품_검색채널")

# 🔍 채널명 필터링
filtered_df = df[df['채널명'].isin(['네이버플러스스토어-검색', '네이버플러스스토어-통합검색'])]

# 📌 Streamlit 대시보드 시작
st.title("🔎 네이버플러스스토어 유입 데이터 분석")

# ✅ 채널 선택 필터
channel = st.selectbox("📂 채널명을 선택하세요", filtered_df["채널명"].unique())

# ✅ 채널 기준으로 필터링
channel_df = filtered_df[filtered_df["채널명"] == channel]

# ✅ 상품카테고리(소) 선택 필터
category = st.selectbox("🧁 상품카테고리(소)를 선택하세요", channel_df["상품카테고리(소)"].unique())

# ✅ 선택된 카테고리에 해당하는 데이터 필터링
cat_df = channel_df[channel_df["상품카테고리(소)"] == category]

# 📊 표 형태 출력
st.subheader(f"📌 '{channel}' - '{category}' 카테고리 분석 결과")
st.dataframe(cat_df[["상품명", "키워드", "결제수(과거 14일간 기여도추정)", "결제금액(과거 14일간 기여도추정)"]])

