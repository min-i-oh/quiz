import streamlit as st

def check_answers(obj_answer, subj_answer):
    correct_obj_answer = "B) 반도체시스템공학부" 
    correct_subj_answer = "새빛관" 

    if obj_answer == correct_obj_answer:
        obj_result = "객관식 정답!"
    else:
        obj_result = f"객관식 오답! 정답은 {correct_obj_answer} 입니다."

    if subj_answer.strip().lower() == correct_subj_answer.lower():
        subj_result = "주관식 정답!"
    else:
        subj_result = f"주관식 오답! 정답은 {correct_subj_answer}입니다."

    return obj_result, subj_result

st.title("퀴즈 서비스")

st.header("객관식 퀴즈")
st.write("다음 중 광운대학교 인공지능융합대학 소속 학부가 아닌 것은?")
options = ["A) 정보융합학부", "B) 반도체시스템공학부", "C)소프트웨어학부", "D) 컴퓨터정보공학부"]
obj_answer = st.radio("선택하세요", options)

st.header("주관식 퀴즈")
st.write("인공지능융합대학 학생회실이 있는 건물의 이름은?")
subj_answer = st.text_input("답을 입력하세요")

if st.button("결과 확인"):
    obj_result, subj_result = check_answers(obj_answer, subj_answer)
    st.write(obj_result)
    st.write(subj_result)
