import streamlit as st
import add_subtitle_to_videos as doSub
import subprocess
from moviepy.config import change_settings

# command = "cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g' > /etc/ImageMagick-6/policy.xml"
# subprocess.run(command, shell=True)

# change_settings({"IMAGEMAGICK_BINARY": r"/usr/bin/convert"})

command = "cp -r interFont /usr/share/fonts/truetype/"
subprocess.run(command, shell=True)

command = "fc-cache -f -v"
subprocess.run(command, shell=True)

st.markdown("<h1 style='text-align:center;' >LOLACAP</h1>", unsafe_allow_html=True)
st.markdown("""<style>
            .st-emotion-cache-1cypcdb.eczjsme11{
                display: none;
            }
            </style>""", unsafe_allow_html=True)

st.write("MP4, MOV, M4A, AVI for video Maximum 200Mo")



with st.container( border=True):
    inputP, outputP = st.columns(2)
    with inputP:
        video_uploaded = st.file_uploader("Upload a video for obtaining subtitles in Yoruba or Fon", type=('MP4', 'MOV', 'M4A', 'AVI'), key="file_uploaded_video")
        # col1, col2 = st.columns([5, 1])
        st.markdown("""
                    <style>
                    .st-emotion-cache-ocqkz7.e1f1d6gn5{
                        align-items: flex-end;
                    }
                    </style>
                    """, unsafe_allow_html=True)
        # with col1:
        youtube_url = st.text_input("Youtube video URL", placeholder="Paste a Youtube URL", key="youtube_url")
        # col2.button('Ok')
        col3, col4 = st.columns([2, 1])
        col3.text("Choose output language: ")
        col4.selectbox("", ('Fon', 'Yoruba'), key="output_lang_select")
        st.radio("Hardcoded or not?:", ("Hardcoded", "Softcoded"), key="hard_radio")
        st.markdown("""
                    <style>
                    .st-af.st-ek.st-el.st-em.st-en.st-eo.st-ep{
                        flex-direction: row;
                    }
                    </style>
                    """, unsafe_allow_html=True)
        placeholder = st.empty()
        add_sub_button = st.button('Add subtitles to videos', key="add_sub")
    with outputP:
        output_placeholder = st.empty()
        output_placeholder.markdown("""
                    <style>
                     .st-emotion-cache-1xw8zd0.e1f1d6gn0{
                         min-width: 1000px;
                     }
                     .st-emotion-cache-ocqkz7.e1f1d6gn5 {
                        align-items: center;
                    }
                    .st-emotion-cache-1wncz92.e1nzilvr5 p{
                        text-align: center
                    }
                    </style>
                    """, unsafe_allow_html=True)
        output_placeholder.caption("Here will be displayed your subtitle video")

if video_uploaded:
    placeholder.video(video_uploaded)
    with open("input.mp4", "wb") as f:
        f.write(video_uploaded.getbuffer())
    command = "ls /mount/src/lolacap/"
    subprocess.run(command, shell=True)

if st.session_state.youtube_url: 
        print('AAAA, ', st.session_state.youtube_url)
        doSub.download_youtube(st.session_state.youtube_url);
        placeholder.video(st.session_state.youtube_url);

if st.session_state.add_sub:
    def doRun():
        output_lang =""
        if st.session_state.output_lang_select == "Yoruba":
            output_lang = "yo"
        else:
            output_lang = "fon"
        hardcoded = st.session_state.output_lang_select == "Hardcoded"
        video = doSub.run(output_lang, hardcoded)
        out_container = output_placeholder.container()
        with out_container:
            st.video(video)
            st.download_button('Download subtitled video', video, file_name="LolacapSub.mp4")
    doRun()
    
# video_uploaded = st.file_uploader("Upload a video for obtaining subtitles in Yoruba or Fon", type=('MP4', 'MOV', 'M4A', 'AVI'), key="file_uploaded_video", on_change=onVideoChange)
# if video_uploaded:
#      st.video(video_uploaded)
#      st.session_state.youtube_url = "www"
# with st.form("Form 2", border=False):
#     st.text_input("Video URL", placeholder="Paste a Youtube URL", key="youtube_url")
#     s_state = st.form_submit_button("Load")
# if s_state:
#     if st.session_state.youtube_url == "":
#         st.warning("Please fill the above fields.")
#     else:
#         st.success("Submitted successfully")
