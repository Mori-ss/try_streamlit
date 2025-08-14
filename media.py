import streamlit as st
from PIL import Image
from streamlit import caption, audio

# Displaying an image
image = Image.open('C:/Users/ssunk/Downloads/images (2).jpeg')
st.image(image, caption='Okak')

# Displaying a video
video = open('C:/Users/ssunk/Downloads/lastproject — сделано в Clipchamp.mp4', 'rb')
video_data = video.read()
st.video(video_data)

# Displaying audio
audio = open('C:/Users/ssunk/OneDrive/Документы/Аудиозаписи/Конец.m4a', 'rb')
audio_data = audio.read()
st.audio(audio_data)