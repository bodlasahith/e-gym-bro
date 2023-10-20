import streamlit as st
import cv2
import tempfile
import time  # Import the time module

def process_video(uploaded_file):
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    video_file_path = tfile.name  # Get the file path of the temporary file

    # Load the video file
    video = cv2.VideoCapture(video_file_path)

    # Check if video file opened successfully
    if not video.isOpened():
        st.error("Could not open the video file.")
        return

    # Get video frame count and fps
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Process and display each frame
    for i in range(frame_count):
        ret, frame = video.read()
        if ret:
            # Convert the frame to RGB (OpenCV uses BGR by default)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame_rgb, channels="RGB")
            # Sleep for the appropriate amount of time to achieve the original video speed
            time.sleep(1.0 / fps)  # Corrected line
        else:
            st.warning("Failed to retrieve frame.")
            break

    # Release the video file
    video.release()

# Upload the video file
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
if uploaded_file is not None:
    process_video(uploaded_file)
