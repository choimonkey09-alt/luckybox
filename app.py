import streamlit as st
import hashlib
from datetime import datetime
import textwrap

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
    .custom-box {
        background: rgba(30, 41, 59, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 1.5rem;
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
            seed_str = f"{user_name.strip()}_{user_birth}"
            hash_val = int(hashlib.md5(seed_str.encode('utf-8')).hexdigest(), 16)
            abs_hash = abs(hash_val)

            # Expanded lists for diverse and unique combinations per user
            exam_analyses = [
                "집중력이 최고조에 달하는 시기입니다. 꾸준히 쌓아온 지식이 시험 당일에 명확하게 발현되며, 특히 어려운 문제에서 직관력이 빛을 발할 것입니다.",
                "학업적 기운이 상승곡선을 그리고 있습니다. 잡념을 비우고 핵심 요약에 집중한다면 노력 대비 매우 우수한 성과를 거둘 수 있습니다.",
                "시험 당일의 긴장감을 지혜롭게 다스릴 수 있는 기운이 감돌고 있습니다. 평소 실력을 온전히 발휘할 수 있는 최적의 컨디션이 유지됩니다.",
                "새로운 유형의 문제에서도 당황하지 않고 유연하게 대처할 수 있는 통찰력이 열리는 대길의 운기입니다.",
                "노력한 시간만큼 정직한 결과가 따라오는 시기입니다. 막바지 총정리가 합격의 당락을 결정짓는 결정적 열쇠가 됩니다.",
                "평소 놓치기 쉬운 세부적인 디테일이 합격을 판가름하는 열쇠가 됩니다. 꼼꼼한 최종 검토가 대성공을 이끕니다."
            ]
            exam_advices = [
                "시험 전날 밤은 무리한 암기보다 가벼운 복습과 충분한 수면으로 뇌의 컨디션을 최상으로 유지하세요.",
                "모르는 문제가 나와도 당황하지 말고 아는 문제부터 빠르게 해결한 뒤 여유를 가지고 접근하세요.",
                "자신감을 가지고 오답 노트 위주로 최종 점검을 진행하면 합격률이 급상승합니다.",
                "시험 시작 30분 전 심호흡을 깊게 하며 마인드 컨트롤을 하는 것이 실력 발휘에 큰 도움이 됩니다.",
                "평소 취약했던 개념을 가볍게 훑어보는 것이 예상 외의 점수 상승을 이끌어냅니다."
            ]

            love_analyses = [
                "주변의 시선을 사로잡는 매력 지수가 최고조에 달하는 시기입니다. 자연스러운 만남 속에서 따뜻한 인연의 기운이 다가옵니다.",
                "현재의 관계 또는 새로운 인연과의 소통이 매우 매끄럽게 풀리는 시기입니다. 진솔한 대화가 관계를 한 단계 더 깊게 만들어 줍니다.",
                "내면의 평온함이 매력으로 작용하여 상대방에게 깊은 신뢰와 호감을 줄 수 있는 시기입니다.",
                "오랫동안 마음에 품었던 관계에 진전이 생기거나 뜻밖의 설렘이 찾아오는 로맨틱한 기운이 감돕니다.",
                "상대방과의 공감대가 깊어지며 서로를 향한 마음이 더욱 돈독해지는 행복한 인연의 흐름입니다."
            ]
            love_advices = [
                "상대방의 작은 이야기에 귀 기울이고 공감해 주는 태도가 최고의 매력 포인트가 됩니다.",
                "표현에 인색해하지 말고 따뜻한 말한마디와 미소를 건네보세요. 관계가 급격히 가까워집니다.",
                "내 자신을 먼저 아끼고 사랑할 때 타인과의 관계도 자연스럽고 조화롭게 풀려나갑니다.",
                "작은 이벤트나 다정한 안부 메시지로 상대방의 하루를 기쁘게 만들어 보세요.",
                "솔직하고 담백한 감정 표현이 오해를 없애고 관계를 더욱 단단하게 지켜줍니다."
            ]

            wealth_analyses = [
                "금전 흐름이 안정세로 접어들며, 예기치 않은 작은 행운이나 보상이 따를 수 있는 길운이 들어와 있습니다.",
                "재물운의 흐름이 활발하여 계획적인 자산 관리가 빛을 발하는 시기입니다. 투자나 지출에 있어서 현명한 판단력이 돋보입니다.",
                "불필요한 지출이 줄어들고 시드머니가 차곡차곡 쌓이는 실속 있는 금전운을 보이고 있습니다.",
                "주변의 조언이나 유용한 정보로 인해 자산 관리의 새로운 돌파구가 열리는 시기입니다.",
                "꾸준히 준비해 온 경제적 목표가 가시적인 성과로 나타나며 마음의 여유가 생깁니다."
            ]
            wealth_advices = [
                "충동구매를 자제하고 현재 보유한 자산의 흐름을 꼼꼼히 기록하는 습관을 들이세요.",
                "작은 금전적 여유가 생겼을 때 미래를 위한 투자나 자기 계발에 일부를 투자하면 배로 돌아옵니다.",
                "주변 사람들과의 소중한 나눔과 베풂이 더 큰 재물운을 불러오는 통로가 됩니다.",
                "이번 주에는 큰 지출을 미루고 가계부를 재정비하는 것이 장기적 재물운에 유리합니다.",
                "저축 목표를 구체적으로 설정하고 불필요한 구독 서비스나 고정 지출을 점검해보세요."
            ]

            colors = [
                "로얄 블루 / 동쪽", 
                "에메랄드 그린 / 남쪽", 
                "골드 옐로우 / 서쪽", 
                "퍼플 바이올렛 / 북쪽", 
                "크림 화이트 / 중앙",
                "루비 레드 / 남동쪽",
                "스카이 블루 / 북서쪽"
            ]

            # Independent index calculation for each category to guarantee true variety
            idx_exam = abs_hash % len(exam_analyses)
            idx_exam_adv = (abs_hash // 7) % len(exam_advices)
            idx_love = (abs_hash // 13) % len(love_analyses)
            idx_love_adv = (abs_hash // 17) % len(love_advices)
            idx_wealth = (abs_hash // 19) % len(wealth_analyses)
            idx_wealth_adv = (abs_hash // 23) % len(wealth_advices)
            idx_color = (abs_hash // 29) % len(colors)

            lucky_num = ((abs_hash % 5) + 1)
            secondary_num = (((abs_hash // 3) % 5) + 1)
            number_string = f"{lucky_num}번" if lucky_num == secondary_num else f"{lucky_num}번, {secondary_num}번"

            html_content = textwrap.dedent(f"""
            <div class="custom-box">
                <h2 style='color: #fbbf24; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-top: 0;'>
                    🔮 {user_name} 님의 맞춤 운세 분석 리포트
                </h2>
                
                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #a78bfa;'>📚 1. 시험운 & 합격 기운</h3>
                    <p><b>운세 분석:</b> {exam_analyses[idx_exam]}</p>
                    <p><b>합격 조언:</b> {exam_advices[idx_exam_adv]}</p>
                    <p style='background: rgba(139, 92, 246, 0.2); padding: 12px; border-radius: 8px; border: 1px solid rgba(139, 92, 246, 0.3); margin-top: 10px;'>
                        🍀 <b>시험 추천 번호 (1~5):</b> {number_string} - 수리 오행상 학업과 집중력을 극대화해주는 행운의 번호입니다.
                    </p>
                </div>

                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #f472b6;'>💗 2. 연애운 & 인연의 흐름</h3>
                    <p><b>운세 분석:</b> {love_analyses[idx_love]}</p>
                    <p><b>연애 팁:</b> {love_advices[idx_love_adv]}</p>
                </div>

                <div style='margin-top: 1.5rem;'>
                    <h3 style='color: #34d399;'>💰 3. 재물운 & 금전 흐름</h3>
                    <p><b>운세 분석:</b> {wealth_analyses[idx_wealth]}</p>
                    <p><b>재물 관리 팁:</b> {wealth_advices[idx_wealth_adv]}</p>
                    <p style='background: rgba(16, 185, 129, 0.2); padding: 12px; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.3); margin-top: 10px;'>
                        ✨ <b>행운의 요소:</b> {colors[idx_color]}
                    </p>
                </div>
            </div>
            """)

            st.markdown(html_content, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>© 2026 Intelligent Fortune & Luck Prediction System. Built with Streamlit.</p>", unsafe_allow_html=True)
