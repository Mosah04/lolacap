import streamlit as st

st.markdown(r"<h1 style={text-align:center} >LOLACAP</h1>", unsafe_allow_html=True)

st.write("MP4, MOV, M4A, AVI for video Maximum 200Mo")

is_video_uploded = False

def onVideoChange():
    # if st.session_state.file_uploaded_video:
    pass

if is_video_uploded == False :
    video_uploaded = st.file_uploader("Upload a file for obtaining subtitles", type=('MP4', 'MOV', 'M4A', 'AVI'), key="file_uploaded_video", on_change=onVideoChange)
    with st.form("Form 2", border=False):
        st.text_input("Video URL", placeholder="Paste a Youtube URL")
        st.form_submit_button("Load")
else:
    st.video("input.mp4")