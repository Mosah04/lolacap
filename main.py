import streamlit as st

st.markdown("<h1 style='text-align:center;' >LOLACAP</h1>", unsafe_allow_html=True)
st.markdown("""<style>
            .st-emotion-cache-1cypcdb.eczjsme11{
                visibility: hidden;
            }
            </style>""", unsafe_allow_html=True)

st.write("MP4, MOV, M4A, AVI for video Maximum 200Mo")

st.session_state.is_video_uploaded = False

def onVideoChange():
    if st.session_state.file_uploaded_video is not None:
        st.session_state.is_video_uploaded = True


video_uploaded = st.file_uploader("Upload a video for obtaining subtitles in Yoruba or Fon", type=('MP4', 'MOV', 'M4A', 'AVI'), key="file_uploaded_video", on_change=onVideoChange)
if video_uploaded:
     st.video(video_uploaded)
with st.form("Form 2", border=False):
    st.text_input("Video URL", placeholder="Paste a Youtube URL", key="youtube_url")
    s_state = st.form_submit_button("Load")
if s_state:
    if st.session_state.youtube_url == "":
        st.warning("Please fill the above fields.")
    else:
        st.success("Submitted successfully")
