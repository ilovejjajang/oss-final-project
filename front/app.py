import streamlit as st
import requests
import time

st.set_page_config(page_title="소비 성향 기반 게임 추천기", page_icon="🎮", layout="centered")

st.markdown("### 20222204043 채민성")
st.divider()

st.title("🎮 맞춤형 게임 타겟 추천기")
st.write("소비 성향과 취향을 입력하면 적합한 게임을 추천해 드립니다.")

with st.sidebar:
    st.header("👤 내 프로필")
    st.write("**이름:** 채민성")
    st.write("**학번:** 20222204043")
    st.write("**상태:** 정상 연결됨 🟢")

with st.form("recommend_form"):
    st.subheader("소비 성향 선택")
    
    spend_reason = st.selectbox(
        "1. 주된 지출 목적이 무엇인가요?",
        ["캐릭터 외모 (디자인 및 일러스트)", "성능 및 스펙업 (경쟁과 성취감)", "스토리 및 세계관 (몰입감)"]
    )
    
    worldview = st.selectbox(
        "2. 선호하는 세계관은?",
        ["판타지", "현대물 및 SF"]
    )
    
    budget = st.radio(
        "3. 한 달 게임 예산은?",
        ["10만원 미만", "10만원 이상"]
    )
    
    submit_btn = st.form_submit_button("추천 받기")

if submit_btn:
    print(">> [로그] 추천 버튼 클릭됨")
    
    with st.spinner("결과 분석 중..."):
        time.sleep(1.0)
        
        API_URL = "http://backend:8000/recommend"
        
        payload = {
            "spend_reason": spend_reason,
            "worldview": worldview,
            "budget": budget
        }
        
        try:
            # API 호출
            response = requests.post(API_URL, json=payload)
            
            # 성공 시 화면 출력
            if response.status_code == 200:
                result = response.json()
                st.success("추천 완료!")
                
                st.markdown("### 💡 추천 결과")
                st.info(f"**추천 타겟:** {result['recommended_target']}")
                st.write(f"**추천 사유:** {result['reason']}")
                st.balloons()
            else:
                st.error("서버 응답 오류")
                
        except Exception as e:
            st.error(f"서버 통신 실패: {e}")