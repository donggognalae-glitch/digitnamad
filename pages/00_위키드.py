import streamlit as st

# --- 1. 페이지 설정 및 디자인 ---
st.set_page_config(
    page_title="위키드 MBTI 분석",
    page_icon="🧙‍♀️",
    layout="wide"
)

# 위키드 테마 CSS (폰트, 컬러 등)
st.markdown("""
<style>
    /* 전체 배경 톤 */
    .stApp {
        background: linear-gradient(to right, #1a2e1a, #2e1a26);
    }
    /* 제목 스타일 */
    h1 {
        text-align: center;
        color: #fff;
        text-shadow: 2px 2px 4px #000000;
    }
    /* 카드 스타일 */
    .char-card {
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. 캐릭터 데이터 (MBTI 분석 내용) ---
characters = {
    "Elphaba": {
        "mbti": "INTJ (용의주도한 전략가)",
        "desc": "남들의 시선보다 자신의 신념이 중요합니다. 독립적이고 통찰력이 뛰어나며, 세상을 바꾸려는 혁명가 기질이 있습니다.",
        "color": "#5F8836", # 엘파바 그린
        "icon": "🧹",
        "quote": "난 이제 중력을 거슬러 날아오를 거야!"
    },
    "Glinda": {
        "mbti": "ESFJ (사교적인 외교관)",
        "desc": "사람들에게 사랑받는 것을 좋아하고, 조화와 규칙을 중시합니다. 분위기 메이커이며, 타인을 돕는 것에서 기쁨을 느낍니다.",
        "color": "#F2A2BA", # 글린다 핑크
        "icon": "👑",
        "quote": "누구나 사랑받을 자격이 있어."
    },
    "Fiyero": {
        "mbti": "ESFP (자유로운 영혼의 연예인)",
        "desc": "인생은 즐기는 것이라 생각합니다. 겉으로는 가벼워 보이지만, 진정으로 마음이 움직이면 모든 것을 던지는 열정이 있습니다.",
        "color": "#D4AF37", # 골드
        "icon": "🕺",
        "quote": "인생은 춤추듯 사는 거야."
    },
    "The Wizard": {
        "mbti": "ENFJ (언변능숙한 선도자 - 불건강)",
        "desc": "카리스마로 대중을 휘어잡지만, 실체보다는 보여지는 이미지를 중요시합니다. 사람들의 마음을 읽고 조종하는 데 능숙합니다.",
        "color": "#4A4A4A", # 그레이
        "icon": "🎭",
        "quote": "사람들은 믿고 싶은 걸 믿는 법이지."
    }
}

# --- 3. 메인 화면 구성 ---
st.title("🧙‍♀️ WICKED : 캐릭터 MBTI 분석")
st.markdown("##### 당신의 성격은 엘파바인가요, 글린다인가요?")

# 탭 메뉴 생성
tab1, tab2 = st.tabs(["📊 캐릭터 분석 보기", "🔮 나랑 닮은 캐릭터 찾기"])

# [탭 1] 캐릭터 분석
with tab1:
    st.write("")
    # 2열로 배치
    cols = st.columns(2)
    
    # 딕셔너리에서 데이터를 하나씩 꺼내서 카드 만들기
    for i, (name, info) in enumerate(characters.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="char-card" style="background-color: {info['color']}; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                <h1>{info['icon']}</h1>
                <h2>{name}</h2>
                <h4>{info['mbti']}</h4>
                <p><i>"{info['quote']}"</i></p>
                <hr style="border-top: 1px dashed white;">
                <p style="font-size:16px;">{info['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# [탭 2] 간단 심리 테스트
with tab2:
    st.header("나와 닮은 위키드 캐릭터는?")
    
    with st.form("quiz_form"):
        q1 = st.radio("주말에 파티가 열린다면?", ["당연히 가야지! 내가 주인공인데 (외향)", "집에서 조용히 책 읽는 게 더 좋아 (내향)"])
        q2 = st.radio("중요한 결정을 내릴 때 나는?", ["논리와 사실, 원칙이 중요해 (이성)", "사람들의 감정과 관계가 중요해 (감성)"])
        
        submitted = st.form_submit_button("결과 확인하기 ✨")
        
        if submitted:
            # 간단한 로직 (재미용)
            is_extrovert = "당연히" in q1
            is_thinking = "논리" in q2
            
            result_char = ""
            if not is_extrovert and is_thinking:
                result_char = "Elphaba" # I + T -> INTJ
            elif is_extrovert and not is_thinking:
                result_char = "Glinda" # E + F -> ESFJ
            elif is_extrovert and is_thinking:
                 result_char = "The Wizard" # E + T -> 대중을 조종하는 마법사
            else:
                result_char = "Fiyero" # I + F -> (피에로는 E지만 자유로운 영혼 느낌으로 매칭)
            
            info = characters[result_char]
            
            st.divider()
            st.subheader(f"당신의 위키드 소울메이트는... {result_char}! {info['icon']}")
            st.caption(f"MBTI 유형: {info['mbti']}")
            
            # 결과 카드 보여주기
            st.markdown(f"""
            <div style="background-color: {info['color']}; padding: 20px; border-radius: 10px; color: white; text-align: center;">
                <h3>{info['quote']}</h3>
                <p>{info['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if result_char == "Elphaba":
                st.snow()
            elif result_char == "Glinda":
                st.balloons()
