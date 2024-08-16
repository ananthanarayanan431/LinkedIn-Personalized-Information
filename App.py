import streamlit as st
from project import FinalCall
import os
from constant import OPENAI_API_KEY


st.set_page_config(page_title="Professional Profile Generator", layout="wide")

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0.3rem;
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 0.3rem;
    }
    h1 {
        color: #2C3E50;
        border-bottom: 2px solid #2C3E50;
        padding-bottom: 10px;
    }
    h2 {
        color: #34495E;
    }
    h3 {
        color: #16A085;
    }
    .stTab {
        background-color: #ECF0F1;
        border-radius: 0.3rem;
        padding: 0.5rem;
    }
    .stImage {
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

if 'profile_generated' not in st.session_state:
    st.session_state.profile_generated = False


def format_background(background_data):
    try:
        background_list = background_data['background']

        education = []
        work_experience = []
        courses_certifications = []

        for item in background_list:
            if item.startswith("Education:"):
                education.append(item.replace("Education: ", ""))
            elif item.startswith("Work Experience:"):
                work_experience.append(item.replace("Work Experience: ", ""))
            elif item.startswith("Courses and Certifications:"):
                courses_certifications.append(item.replace("Courses and Certifications: ", ""))

        if education:
            st.subheader("📚 Education")
            for edu in education:
                st.markdown(f"- {edu}")

        if work_experience:
            st.subheader("💼 Work Experience")
            for work in work_experience:
                st.markdown(f"- {work}")

        if courses_certifications:
            st.subheader("🏆 Courses and Certifications")
            for course in courses_certifications:
                st.markdown(f"- {course}")

    except Exception as e:
        st.error(f"Error processing background data: {str(e)}")
        st.write("Raw background data:")
        st.write(background_data)


if not st.session_state.profile_generated:
    st.write("Enter a name and company to generate a professional profile:")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name:", placeholder="e.g. John Doe")
    with col2:
        company = st.text_input("Company:", placeholder="e.g. Tech Innovators Inc.")

    if st.button("Generate Profile", key="generate_button"):
        if name and company:
            with st.spinner("Generating profile... This may take a moment."):
                Summary, Facts, Interest, Background, IceBreaker, Profile = FinalCall(name, company)
            st.session_state.profile_generated = True
            st.session_state.profile_data = {
                'name': name,
                'company': company,
                'Summary': Summary,
                'Facts': Facts,
                'Interest': Interest,
                'Background': Background,
                'IceBreaker': IceBreaker,
                'Profile': Profile
            }
            st.experimental_rerun()
        else:
            st.warning("⚠️ Please enter both name and company.")

if st.session_state.profile_generated:
    name = st.session_state.profile_data['name']
    company = st.session_state.profile_data['company']
    Summary = st.session_state.profile_data['Summary']
    Facts = st.session_state.profile_data['Facts']
    Interest = st.session_state.profile_data['Interest']
    Background = st.session_state.profile_data['Background']
    IceBreaker = st.session_state.profile_data['IceBreaker']
    Profile = st.session_state.profile_data['Profile']

    st.markdown(f"# Profile for {name}")
    st.markdown(f"## 🏢 {company}")

    col1, col2 = st.columns([1, 3])
    with col1:
        if Profile:
            st.image(Profile, caption=name, width=200, use_column_width=True)
    with col2:
        st.markdown("### 📝 Summary")
        st.write(Summary.ans()['summary'])

    tabs = st.tabs(["🎓 Background", "📊 Facts", "🌟 Interests", "💬 Icebreakers"])

    with tabs[0]:
        background_content = Background.ans()
        format_background(background_content)

    with tabs[1]:
        st.subheader("📊 Facts")
        val = Facts.ans()
        for i, fact in enumerate(val['facts'], 1):
            st.markdown(f"{i}. {fact}")

    with tabs[2]:
        st.subheader("🌟 Interests")
        interest_data = Interest.ans()
        for item in interest_data['Interest']:
            st.markdown(f"### 📌 {item['Topic_of_Interest']}")
            st.markdown(f"**Justification**: {item['Justification']}")
            st.markdown(f"**Supporting Evidence**: {item['Supporting_Evidence']}")
            st.markdown(f"**Potential Engagement**: {item['Potential_Engagement']}")
            st.markdown("---")

    with tabs[3]:
        st.subheader("💬 Icebreakers")
        val = IceBreaker.ans()
        for icebreaker in val['icebreaker']:
            st.markdown(f"- {icebreaker}")

    if st.button("Generate New Profile", key="new_profile_button"):
        st.session_state.profile_generated = False
        st.experimental_rerun()
else:
    st.info("👆 Enter a name and company above to generate a professional profile.")