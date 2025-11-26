import streamlit as st
import time

# --- 1. 선생님의 설정 (페이지 디자인) ---
st.set_page_config(page_title="맥도날드 주문 연습", page_icon="🍔")

# 버튼을 크고 예쁘게 만드는 마법의 주문 (CSS)
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 150px;
        font-size: 40px !important;
        font-weight: bold;
        border-radius: 20px;
        background-color: #FFC72C; /* 맥도날드 노란색 */
        color: #DA291C; /* 맥도날드 빨간색 */
        border: 2px solid #DA291C;
    }
    .stButton>button:hover {
        background-color: #ffdb75;
        border: 4px solid #DA291C;
    }
    h1 { text-align: center; color: #DA291C; }
    h2 { text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 2. 주문 단계 관리 (상태 저장) ---
if 'step' not in st.session_state:
    st.session_state.step = 1  # 1:시작, 2:메뉴선택, 3:세트선택, 4:결제, 5:완료

def go_next():
    st.session_state.step += 1
    st.rerun()

def restart():
    st.session_state.step = 1
    st.rerun()

# --- 3. 화면 구성 ---

# [1단계] 시작 화면
if st.session_state.step == 1:
    st.title("🍔 맥도날드 연습하기")
    st.markdown("## 화면을 눌러주세요")
    
    # 여백을 줘서 버튼을 중앙에
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("주문 시작하기 👇"):
            go_next()

# [2단계] 메뉴 선택 (불고기버거 찾기)
elif st.session_state.step == 2:
    st.title("메뉴를 골라보아요")
    st.markdown("## '불고기 버거'는 어디 있을까요?")

    col1, col2 = st.columns(2)
    
    with col1:
        # 다른 메뉴 (오답)
        if st.button("🍦 아이스크림"):
            st.toast("어라? 우리는 햄버거를 먹을 거예요! 다시 찾아볼까요?", icon="🤔")
            
        # 정답 메뉴
        if st.button("🍔 불고기버거"):
            st.balloons() # 칭찬 효과!
            time.sleep(1)
            go_next()
            
    with col2:
        # 다른 메뉴 (오답)
        if st.button("🍟 감자튀김"):
            st.toast("감자튀김은 나중에 시킬 거예요. 햄버거를 먼저 골라주세요!", icon="😉")
        
        # 다른 메뉴 (오답)
        if st.button("🥤 콜라"):
            st.toast("음료수는 나중에 시킬 거예요. 햄버거를 먼저 골라주세요!", icon="😉")

# [3단계] 세트 vs 단품 선택
elif st.session_state.step == 3:
    st.title("어떻게 먹을까요?")
    st.markdown("## 감자튀김과 콜라가 있는 '세트'를 눌러주세요!")

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🍔 햄버거만\n(단품)"):
            st.warning("오늘은 감자튀김도 같이 먹고 싶어요. '세트'를 눌러볼까요?")
            
    with col2:
        if st.button("🍟🥤 세트 메뉴\n(추천)"):
            st.success("참 잘했어요! 맛있는 세트를 골랐네요!")
            time.sleep(1)
            go_next()

# [4단계] 결제 하기
elif st.session_state.step == 4:
    st.title("계산해 주세요")
    st.markdown("## 카드를 꽂아주세요")
    
    # 카드 그림 대신 이모지 활용 (실제 이미지로 교체 가능)
    st.markdown("<div style='text-align: center; font-size: 100px;'>💳 ➡️ 🏧</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("카드 넣기"):
            with st.spinner("결제 중입니다..."):
                time.sleep(2) # 결제하는 척 기다리기
            go_next()

# [5단계] 주문 완료
elif st.session_state.step == 5:
    st.title("주문 성공! 🎉")
    st.markdown("## 맛있는 불고기버거 세트가 나옵니다.")
    st.balloons()
    
    st.image("https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60", caption="맛있게 드세요!")
    
    if st.button("처음부터 다시 하기 🔄"):
        restart()
