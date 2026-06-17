import streamlit as st
import requests
import time

st.set_page_config(page_title="소비 성향 기반 게임 추천기", page_icon="🎮", layout="centered")

st.markdown("### 20222204043 채민성")
st.divider()

st.title("🎮 맞춤형 게임 및 덕질 타겟 추천기")
st.write("평소 소비 성향과 선호하는 스타일을 입력하시면 가장 적합한 게임을 추천해 드립니다.")

with st.sidebar:
    st.header("👤 내 프로필")
    st.write("**이름:** 채민성")
    st.write("**학번:** 20222204043")
    st.write("**상태:** 서비스 정상 연결됨 🟢")

with st.form("recommend_form"):
    st.subheader("소비 성향 및 취향 선택")
    
    spend_reason = st.selectbox(
        "1. 주로 어떤 목적이나 이유로 비용을 지출하시나요?",
        ["캐릭터 외모 (디자인 및 일러스트)", "성능 및 스펙업 (경쟁과 성취감)", "스토리 및 세계관 (몰입감)"]
    )
    
    worldview = st.selectbox(
        "2. 선호하는 게임의 세계관을 선택해 주세요.",
        ["판타지", "현대물 및 SF"]
    )
    
    budget = st.radio(
        "3. 한 달 동안 사용할 수 있는 가용 예산 범위는 어떻게 되나요?",
        ["10만원 미만", "10만원 이상"]
    )
    
    submit_btn = st.form_submit_button("추천 결과 확인하기")

if submit_btn:
    print(">> [클라이언트 로그] 사용자가 추천 요청 버튼을 클릭했습니다.")
    
    with st.spinner("사용자의 취향 분석 결과를 백엔드 서버로부터 조회 중입니다..."):
        time.sleep(1.0)
        
        API_URL = "http://backend:8000/recommend"
        
        payload = {
            "spend_reason": spend_reason,
            "worldview": worldview,
            "budget": budget
        }
        
        try:
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                st.success("취향 분석 및 추천이 완료되었습니다.")
                
                st.markdown("### 💡 추천 결과 안내")
                st.info(f"**추천 타겟:** {result['recommended_target']}")
                st.write(f"**추천 사유:** {result['reason']}")
                st.balloons() 
            else:
                st.error("백엔드 서버 응답 오류가 발생했습니다.")
                
        except Exception as e:
            st.error(f"백엔드 서버와 통신할 수 없습니다. 에러 메시지: {e}")