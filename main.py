import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="My Video Website",
        page_icon="▶️",
        layout="centered"  # or "wide" for wider layout
    )
    
    # Title
    st.title("Hello 👋")
  
    
    # Your default video (replace with your video path or URL)
    DEFAULT_VIDEO = "your_video.mp4"  # Local file path
    # OR use a URL:
    # DEFAULT_VIDEO = "https://example.com/your_video.mp4"
    
    # Display the video (autoplay doesn't work in Streamlit, user needs to click)
    st.video(DEFAULT_VIDEO)
    

    st.markdown("""
    <style>
        .stVideo {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            autoplay loop muted playsinline
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
