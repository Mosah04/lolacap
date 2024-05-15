# -*- coding: utf-8 -*-
import subprocess
import json
import time
import math
import ffmpeg
import pytube
import http.client
from moviepy.editor import *
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
from faster_whisper import WhisperModel

command = "cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g' > /etc/ImageMagick-6/policy.xml"
subprocess.run(command, shell=True)

change_settings({"IMAGEMAGICK_BINARY": r"/usr/bin/convert"})

command = "sudo cp -r Inter /usr/share/fonts/truetype/"
subprocess.run(command, shell=True)

command = "sudo fc-cache -f -v"
subprocess.run(command, shell=True)

input_video = "input.mp4"
def download_youtube(url : str):
    input_video_name = input_video.replace(".mp4", "")
    yt = pytube.YouTube(url)
    # Filter and get the highest resolution video
    video = yt.streams.filter(res="720p").first()
    # Download the video
    video.download(filename="input.mp4")

def extract_audio():
    extracted_audio = f"audio-{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

def transcribe(audio):
    model = WhisperModel("small")
    segments, info = model.transcribe(audio)
    language = info[0]
    print("Transcription language", info[0])
    segments = list(segments)
    for segment in segments:
        # print(segment)
        print("[%.2fs -> %.2fs] %s" %
              (segment.start, segment.end, segment.text))
    return language, segments

def format_time(seconds):

    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

    return formatted_time

def generate_subtitle_file(language, segments, translated_texts=None):
    subtitle_file = f"sub-input.{language}.srt"
    text = ""
    if translated_texts:
        translated_lines = translated_texts.split("\n")
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        text += f"{str(index+1)} \n"
        text += f"{segment_start} --> {segment_end} \n"
        if translated_texts:
            text += f"{translated_lines[index]} \n"
        else:
            text += f"{segment.text} \n"
        text += "\n"

    with open(subtitle_file, "w") as f:
        f.write(text)

    return subtitle_file

def translate(input_phrase, source_lang, target_lang):
    conn = http.client.HTTPSConnection("translator-api.glosbe.com")
    payload = input_phrase
    headers = {'Content-Type': 'text/plain'}
    try:
        conn.request("POST", f"/translateByLangDetect?sourceLang={source_lang}&targetLang={target_lang}", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return json.loads(data)['translation']
    except (http.client.HTTPException, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

def add_subtitle_to_video(soft_subtitle, subtitle_file,  subtitle_language):

    video_input_stream = ffmpeg.input(input_video)
    subtitle_input_stream = ffmpeg.input(subtitle_file)
    output_video = f"output-{input_video_name}.mp4"
    subtitle_track_title = subtitle_file.replace(".srt", "")

    if soft_subtitle:
        stream = ffmpeg.output(
            video_input_stream, subtitle_input_stream, output_video, **{"c": "copy", "c:s": "mov_text"},
            **{"metadata:s:s:0": f"language={subtitle_language}",
            "metadata:s:s:0": f"title={subtitle_track_title}"}
        )
        ffmpeg.run(stream, overwrite_output=True)

    if soft_subtitle:
        ...
    else:
        stream = ffmpeg.output(video_input_stream, output_video,
                               vf=f"subtitles={subtitle_file}:force_style='Fontname=Trebuchet MS'")
        ffmpeg.run(stream, overwrite_output=True)

def run():

    extracted_audio = extract_audio()
    language, segments = transcribe(extracted_audio)
    subtitle_file = generate_subtitle_file(
    language=language,
    segments=segments
    )

    segments_texts = [segment.text for segment in segments]
    all_texts = "\r\n".join(segments_texts)
    segments_texts_fon = translate(all_texts, language, 'fon')

    subtitle_file_fon = generate_subtitle_file(
    language='fon',
    segments=segments,
    translated_texts=segments_texts_fon
    )

    add_subtitle_to_video(
      soft_subtitle=False,
      subtitle_file=subtitle_file_fon,
      subtitle_language='fon'
    )

run()

# !wget https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip
# !unzip Inter-4.0.zip -d Inter
# !rm Inter-4.0.zip
# !sudo cp -r Inter /usr/share/fonts/truetype/
# !sudo fc-cache -f -v
# from moviepy.editor import TextClip
# TextClip.list('font')

# from moviepy.video.tools.subtitles import SubtitlesClip
# from moviepy.video.io.VideoFileClip import VideoFileClip
generator = lambda text: TextClip(text, font='Inter-Regular',
                                  fontsize=24, color='white')
subtitles = SubtitlesClip("sub-input.fon.srt", generator)
clip = VideoFileClip("input.mp4")
final = CompositeVideoClip([clip, subtitles])
final.write_videofile("final.mp4", fps=clip.fps)