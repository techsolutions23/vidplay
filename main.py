import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="My Video Website",
        page_icon="▶️",
        layout="centered"
    )
    
    # Your default video (replace with your video path or URL)
    DEFAULT_VIDEO = "https://tenor.com/view/get-lost-get-out-funny-funny-face-oombu-gif-17507725"  # Local file path
    # OR use a URL:
    # DEFAULT_VIDEO = "https://example.com/your_video.mp4"
    
    # HTML video player with autoplay and loop
    video_html = f"""
    <div style="margin: 0 auto; max-width: 800px;">
        <video width="100%" autoplay loop muted playsinline>
            <source src="{DEFAULT_VIDEO}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """
    
    # Display the video
    st.markdown(video_html, unsafe_allow_html=True)
    
    # Optional: Add some text below the video
    st.markdown("---")
    st.markdown("### About This Video")
    st.write("This video plays automatically in a loop when you visit this website.")
    
    # Optional: Style adjustments
    st.markdown("""
    <style>
        video {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
