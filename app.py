import streamlit as st
import hashlib
from datetime import datetime

st.set_page_config(
    page_title="지능형 운세 및 행운 예측 시스템",
    page_icon="🔮",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #f8fafc;
    }
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.3);
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🔮 지능형 운세 및 행운 예측 시스템</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cbd5e1;'>사주 명리학과 통계적 추론을 통한 맞춤형 시험·연애·재물운 분석 리포트</p>", unsafe_allow_html=True)
st.write("---")

with st.form("fortune_form"):
    st.markdown("### 📝 사용자 정보 입력")
    user_name = st.text_input("이름 (성함)", placeholder="예: 홍길동")
    user_birth = st.date_input("생년월일", value=datetime(2000, 1, 1))
    
    submitted = st.form_submit_button("맞춤 운세 분석 리포트 생성하기", use_container_width=True)

if submitted:
    if not user_name.strip():
        st.warning("이름을 정확히 입력해주세요.")
    else:
        with st.spinner("우주의 기운과 사주 명리 데이터를 분석 중입니다..."):
            # Hash calculation for deterministic variability
            seed_str = user_name + str(user_birth)
            hash_val = int(hashlib.md5(seed_str.encode('utf-8')).hexdigest(), 16)
            abs_hash = abs(hash_val)

            lucky_num = (abs_hash % 5) + 1
            secondary_num = ((abs_hash + 2) % 5) + 1
            number_string = f"{lucky_num}번" if lucky_num == secondary_num else f"{lucky_num}번, {secondary_num}번"

            exam_analyses = [
                "집중력이 최고조에 달하는 시기입니다. 꾸준히 쌓아온 지식이 시험 당일에 명확하게 발현되며, 특히 어려운 문제에서 직관력이 빛을 발할 것입니다.",
                "학업적 기운이 상승곡선을 그리고 있습니다. 잡념을 비우고 핵심 요약에 집중한다면 노력 대비 매우 우수한 성과를 거둘 수 있습니다.",
                "시험 당일의 긴장감을 지혜롭게 다스릴 수 있는 기운이 감돌고 있습니다. 평소 실력을 온전히 발휘할 수 있는 최적의 컨디션이 유지됩니다."
            ]
            exam_advices = [
                "시험 전날 밤은 무리한 암기보다 가벼운 복습과 충분한 수면으로 뇌의 컨디션을 최상으로 유지하세요.",
                "모르는 문제가 나와도 당황하지 말고 아는 문제부터 빠르게 해결한 뒤 여유를 가지고 접근하세요.",
                "자신감을 가지고 오답 노트 위주로 최종 점검을 진행하면 합격률이 급상승합니다."
            ]

            love_analyses = [
                "주변의 시선을 사로잡는 매력 지수가 최고조에 달하는 시기입니다. 자연스러운 만남 속에서 따뜻한 인연의 기운이 다가옵니다.",
                "현재의 관계 또는 새로운 인연과의 소통이 매우 매끄럽게 풀리는 시기입니다. 진솔한 대화가 관계를 한 단계 더 깊게 만들어 줍니다.",
                "내면의 평온함이 매력으로 작용하여 상대방에게 깊은 신뢰와 호감을 줄 수 있는 시기입니다."
            ]
            love_advices = [
                "상대방의 작은 이야기에 귀 기울이고 공감해 주는 태도가 최고의 매력 포인트가 됩니다.",
                "표현에 인색해하지 말고 따뜻한 말한마디와 미소를 건네보세요. 관계가 급격히 가까워집니다.",
                "내 자신을 먼저 아끼고 사랑할 때 타인과의 관계도 자연스럽고 조화롭게 풀려나갑니다."
            ]

            wealth_analyses = [
                "금전 흐름이 안정세로 접어들며, 예기치 않은 작은 행운이나 보상이 따를 수 있는 길운이 들어와 있습니다.",
                "재물운의 흐름이 활발하여 계획적인 자산 관리가 빛을 발하는 시기입니다. 투자나 지출에 있어서 현명한 판단력이 돋보입니다.",
                "불필요한 지출이 줄어들고 시드머니가 차곡차곡 쌓이는 실속 있는 금전운을 보이고 있습니다."
            ]
            wealth_advices = [
                "충동구매를 자제하고 현재 보유한 자산의 흐름을 꼼꼼히 기록하는 습관을 들이세요.",
                "작은 금전적 여유가 생겼을 때 미래를 위한 투자나 자기 계발에 일부를 투자하면 배로 돌아옵니다.",
                "주변 사람들과의 소중한 나눔과 베풂이 더 큰 재물운을 불러오는 통로가 됩니다."
            ]

            colors = ["로얄 블루 / 동쪽", "에메랄드 그린 / 남쪽", "골드 옐로우 / 서쪽", "퍼플 바이올렛 / 북쪽", "크림 화이트 / 중앙"]

            st.markdown(f"""
            <div class="glass-card">
                <h2 style='color: #fbbf24; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;'>
                    🔮 {user_name} 님의 맞춤 운세 분석 리포트
                </h2>
                
                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #a78bfa;'>📚 1. 시험운 & 합격 기운</h3>
                    <p><b>운세 분석:</b> {exam_analyses[abs_hash % len(exam_analyses)]}</p>
                    <p><b>합격 조언:</b> {exam_advices[(abs_hash + 1) % len(exam_advices)]}</p>
                    <p style='background: rgba(139, 92, 246, 0.2); padding: 10px; border-radius: 8px;'>
                        🍀 <b>시험 추천 번호 (1~5):</b> {number_string} - 수리 오행상 학업과 집중력을 극대화해주는 행운의 번호입니다.
                    </p>
                </div>

                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #f472b6;'>💗 2. 연애운 & 인연의 흐름</h3>
                    <p><b>운세 분석:</b> {love_analyses[abs_hash % len(love_analyses)]}</p>
                    <p><b>연애 팁:</b> {love_advices[(abs_hash + 1) % len(love_advices)]}</p>
                </div>

                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #34d399;'>💰 3. 재물운 & 금전 흐름</h3>
                    <p><b>운세 분석:</b> {wealth_analyses[abs_hash % len(wealth_analyses)]}</p>
                    <p><b>재물 관리 팁:</b> {wealth_advices[(abs_hash + 1) % len(wealth_advices)]}</p>
                    <p style='background: rgba(16, 185, 129, 0.2); padding: 10px; border-radius: 8px;'>
                        ✨ <b>행운의 요소:</b> {colors[abs_hash % len(colors)]}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>© 2026 Intelligent Fortune & Luck Prediction System. Built with Streamlit.</p>", unsafe_allow_html=True)
