import streamlit as st

st.markdown(r"<h1 style={text-align:center} >LOLACAP</h1>", unsafe_allow_html=True)

st.write("MP4, MOV, M4A, AVI for video Maximum 200Mo")

is_video_uploded = False

if is_video_uploded == False :
    video_uploded = st.file_uploader("Upload a file for obtaining subtitles", type=('MP4', 'MOV', 'M4A', 'AVI'))
    with st.form("Form 2", border=False):
        st.text_input("Video URL", placeholder="Paste a Youtube URL")
        st.form_submit_button("Load")
else:
    st.video("input.mp4")