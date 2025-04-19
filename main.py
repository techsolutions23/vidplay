import streamlit as st
from pathlib import Path

# Set page config to remove all padding and margins
st.set_page_config(layout="centered", page_title="Video Player", page_icon="▶️")

# Hide all Streamlit UI elements completely
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {margin: 0; padding: 0;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Video configuration (CHANGE THIS TO YOUR VIDEO PATH OR URL)
VIDEO_FILE = "your_video.mp4"  # For local file
# VIDEO_FILE = "https://example.com/your_video.mp4"  # For web URL

# HTML video player with autoplay and loop
video_html = f"""
<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; overflow: hidden; margin: 0; padding: 0; background-color: black;">
    <video width="100%" height="100%" autoplay loop muted playsinline style="object-fit: cover;">
        <source src="{VIDEO_FILE}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
"""

# Display the video
st.markdown(video_html, unsafe_allow_html=True)

# Add a tiny invisible element to prevent Streamlit from showing empty space
st.markdown("<div style='height: 1px; visibility: hidden;'></div>", unsafe_allow_html=True)
