
import streamlit as st
from project import FinalCall
import os
from constant import OPENAI_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

st.set_page_config(page_title="Nothing", layout="wide")

st.title("Give Proper Name")

if 'profile_generated' not in st.session_state:
    st.session_state.profile_generated = False

if not st.session_state.profile_generated:
    st.write("Enter a name and company to get information:")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name:")
    with col2:
        company = st.text_input("Company:")
    
    if st.button("Generate Profile"):
        if name and company:
            with st.spinner("Generating profile..."):
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
            st.warning("Please enter both name and company.")



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
        
        st.subheader("Education")
        for edu in education:
            st.write(f"• {edu}")
        
        st.subheader("Work Experience")
        for work in work_experience:
            st.write(f"• {work}")
            
        if courses_certifications:
            st.subheader("Courses and Certifications")
            for course in courses_certifications:
                st.write(f"• {course}")
        
    except Exception as e:
        st.error(f"Error processing background data: {str(e)}")
        st.write("Raw background data:")
        st.write(background_data)

if st.session_state.profile_generated:
    name = st.session_state.profile_data['name']
    company = st.session_state.profile_data['company']
    Summary = st.session_state.profile_data['Summary']
    Facts = st.session_state.profile_data['Facts']
    Interest = st.session_state.profile_data['Interest']
    Background = st.session_state.profile_data['Background']
    IceBreaker = st.session_state.profile_data['IceBreaker']
    Profile = st.session_state.profile_data['Profile']

    col1, col2 = st.columns([1, 3])
    with col1:
        if Profile:
            st.image(Profile, caption=name, width=200)
    with col2:
        st.subheader(f"{name} -  {company}")
        st.write(Summary.ans()['summary'])

    tab1, tab2, tab3, tab4, = st.tabs(["Background", "Facts", "Interests", "Icebreakers"])

    with tab1:
        st.header("Background")
        background_content = Background.ans()
        format_background(background_content)

    with tab2:
        st.subheader("Facts")
        val = Facts.ans()
        for i, fact in enumerate(val['facts'], 1):
            st.write(f"{i}. {fact}")

    with tab3:
        st.subheader("Interests")
        val = Interest.ans()
        for interest in val['interest']:
            st.write(interest)

    with tab4:
        st.subheader("Icebreakers")
        val = IceBreaker.ans()
        for icebreaker in val['icebreaker']:
            st.write(icebreaker)

    if st.button("Generate New Profile"):
        st.session_state.profile_generated = False
        st.experimental_rerun()
else:
    st.info("Enter a name and company to generate a profile.")