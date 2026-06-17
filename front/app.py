import streamlit as st
import requests
import time

# 웹페이지 브라우저 탭 및 레이아웃 설정
st.set_page_config(page_title="소비 성향 기반 게임 추천기", page_icon="🎮", layout="centered")

# 과제 제출자 정보 표시 (이전 실습 스타일 반영)
st.markdown("### 20222204043 채민성")
st.divider()

st.title("🎮 맞춤형 게임 및 덕질 타겟 추천기")
st.write("평소 소비 성향과 선호하는 스타일을 입력하시면 가장 적합한 게임을 추천해 드립니다.")

# 좌측 사이드바 프로필 영역 구성
with st.sidebar:
    st.header("👤 내 프로필")
    st.write("**이름:** 채민성")
    st.write("**학번:** 20222204043")
    st.write("**상태:** 서비스 정상 연결됨 🟢")

# 사용자 입력을 받기 위한 스트림릿 폼 구성
with st.form("recommend_form"):
    st.subheader("소비 성향 및 취향 선택")
    
    # 평가 기준인 개인별 차별성을 위한 맞춤형 문항 설정
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
    
    # 폼 제출 버튼
    submit_btn = st.form_submit_button("추천 결과 확인하기")

# 버튼 클릭 시 백엔드 API와 통신하는 로직
if submit_btn:
    print(">> [클라이언트 로그] 사용자가 추천 요청 버튼을 클릭했습니다.")
    
    # 데이터 처리 중임을 시각적으로 보여주는 로딩 효과 적용
    with st.spinner("사용자의 취향 분석 결과를 백엔드 서버로부터 조회 중입니다..."):
        time.sleep(1.0)
        
        # Docker Compose 환경에서 백엔드 서비스의 이름(backend)을 도메인으로 사용합니다.
        API_URL = "http://backend:8000/recommend"
        
        # 백엔드로 보낼 요청 데이터 구성
        payload = {
            "spend_reason": spend_reason,
            "worldview": worldview,
            "budget": budget
        }
        
        try:
            # FastAPI 백엔드 서버로 POST 요청 전송
            response = requests.post(API_URL, json=payload)
            
            # 정상적으로 응답을 받은 경우 결과 출력
            if response.status_code == 200:
                result = response.json()
                st.success("취향 분석 및 추천이 완료되었습니다.")
                
                st.markdown("### 💡 추천 결과 안내")
                st.info(f"**추천 타겟:** {result['recommended_target']}")
                st.write(f"**추천 사유:** {result['reason']}")
                st.balloons()  # 결과 출력 시 시각 효과 부여
            else:
                st.error("백엔드 서버 응답 오류가 발생했습니다.")
                
        except Exception as e:
            st.error(f"백엔드 서버와 통신할 수 없습니다. 에러 메시지: {e}")