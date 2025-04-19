import streamlit as st
from pathlib import Path

# Hide all Streamlit UI elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Video path (replace with your video file or URL)
VIDEO_PATH = "your_video.mp4"  # Local file
# VIDEO_PATH = "https://example.com/your_video.mp4"  # Or URL

# HTML video player with autoplay and loop
video_html = f"""
<div style="margin: 0 auto; max-width: 100%;">
    <video width="100%" height="auto" autoplay loop muted playsinline>
        <source src="{VIDEO_PATH}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
"""

# Display the video (will auto-play if browser allows)
st.markdown(video_html, unsafe_allow_html=True)
